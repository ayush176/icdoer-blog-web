from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200 ,default="")
    phone = models.CharField(max_length=20 ,default="")
    email = models.CharField(max_length=200 ,default="")
    timeStamp = models.DateTimeField(auto_now_add=True ,blank=True)
    content = models.TextField(max_length=2000 ,default="")

    def __str__(self):
        return 'Message from ' + self.name + ' - ' + self.email
    