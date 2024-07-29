from django.core.mail import  send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags, format_html

from django.conf import settings

def send_confirmation_email(email, code):
    activation_url = f'http://127.0.0.1:8000/api/account/activate/?u={code}'
    message = format_html(
        'Здравствуйте, активируйте ваш аккаунт! '
        'Чтобы активировать ваш аккаунт, перейдите по ссылке:'
        '<br>'
        '<a href="{}">{}</a>'
        '<br>'
        'Не передавайте этот код никому!',
        activation_url, activation_url
    )

    send_mail(
        'Здравствуйте, активируйте ваш аккаунт!',
        message,
        'johnsnowtest73@gmail.com',
        [email],
        fail_silently=False,
    )


