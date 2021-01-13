from django.contrib import admin
from .models import CustomUser, Speciality, Post
# Register your models here.

admin.site.register(Post)
admin.site.register(Speciality)
admin.site.register(CustomUser)

