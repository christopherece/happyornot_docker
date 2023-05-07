from django import template

register = template.Library()

@register.filter(name='emoji')
def emoji(value):
    if value == 1:
        return '😞'
    elif value == 2:
        return '🙁'
    elif value == 3:
        return '😐'
    elif value == 4:
        return '🙂'
    elif value == 5:
        return '😀'
