from rest_framework.routers import SimpleRouter
from django.urls import path, include
from . import views


app_name = 'search'

router = SimpleRouter()
router.register(
    prefix=r'users',
    basename='users',
    viewset=views.UserViewSet
)
urlpatterns = [
    path('', include(router.urls)),
    path('user/<str:name>/', views.search_user, name="search_user")
]