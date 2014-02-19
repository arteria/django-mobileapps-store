from django.db import models
from django.utils.translation import ugettext_lazy as _
 
class MobileApp(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True, help_text="Name of the app.")
    android_target = models.URLField(null=True, blank=True)
    ios_target = models.URLField(null=True, blank=True)
    landing_target = models.URLField(help_text="Fallback landing webpage", blank=True, null=True)
    
    