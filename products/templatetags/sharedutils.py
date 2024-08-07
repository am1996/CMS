from django import template

register = template.Library()

@register.filter(name="split")
def split(data,delimiter):
    return data.split(delimiter)