from django.conf import settings
from django.conf.urls import url, include
from django.views.generic import TemplateView
from pets.views import PetViewSet
from rest_framework import routers

from project.admin import owners_admin, admin

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='pets/index.html'), name='home'),
    url(r'^admin/', admin.urls),
    url(r'^owners-admin/', owners_admin.urls),
    url(r'^', include('pets.urls')),
]

# API
router = routers.DefaultRouter()
router.register(r'pets', PetViewSet, base_name='pet')
urlpatterns += [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

