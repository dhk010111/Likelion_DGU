from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Homework(models.Model):
  title = models.CharField(max_length=200)
  writer = models.ForeignKey(User, on_delete=models.CASCADE)
  contents = models.TextField()

class Assignment(models.Model):
  hw_id = models.ForeignKey(Homework, on_delete=models.CASCADE, db_column="hw_id")
  title = models.CharField(max_length=200)
  writer = models.ForeignKey(User, on_delete=models.CASCADE)
  url = models.URLField(max_length=200)
  contents = models.TextField()
  pub_date = models.DateTimeField()