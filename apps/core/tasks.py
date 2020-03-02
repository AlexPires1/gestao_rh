from __future__ import absolute_import, unicode_literals
from celery import shared_task
from apps.funcionarios.models import Funcionario
from django.core.mail import send_mail


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)

@shared_task
def send_relatorio():
    total = Funcionario.objects.all().count()
    send_mail(
        'Relátorio Celery',
        'Relátorio geral de funcionarios %f' % total,
        'alexpirespereira747@gmail.com',
        ['alexpirespereira747@gmail.com'],
        fail_silently=False,
    )
    return True