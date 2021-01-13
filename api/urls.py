from rest_framework.urlpatterns import format_suffix_patterns
from . import views as api_views
from django.urls import path, include


urlpatterns = [
    path('', api_views.home, name="home"),
    path('<str:name>/', api_views.PostView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
