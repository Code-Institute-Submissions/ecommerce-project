from django.conf.urls import url
from .views import all_bugs, add_bug, one_bug, comment


urlpatterns = [
    url(r'^$', all_bugs, name='bugs'),
    url(r'^add/$', add_bug, name='add_bugs'),
    url(r'^comment/(?P<bug_id>.*)$', comment, name='comment_bug'),
    url(r'^(?P<bug_id>.*)$', one_bug, name='one_bugs'),
    ]
