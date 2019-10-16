from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.core.mail import EmailMultiAlternatives
from .managers import UserManager
from django.utils.translation import ugettext_lazy as _
from rest_framework.authtoken.models import Token
from django.utils import timezone
from django.conf import settings

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(('email address'), unique=True, error_messages={'unique': 'A user with that email already exists.'})
    first_name = models.CharField(('first name'), max_length=30, blank=True)
    last_name = models.CharField(('last name'), max_length=30, blank=True)
    is_active = models.BooleanField(('active'), default=True)
    password = models.CharField(('password'), max_length=30, blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin site.'),
                                   )
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Register(models.Model):

    emails = models.EmailField(('email address'), unique=True, )

    def save(self):

        email = self.emails
        subject, from_email, to = 'hello', 'Hashroot', email
        text_content = 'Confirmation Link'
        href = 'http://localhost:4200/auth/signup/' + email
        html_content = '<a href=' + href + '>Click here for confirmation</a>'
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        super(Register, self).save()
        return msg


class ExpiringToken(Token):

    class Meta(object):
        proxy = True

    def expired(self):

        now = timezone.now()
        return self.created < now - settings.EXPIRING_TOKEN_LIFESPAN