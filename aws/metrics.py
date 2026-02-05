import boto3
from datetime import datetime, timezone, timedelta


def get_cpu_metrics(region_name: str, asg_name: str, created_time):
    """
    Fetch hourly CPU metrics for an ASG from CloudWatch.
    """
    cw = boto3.client("cloudwatch", region_name=region_name)

    now_utc = datetime.now(timezone.utc)
    default_start_time = now_utc - timedelta(hours=24)

    start_time = max(created_time, default_start_time)

    response = cw.get_metric_statistics(
        Namespace="AWS/EC2",
        MetricName="CPUUtilization",
        Dimensions=[
            {"Name": "AutoScalingGroupName", "Value": asg_name}
        ],
        StartTime=start_time,
        EndTime=now_utc,
        Period=3600,
        Statistics=["Average", "Maximum"],
    )

    cpu_data = {
        dp["Timestamp"]: {
            "avg": dp.get("Average"),
            "max": dp.get("Maximum"),
        }
        for dp in response["Datapoints"]
    }

    return cpu_data
