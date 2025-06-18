from django.contrib import admin
from .models import MyUser



admin.site.register(MyUser)
list_display = ('name' , 'email' , 'password' , 'match_password')

# Register your models here.
