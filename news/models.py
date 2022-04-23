from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=500)
    descriptions = models.TextField()
    price = models.IntegerField()
    duration = models.IntegerField()

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.title

# O'qituvchilar uchun model
class Teacher(models.Model):
    full_name = models.CharField(max_length=255)
    image = models.ImageField(null=True,)
    teaching_course = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.full_name


class Application(models.Model):
    client_name = models.CharField(max_length=200)
    client_last_name = models.CharField('Clint last name', max_length=200, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    client_phone_number = models.CharField(max_length=50)

    def __str__(self):
        return f"Client name: {self.client_name}, Phone nummer: {self.client_phone_number}"
