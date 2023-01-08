from django.contrib.auth.models import Group

from app import constants


def create_group_if_not_exists(group_name):
    # Check if a group with the given name already exists
    group = Group.objects.filter(name=group_name).first()
    if group is None:
        # Create the group if it does not exist
        group = Group(name=group_name)
        group.save()
    else:
        print(f'Group with name:{group_name} already exists')


# Use the function to create a group
create_group_if_not_exists(constants.STUDENT)
create_group_if_not_exists(constants.WORKER)
create_group_if_not_exists(constants.MANAGER)
