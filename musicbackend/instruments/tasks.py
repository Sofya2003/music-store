from celery import shared_task
from django.core.mail import send_mail
from django.core.cache import cache


@shared_task
def send_report():
    subject = 'Report'
    message = 'Report about site'
    from_email = 'your_email@example.com'
    recipient_list = ['recipient_email@example.com']
    send_mail(subject, message, from_email, recipient_list, fail_silently=False)


@shared_task
def send_email():
    subject = 'Test email from Celery'
    message = 'This is a test email sent from a Django Celery task.'
    from_email = 'your_email@example.com'
    recipient_list = ['recipient_email@example.com']
    send_mail(subject, message, from_email, recipient_list, fail_silently=False)


@shared_task
def get_cache():
    keys = cache.keys('*')
    print(222222222222, keys)
    for key in keys:
        if key.startswith('visit'):
            cache.get(key).save()
    for key in keys:
        if key.startswith('visit'):
            cache.delete(key)
