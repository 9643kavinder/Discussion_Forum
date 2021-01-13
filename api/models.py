from django.db import models
# Create your models here.


class Speciality(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class CustomUser(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250, unique=True)
    phone = models.CharField(max_length=20, unique=True)
    tag = models.ForeignKey(Speciality, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Post(models.Model):
    message = models.CharField(max_length=300)
    tags = models.ManyToManyField(Speciality)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


