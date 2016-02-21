from django.conf.urls import url

from .views import fiddle_view


urlpatterns = [
    url(r'^$', fiddle_view, name='fiddle-view'),
]
