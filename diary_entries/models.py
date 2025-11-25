from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DiaryEntry(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='diary_entries')
    location = models.CharField(max_length=200)
    pain_level = models.IntegerField()
    mood = models.CharField(max_length=100)
    sleep_hours = models.FloatField()
    triggers = models.TextField(blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content[:50]  # Return the first 50 characters of the content
    

# class ContactMessage(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     subject = models.CharField(max_length=200)
#     message = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ['-created_at']

#     def __str__(self):
#         return f"{self.subject} from {self.name}"