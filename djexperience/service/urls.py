from django.conf.urls import include, url
from djexperience.service import views as s


protest_patterns = [
    url(r'^$', s.ProtestList.as_view(), name='protest_list'),
    url(r'^add/$', s.ProtestCreate.as_view(), name='protest_add'),
    url(r'^(?P<pk>\d+)/$', s.ProtestDetail.as_view(), name='protest_detail'),
]


urlpatterns = [
    url(r'^protest/', include(protest_patterns)),
]
