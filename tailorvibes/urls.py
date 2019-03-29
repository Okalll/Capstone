from django.conf.urls import url
from . import views
from .views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^tailors',views.tailors, name='tailors'),
    url(r'^index',views.index, name='index'),
    url(r'^hire',views.hire, name='hire'),
    url(r'^market',views.market, name='market'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
