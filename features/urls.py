from django.conf.urls import url
from .views import all_features, add_feature, one_feature, comment


urlpatterns = [
    url(r'^$', all_features, name='features'),
    url(r'^add/$', add_feature, name='add_features'),
    url(r'^features/(?P<feature_id>.*)$', comment, name='comment_feature'),
    url(r'^(?P<feature_id>.*)$', one_feature, name='one_feature'),
    ]
