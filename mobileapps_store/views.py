"""Views for the mobileapps_store app."""
from django.http import HttpResponseRedirect, HttpResponse
from .models import *

import httpagentparser


def getPlatform(agent):
    """ Version Dump DB """
    mobiles = ['iPhone', 'iPad', 'iPod', 'Android', 'BlackBerry', 'PlayBook',
               'Kindle', 'Opera Mobi', 'Opera Mini', 'Windows Phone', 'Mobile']
    ios = ['iPhone', 'iPad', 'iPod']

    isMobile = False
    platform = 'Unknown'
    version = 'Unknown'
    name = 'Unknown'

    ua = agent

    parsed = httpagentparser.detect(ua)

    if parsed == {}:
        return None

    if parsed.get('browser',) is not None:
        name = parsed['browser']['name']
        version = parsed['browser']['version']

    if parsed.get('os',) is not None:
        platform = parsed['os']['name']

    #search for mobiles
    for i in mobiles:
        if ua.find(i) > 0:
            isMobile = True
            break

    #search for ios devices
    for i in ios:
        if ua.find(i) > 0:
            platform = 'iOS'
            break

    if ua.find('Android') > 0:
        platform = 'Android'
    return platform 
        

def switchToStoreOrLanding(request):
    """
    """
    agent = request.META['HTTP_USER_AGENT']
    platform = getPlatform(agent)
    ma = MobileApp.objects.latest('pk')
    if platform == "iOS":
        target = ma.ios_target #TODO: use fallback if not set
    elif platform == "Android":
        target = ma.android_target  #TODO: use fallback if not set
    else:
        target = ma.landing_target # fallback,  #TODO: what to use as fallback if not set
    return HttpResponseRedirect(target)
    