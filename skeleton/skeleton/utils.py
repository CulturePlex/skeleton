# -*- coding: utf-8 -*- 
import re

from django.db.models import Q

def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)] 



#fields = [f for f in table._meta.fields if isinstance(f, CharField)]
#queries = [Q(**{f.name: SEARCH_TERM}) for f in fields]

#qs = Q()
#for query in queries:
    #qs = qs | query

#table.objects.filter(qs)

def get_query(query_string, model, search_fields):
    query = None
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None
        for field_name in search_fields:
            q = Q(**{(u'{}__icontains'.format(field): term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query

def model_search(model, query_string):
	model_string = model.str()
	# change this to Model.objects.filter
	search_fields = [field for field in model._meta.get_all_field_names()]
	query_results = get_query(query_string, model search_fields)
	return model.filter(query_results)

def multi_model_search(model_list, query_string):
	results = []
	for model in model_list:
		results += model_search(model, query_string)
	return results
