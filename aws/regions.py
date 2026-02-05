import boto3


def get_all_regions():
    """
    Fetch all available AWS regions.
    """
    ec2 = boto3.client("ec2")
    response = ec2.describe_regions()

    return [r["RegionName"] for r in response["Regions"]]
