from django.conf.urls import url
from .views import view_cart, add_to_cart, adjust_cart, del_cart_item, charge

urlpatterns = [
    url(r'^$', view_cart, name='view_cart'),
    url(r'^del/(?P<item_id>.*)$', del_cart_item, name='del_cart_item'),
    url(r'^charge/(?P<total>.*)$', charge, name='charge'),
    url(r'^add/(?P<id>\d+)', add_to_cart, name='add_to_cart'),
    url(r'^adjust/(?P<id>\d+)', adjust_cart, name='adjust_cart'),
]