import json
from os import getenv

from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RequestSerializer


def send(data):
    mail_info = json.loads(data)
    subject = 'Консультация'
    message = 'Привет.'
    html_message = '<h1>Привет!</h1> <br> ' \
                   '<p>Тебе поступила заявка на консультацию от ' \
                   + mail_info['name'] + '.</p>' \
                   '<p>Комментарий к сообщению от пользователя ' \
                   + mail_info['comment'] + '.</p>' \
                   '<p>Почта: ' \
                   + mail_info['email'] + '.</p>'
    from_email = getenv('EMAIL_HOST_USER')
    recipient_list = [getenv('EMAIL_HOST_USER')]

    try:
        send_mail(subject, message, from_email, recipient_list, html_message=html_message)
        print('sent')
    except Exception as _ex:
        print(_ex)
        return f"{_ex}"


class RequestApiView(APIView):
    def post(self, request):
        send(request.body)
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
