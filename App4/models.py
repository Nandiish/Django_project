from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# A simple User model to store the sign-up information

class Signup(models.Model):
    user = models.CharField(max_length=150, unique=True)
    pasw = models.CharField(max_length=128)  # For hashed passwords
    email = models.EmailField(unique=True)  # Ensure the email is unique


    def __str__(self):
        return self.user

CATEGORY_CHOICES = [
    ('beach', 'Beach'),
    ('mountain', 'Mountain'),
    ('city', 'City'),
    ('desert', 'Desert'),
    ('forest', 'Forest'),
    # Add other categories as needed
]


class Data(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='destinations/')
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='beach')

    def __str__(self):
        return self.name