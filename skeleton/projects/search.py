# -*- coding: utf-8 -*-
import re
from django.db.models import Q, CharField, TextField

#####################################################################
# Modified from Julian Phalip
# http://julienphalip.com/post/2825034077/
#  adding-search-to-a-django-site-in-a-snap


def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    return [
        normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)
    ]


def get_query(query_string, search_fields):
    q_set = {}
    search_terms = normalize_query(query_string)
    for term in search_terms:
        or_query = None
        for field_name in search_fields:
            q = Q(**{"{0}__icontains".format(field_name): term})
            q_set[field_name] = q
    return q_set

#####################################################################


def model_search(model, query_string):
    results_dict = {}
    search_fields = [
        field for field in model._meta.fields if
        isinstance(field, CharField) or isinstance(field, TextField)
    ]
    search_fields = [
        field.name for field in search_fields if field.name != 'slug'
    ]
    q_set = get_query(query_string, search_fields)
    #import ipdb; ipdb.set_trace()
    for field, value in q_set.items():
        results = model.objects.filter(value)
        if results:
            for result in results:
                results_dict.setdefault(result, [])
                results_dict[result].append(field)
    return results_dict


def multi_model_search(model_list, query_string):
    results = []
    for model in model_list:
        search = model_search(model, query_string)
        for key, vals in search.iteritems():
            results += [{key: vals}]
    #import ipdb; ipdb.set_trace()
    return results
