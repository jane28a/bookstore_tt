from datetime import datetime

from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag
def copyright():
    start = str(getattr(settings, 'COPYRIGHT_START', ''))
    end = str(datetime.now().year)
    if start:
        years = ' - '.join([start, end])
    else:
        years = end
    return ' '.join(['Copyright', years])
