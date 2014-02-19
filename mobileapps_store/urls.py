from django.conf.urls import patterns, include, url

urlpatterns = patterns('mobileapps_store.views',
    url(r'^$', view='switchToStoreOrLanding', name='switch_to_store_or_landing'),
)
