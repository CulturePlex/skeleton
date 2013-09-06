# -*- coding: utf-8 -*- 
import re

from itertools import chain

from django.db.models import Q, CharField, TextField

#####################################################################
# From Julian Phalip 
# http://julienphalip.com/post/2825034077/adding-search-to-a-django-site-in-a-snap
def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)] 

def get_query(query_string, search_fields):
    q_set = None
    search_terms = normalize_query(query_string)
    for term in search_terms:
        or_query = None
        for field_name in search_fields:
            q = Q((u'{0}__icontains'.format(field_name)=term)
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            q_set = q_set & or_query    
    return q_set

#####################################################################

def model_search(model, query_string):
    search_fields = [
        field for field in model._meta.get_all_field_names() 
        if isinstance(field, CharField) or if isinstance(field, TextField)
        ]
    q_set = get_query(query_string, search_fields)
    return model.objects.filter(q_set)

def multi_model_search(model_list, query_string):
    results = []
    for model in model_list:
        results.append(model_search(model, query_string))
    results = chain.from_iterable(results)
    return results

    
