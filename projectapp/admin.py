from django.contrib import admin
import projectapp
from projectapp.models import *;

# Register your models here.
admin.site.register(Signup)
admin.site.register(Forgot)
admin.site.register(OTP)
admin.site.register(Update)
admin.site.register(Login)
admin.site.register(Facescan)
admin.site.register(Result)
admin.site.register(History)