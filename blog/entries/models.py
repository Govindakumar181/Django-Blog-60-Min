from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Entry(models.Model):
    entry_title = models.CharField(max_length=50)
    entrey_text = models.TextField()
    entrey_date = models.DateTimeField(auto_now_add=True)
    entry_author = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        return self.entry_title