from django.contrib import admin
from .models import Subscriber


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'is_subscribed', 'subscribed_at']
    fields = ['email', 'is_subscribed', 'subscribed_at']
    list_display_links = ['email']


admin.site.register(Subscriber, SubscriberAdmin)

