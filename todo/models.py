from django.db import models

# Create your models here.
class Todo(models.Model):
  title = models.CharField(max_length=120)
  description = models.TextField()
  date_added = models.DateField(null=True)
  completed = models.BooleanField(default=False)

  def __str__(self):
    return self.title