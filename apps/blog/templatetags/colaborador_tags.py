from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.simple_tag
def has_group(user, group_name):
    try:
        group = Group.objects.get(name=group_name)
        has_permission = (group in user.groups.all()) or user.is_superuser
        return has_permission
    except Group.DoesNotExist:
        return False