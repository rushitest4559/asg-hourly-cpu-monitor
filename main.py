from datetime import datetime, timezone, timedelta

from aws.regions import get_all_regions
from aws.asg import fetch_asgs
from aws.metrics import get_cpu_metrics

from processing.aggregator import group_by_owner
from processing.formatter import format_owner_report
from processing.validator import validate_asg

from notifications.email_client import EmailClient
from notifications.templates import build_subject, build_html

from config import (
    SMTP_SERVER,
    SMTP_PORT,
    SMTP_USERNAME,
    SMTP_PASSWORD,
    EMAIL_SENDER,
)

from utils.logger import get_logger

logger = get_logger(__name__)


def main():
    logger.info("Starting ASG CPU monitoring...")

    now = datetime.now(timezone.utc)
    window_end = now
    window_start = now - timedelta(hours=24)

    regions = get_all_regions()
    print(f"\n🌍 Total Regions Found: {len(regions)}")

    all_asgs = []

    for region in regions:
        print(f"\n➡️ Processing Region: {region}")

        asgs = fetch_asgs(region)
        print(f"   🔎 ASGs Found: {len(asgs)}")

        for asg in asgs:
            print(f"      📦 Processing ASG: {asg['name']}")

            metrics = get_cpu_metrics(
                region,
                asg["name"],
                asg["created_time"]
            )

            is_valid, issues = validate_asg(asg)

            if not is_valid:
                print(f"      ⚠️ Skipped Invalid ASG: {asg['name']} | Issues: {issues}")
                continue

            if metrics:
                print(f"      📊 Metrics collected: {len(metrics)} datapoints")
                asg["cpu_metrics"] = metrics
                all_asgs.append(asg)
            else:
                print(f"      ❌ No metrics found")

    print(f"\n👥 Total Valid ASGs Collected: {len(all_asgs)}")

    owner_groups = group_by_owner(all_asgs)
    print(f"📧 Owners to notify: {len(owner_groups)}")

    reports = {}
    for owner_email, asgs in owner_groups.items():
        print(f"   📨 Preparing report for: {owner_email} | ASGs: {len(asgs)}")
        reports[owner_email] = format_owner_report(
            owner_email,
            asgs,
            window_start,
            window_end
        )

    email_client = EmailClient(
        SMTP_SERVER,
        SMTP_PORT,
        SMTP_USERNAME,
        SMTP_PASSWORD,
        EMAIL_SENDER,
    )
    email_client.connect() 

    for owner_email, data in reports.items():
        print(f"   ✉️ Sending email to: {owner_email}")
        subject = build_subject()
        html = build_html(owner_email, data["asgs"])

        email_client.send_email(owner_email, subject, html)

    email_client.disconnect()

    logger.info("Email process completed.")


if __name__ == "__main__":
    main()
