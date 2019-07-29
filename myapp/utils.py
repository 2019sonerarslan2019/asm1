from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_mail(subject, template_name, context, to):
    html_content = render_to_string(template_name, context)
    text_content = strip_tags(html_content)
    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER,[''])
    msg.attach_alternative(html_content, "text/html")
    msg.send()








