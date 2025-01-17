from django import forms
from django.conf import settings

from Simplemooc.core.mail import send_mail_template

from .models import Comment


class ContactCourse(forms.Form):

    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail')
    msg = forms.CharField(
        label='Messagem/Dúvida', widget=forms.Textarea

    )

    def send_mail(self, Course):

        subject = '[%s] Contato' %Course
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'msg': self.cleaned_data['msg'],


        }
        template_name = 'courses/contact_email.html'
        send_mail_template(
            subject,template_name,context,
                  [settings.CONTACT_EMAIL]
                  )
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment']