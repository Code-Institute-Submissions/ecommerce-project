from django.conf.urls import url
from .views import all_features, add_feature, one_feature, comment, vote, edit, delete


urlpatterns = [
    url(r'^$', all_features, name='features'),
    url(r'^add/$', add_feature, name='add_features'),
    url(r'^features/(?P<feature_id>.*)$', comment, name='comment_feature'),
    url(r'^vote/(?P<feature_id>.*)$', vote, name='vote_feature'),
    url(r'^edit/(?P<feature_id>.*)$', edit, name='edit_feature'),
    url(r'^delete/(?P<feature_id>.*)$', delete, name='del_feature'),
    url(r'^(?P<feature_id>.*)$', one_feature, name='one_feature'),
]