from django.template.loader import render_to_string
from django.template.defaultfilters import striptags
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

def send_mail_template(subject,template_name,context,recipient_list,
                       from_email=settings.DEFAULT_FROM_EMAIL, fail_silently=False):
    msg_html = render_to_string(template_name, context)

    msg_txt = striptags(msg_html)

    email = EmailMultiAlternatives(
        subject=subject, body= msg_txt,
        from_email=from_email, to=recipient_list

    )
    email.attach_alternative(msg_html, "text/html")
    email.send(fail_silently=fail_silently)
