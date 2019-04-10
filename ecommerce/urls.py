from django.conf.urls import url, include
from django.contrib import admin
from accounts.views import index, logout, login
from accounts import urls as urls_accounts

from bugs import urls as urls_bugs
from cart import urls as urls_cart
from search import urls as urls_search
from checkout import urls as urls_checkout
from bugs.views import all_bugs
from home.views import all_index
from accounts.views import index
from django.views import static
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', all_index, name='index'),
    url(r'^accounts/logout/$', logout, name="logout"),
    url(r'^accounts/login/$', login, name="login"),
    url(r'^$', all_bugs, name='bugs'),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^bugs/', include(urls_bugs)),
    url(r'^cart/', include(urls_cart)),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
]
