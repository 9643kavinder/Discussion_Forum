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
    path('user/<str:name>/', views.search_user, name="search_user"),
    path('discussion/<int:index>/', views.search_discussion_basis_on_id, name="search_discussions"),
    path('discussion/<str:message>/', views.search_discussion_basis_on_message, name="discussion_message"),
    path('should/', views.should_discussion_basis_on_list, name="should_discussions"),
    path('must/', views.must_discussion_basis_on_list, name="must_discussions"),

]