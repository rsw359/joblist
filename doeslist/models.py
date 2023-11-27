from django.db import models
from django.contrib.auth.models import AbstractUser

class Job(models.Model):
  title = models.CharField(max_length=100)
  customer_name = models.CharField(max_length=100)
  customer_email = models.EmailField(max_length=100, blank=True, null=True)
  created_by = models.ForeignKey('doeslist.Custom_User',on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  completed= models.BooleanField(default=False)
  description = models.TextField(max_length=1000)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.title}-{self.customer_name}"
  
class Custom_User(AbstractUser):
  email = models.EmailField(max_length=100, unique=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.username}-{self.email}"

