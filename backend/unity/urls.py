from django.urls import path
from .views import GetOrCreateSubscriber, list_emails

urlpatterns = [
    # v1 API endpoints
    path('api/v1/leads/', GetOrCreateSubscriber.as_view()),

    # regular views
    path('list-emails/', list_emails, name='list-emails'),
]