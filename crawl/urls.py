from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^blocks/(?P<time>[0-9]{13})', views.block_detail, name='block_detail'),
]