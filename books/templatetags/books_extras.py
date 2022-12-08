from datetime import datetime

from django import template

register = template.Library()

@register.filter
def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')


@register.simple_tag
def current_time(format_string):
    return datetime.now().strftime(format_string)

# register.filter('cut', cut)