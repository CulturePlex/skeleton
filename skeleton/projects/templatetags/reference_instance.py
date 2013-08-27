from django import template
from projects.models import BookReference

register = template.Library()

def book_instance(inst):
	return isinstance(inst, BookReference)

register.filter('book_instance', book_instance)




