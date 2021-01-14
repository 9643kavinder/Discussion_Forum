from rest_framework.routers import SimpleRouter

from . import views


app_name = 'search'

router = SimpleRouter()
router.register(
    prefix=r'users',
    basename='users',
    viewset=views.UserViewSet
)
urlpatterns = router.urls