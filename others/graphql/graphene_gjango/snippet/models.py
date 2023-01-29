from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.utils.text import gettext_lazy as _
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Person(models.Model):
    first_name = models.CharField(max_length=20, blank=False, null=False)
    last_name = models.CharField(max_length=20, blank=False, null=False)
    birth_date = models.DateField(null=False, blank=False)
    phone = PhoneNumberField(blank=True)
    email = models.EmailField()
    city = models.CharField(max_length=30)
    post_code = models.IntegerField(validators=[RegexValidator('^[0-9]{6}$', _('Invalid postal code'))], )
    profession = models.CharField(max_length=30)
    about = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def body_preview(self):
        return self.about[:50]
