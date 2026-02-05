import boto3


def fetch_asgs(region_name: str):
    """
    Fetch all ASGs in a region with basic metadata.
    """
    client = boto3.client("autoscaling", region_name=region_name)
    paginator = client.get_paginator("describe_auto_scaling_groups")

    asg_list = []

    for page in paginator.paginate():
        for asg in page["AutoScalingGroups"]:
            tags = {t["Key"]: t["Value"] for t in asg.get("Tags", [])}

            asg_list.append(
                {
                    "region": region_name,
                    "name": asg["AutoScalingGroupName"],
                    "created_time": asg["CreatedTime"],
                    "min_size": asg["MinSize"],
                    "desired_capacity": asg["DesiredCapacity"],
                    "max_size": asg["MaxSize"],
                    "tags": tags,
                }
            )

    return asg_list
