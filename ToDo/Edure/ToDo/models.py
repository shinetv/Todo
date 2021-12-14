from django.db import models

# Create your models here.
class User_reg(models.Model):
    User_name=models.CharField(max_length=300,default='')
    Mail_id=models.CharField(max_length=200,default='')
    gender=models.CharField(max_length=200,default='')
    Password=models.CharField(max_length=300,default='')
    Confirm_password=models.CharField(max_length=300,default='')
    std_type=models.CharField(max_length=300,default='')


class tasks(models.Model):
    task_IDD=models.ForeignKey(User_reg,on_delete=models.CASCADE, blank=True,null=True)
    user_task=models.CharField(max_length=300,default='')
    percentage=models.CharField(max_length=300,default='')
    dates=models.CharField(max_length=200,default='')
