def validate_asg(asg_record):
    """
    Validate ASG record before processing.
    Returns (is_valid, issues_list)
    """

    issues = []

    if not asg_record.get("name"):
        issues.append("Missing ASG name")

    if not asg_record.get("region"):
        issues.append("Missing region")

    if "OwnerEmail" not in asg_record.get("tags", {}):
        issues.append("Missing OwnerEmail tag")

    return (len(issues) == 0, issues)


def validate_metrics(cpu_metrics):
    """
    Validate CPU metric payload.
    """
    if not cpu_metrics:
        return False

    return True
