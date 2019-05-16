from django.template import Library

register = Library()


@register.filter
def do_listreverse(list):
    list.reverse()
    return list
