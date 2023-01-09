from django.db import models

# Create your models here.
class Todo_list(models.Model):
    added_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title