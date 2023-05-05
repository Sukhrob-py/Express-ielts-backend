from django.contrib import admin

# Register your models here.
from .models import MockPaymentModel

admin.site.register(MockPaymentModel)