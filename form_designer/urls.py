from django.conf.urls import url
from form_designer.views import detail, detail_by_hash


urlpatterns = [
    url(r'^(?P<object_name>[-\w]+)/$', detail, name='form_designer_detail'),
    url(r'^h/(?P<public_hash>[-\w]+)/$', detail_by_hash, name='form_designer_detail_by_hash'),
]
