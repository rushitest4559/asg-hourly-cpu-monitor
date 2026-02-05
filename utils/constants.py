from datetime import timezone, timedelta

# Timezone
IST = timezone(timedelta(hours=5, minutes=30))

# CloudWatch
CPU_METRIC_NAME = "CPUUtilization"
CPU_NAMESPACE = "AWS/EC2"

# Tag keys
OWNER_TAG = "OwnerEmail"

# Metric window
METRIC_PERIOD_SECONDS = 3600  # 1 hour

# Email defaults
DEFAULT_SENDER = "noreply@example.com"

# Logging
LOG_FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
LOG_LEVEL = "INFO"
