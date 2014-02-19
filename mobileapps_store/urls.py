from django.conf.urls.defaults import *

urlpatterns = patterns('feedsync.views',
    url(r'^$', view='switchToStoreOrLanding', name='switch_to_store_or_landing'),
)
