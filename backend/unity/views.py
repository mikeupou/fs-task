from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from .models import Subscriber
from .serializers import SubscriberSerializer
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render
from datetime import datetime

import logging

logger = logging.getLogger('django')


# API views
class GetOrCreateSubscriber(APIView, LimitOffsetPagination):
    def get(self, request):
        subscribers = Subscriber.objects.all().order_by('id')
        results = self.paginate_queryset(subscribers, request, view=self)
        serializer = SubscriberSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = SubscriberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Django views
def list_emails(request):
    today = datetime.now()
    current_month = today.month
    subscribers = Subscriber.objects.all().order_by('-id')
    email_list = subscribers.count()
    new_this_month = subscribers.filter(subscribed_at__month=current_month).count()
    unsubscribed = subscribers.filter(is_subscribed=False).count()

    context = {
        'today': today,
        'subscribers': subscribers,
        'email_list': email_list,
        'new_this_month': new_this_month,
        'unsubscribed': unsubscribed
    }

    return render(request, 'unity/list_emails.html', context)

