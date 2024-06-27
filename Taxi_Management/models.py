from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    name = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    state = models.CharField(max_length=100)
    USER_TYPES = (
        ('user', 'User'),
        ('driver', 'Driver'),
    )
    type = models.CharField(max_length=6, choices=USER_TYPES)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Add unique related_name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Add unique related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

class LiveLocation(models.Model):
    user = models.ForeignKey(CustomUser, related_name='user_locations', on_delete=models.CASCADE)
    driver = models.ForeignKey(CustomUser, related_name='driver_locations', on_delete=models.CASCADE)
    driver_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    driver_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    user_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    user_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    timestamp = models.DateTimeField(auto_now_add=True)

class Booking(models.Model):
    user_booked = models.ForeignKey(CustomUser, related_name='user_bookings', on_delete=models.CASCADE)
    driver = models.ForeignKey(CustomUser, related_name='driver_bookings', on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
