from django.conf.urls import patterns, include, url

from django.contrib import admin

from ssrobot.views import post
from msg_board.views import show_msg_board
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ssrobot.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', post),
    url(r'^board/', show_msg_board)
)
