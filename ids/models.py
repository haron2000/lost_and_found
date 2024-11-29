from django.db import models

from django.contrib.auth.models import User

class LostFoundID(models.Model):
    STATUS_CHOICES = [
        ('lost', 'Lost'),
        ('found', 'Found'),
    ]

    id_number = models.CharField(max_length=8, unique=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    location = models.CharField(max_length=20)  # Can later integrate GPS coordinates
    description = models.TextField()  # Extra details about where it was found/lost
    date_reported = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # User who found/lost the ID
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=13, null=True, blank=True)  # Adjust max length as needed

    def __str__(self):
        return f"ID: {self.id_number} - {self.status}"
    
    def clean(self):
        from django.core.exceptions import ValidationError
        # Enforce that email and phone number are required if status is 'lost'
        if self.status == 'lost' and (not self.email or not self.phone_number):
            raise ValidationError("Email and phone number are required if the ID is marked as lost.")