from django.conf.urls import url, include
from rest_framework import routers
from django.urls import path
from app.views import UserViewSet, ArticlesViewSet, LoginViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'login', LoginViewSet, base_name='login')
router.register(r'articles', ArticlesViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include(
        'rest_framework.urls', namespace='rest_framework')),
    path('accounts/', include('rest_registration.api.urls'))
]