import os
from dotenv import load_dotenv

load_dotenv()

# AWS
AWS_PROFILE = os.getenv("AWS_PROFILE", "default")

# SMTP / Email
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
EMAIL_SENDER = os.getenv("EMAIL_SENDER")

# Metrics
CPU_NAMESPACE = "AWS/EC2"
CPU_METRIC_NAME = "CPUUtilization"
PERIOD_SECONDS = 3600  # 1 hour

# Time Window
LOOKBACK_HOURS = int(os.getenv("LOOKBACK_HOURS", 24))
