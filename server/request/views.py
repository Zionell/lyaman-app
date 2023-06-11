import json
import os

from django.core.mail import send_mail
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Request
from .serializers import RequestSerializer


def send(data):
    mail_info = json.loads(data)
    subject = 'Консультация'
    message = 'Привет.'
    html_message = '<h1>Привет!</h1> <br> ' \
                   '<p>Тебе поступила заявка на консультацию от ' \
                   + mail_info['name'] + '.</p>' \
                   '<p>Комментарий к сообщению от пользователя ' \
                   + mail_info['comment'] + '.</p>'
    from_email = mail_info['email']
    recipient_list = [os.environ.get('EMAIL_HOST_USER')]
    send_mail(subject, message, from_email, recipient_list, html_message=html_message)


class RequestApiView(APIView):
    def post(self, request):
        send(request.body)
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
