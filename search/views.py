from django_elasticsearch_dsl_drf.constants import (
    LOOKUP_FILTER_RANGE,
    LOOKUP_QUERY_GT,
    LOOKUP_QUERY_GTE,
    LOOKUP_QUERY_IN,
    LOOKUP_QUERY_LT,
    LOOKUP_QUERY_LTE,
    SUGGESTER_COMPLETION,
)
from django.views.decorators.csrf import csrf_exempt
from django_elasticsearch_dsl_drf.filter_backends import (
    DefaultOrderingFilterBackend,
    FacetedSearchFilterBackend,
    FilteringFilterBackend,
    SearchFilterBackend,
    SuggesterFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet

from .documents import UserDocument
from .serializers import UserDocumentSerializer
from elasticsearch import Elasticsearch
from django.http import JsonResponse


class UserViewSet(DocumentViewSet):
    document = UserDocument
    serializer_class = UserDocumentSerializer
    ordering = ('id',)
    lookup_field = 'id'

    filter_backends = [
        DefaultOrderingFilterBackend,
        FacetedSearchFilterBackend,
        FilteringFilterBackend,
        SearchFilterBackend,
        SuggesterFilterBackend,
    ]

    search_fields = (
        'name',
    )

    filter_fields = {
        'id': {
            'field': 'id',
            'lookups': [
                LOOKUP_FILTER_RANGE,
                LOOKUP_QUERY_IN,
                LOOKUP_QUERY_GT,
                LOOKUP_QUERY_GTE,
                LOOKUP_QUERY_LT,
                LOOKUP_QUERY_LTE,
            ],
        },
        'name': 'name',
    }

    suggester_fields = {
        'name_suggest': {
            'field': 'name.suggest',
            'suggesters': [
                SUGGESTER_COMPLETION,
            ],
        },
    }


def search_user(request, name):
    es = Elasticsearch()
    res = es.search(index="users", body={
    "query": {
        "query_string": {
            "query": f"({name}*)",
            "default_field": "name"
            }
        }
    })
    return JsonResponse(res)


def search_discussion_basis_on_id(request, index):
    es = Elasticsearch()
    res = es.search(index="posts", body={
        "query": {
            "nested": {
                "path": "speciality",
                "query": {
                    "bool": {
                        "must": [
                            {"match": {"speciality.id": f"{index}"}}
                        ]
                    }
                }
            }
        }
    })
    return JsonResponse(res)


def search_discussion_basis_on_message(request, message):
    es = Elasticsearch()
    res = es.search(index="posts", body={
    "query": {
        "query_string": {
            "query": f"({message}*)",
            "default_field": "message"
            }
        }
    })
    return JsonResponse(res)


def should_discussion_basis_on_list(request):
    list_of_specialities = request.GET.get('list_of_specialities')
    print(list_of_specialities)
    specialities = list_of_specialities.strip('][')
    specialities = specialities.split(",")
    print(specialities)
    es = Elasticsearch()
    match_records = []
    for speciality in specialities:
        match = {
            "match": {
                "speciality.name": f"{speciality[1:-1]}"
            }
        }
        match_records.append(match)
    print(match_records)
    res = es.search(index="posts", body={
        "query": {
            "nested": {
                "path": "speciality",
                "query": {
                    "bool": {
                        "should": match_records
                    }
                }
            }
        }
    })
    return JsonResponse(res)


def must_discussion_basis_on_list(request):
    list_of_specialities = request.GET.get('list_of_specialities')
    specialities = list_of_specialities.strip('][')
    specialities = specialities.split(",")
    es = Elasticsearch()
    match_records = []
    for speciality in specialities:
        match = {
            "match": {
                "speciality.name": f"{speciality[1:-1]}"
            }
        }
        match_records.append(match)
    res = es.search(index="posts", body={
        "query": {
            "nested": {
                "path": "speciality",
                "query": {
                    "bool": {
                        "must": match_records
                    }
                }
            }
        }
    })
    return JsonResponse(res)


