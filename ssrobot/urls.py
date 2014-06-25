from django.conf.urls import patterns, include, url

#from django.contrib import admin
import xadmin
from xadmin.plugins import xversion

from ssrobot.views import post
from msg_board.views import show_msg_board
from checkin.views import show_checkin
#admin.autodiscover()

xadmin.autodiscover()
xversion.register_models()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ssrobot.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(xadmin.site.urls)),
    url(r'^$', post),
    url(r'^board/', show_msg_board),
    url(r'^checkin', show_checkin),
)
