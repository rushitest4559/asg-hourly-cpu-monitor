from collections import defaultdict


def group_by_owner(asg_records):
    """
    Group ASG records by OwnerEmail tag.
    Returns dict: { owner_email: [asg_records] }
    """

    grouped = defaultdict(list)

    for asg in asg_records:
        owner_email = asg.get("tags", {}).get("OwnerEmail")

        if owner_email:
            owner_email = owner_email.strip().lower()
        else:
            owner_email = "unassigned"

        grouped[owner_email].append(asg)

    return dict(grouped)
