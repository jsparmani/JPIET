from django import template

register = template.Library()

@register.filter
def count4(value):
	if value<=4:
		return True
	else:
		return False