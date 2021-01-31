from django.db import models
from django.utils import timezone
# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    mob_no = models.IntegerField()
    balance = models.DecimalField(default=0.0,decimal_places=2,max_digits=10)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class History(models.Model):
    time = models.DateTimeField(auto_now_add=timezone.now())
    amount = models.DecimalField(default=0.0,decimal_places=2,max_digits=10)
    status = models.CharField(max_length=20,default="")
    additional_msg = models.CharField(max_length=200,default="")
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)

    def __str__(self):
        return self.status