from datetime import timezone, timedelta

IST = timezone(timedelta(hours=5, minutes=30))


def format_owner_report(owner_email, asg_records, window_start, window_end):
    """
    Builds report ensuring every hour is shown.
    - Missing metrics -> 'No instances'
    - CPU 0% -> shown normally
    """

    report = {
        "owner": owner_email,
        "asgs": [],
    }

    for asg in asg_records:
        created_ist = asg["created_time"].astimezone(IST)

        formatted_asg = {
            "region": asg["region"],
            "name": asg["name"],
            "created": created_ist.strftime("%Y-%m-%d %H:%M:%S"),
            "capacity": f'{asg["min_size"]}/{asg["desired_capacity"]}/{asg["max_size"]}',
            "metrics": [],
        }

        cpu_data = asg.get("cpu_metrics", {})

        # build full hourly timeline
        current = window_start.replace(minute=0, second=0, microsecond=0)

        while current <= window_end:
            ts_ist = current.astimezone(IST)

            if current in cpu_data:
                avg = cpu_data[current].get("avg")
                maxv = cpu_data[current].get("max")

                formatted_asg["metrics"].append({
                    "time": ts_ist.strftime("%Y-%m-%d %H:%M"),
                    "avg_cpu": f"{avg:.2f}" if avg is not None else "NA",
                    "max_cpu": f"{maxv:.2f}" if maxv is not None else "NA",
                })
            else:
                formatted_asg["metrics"].append({
                    "time": ts_ist.strftime("%Y-%m-%d %H:%M"),
                    "avg_cpu": "No instances",
                    "max_cpu": "No instances",
                })

            current += timedelta(hours=1)

        report["asgs"].append(formatted_asg)

    return report
