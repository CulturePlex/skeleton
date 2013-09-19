from django import template
from projects.models import BookReference, JournalReference

register = template.Library()


def book_instance(inst):
    return isinstance(inst, BookReference)

register.filter('book_instance', book_instance)


def journal_instance(inst):
    return isinstance(inst, JournalReference)

register.filter('journal_instance', journal_instance)
