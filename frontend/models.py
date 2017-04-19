from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models


class Car(models.Model):
    """
    Model for Car. 
    Fields: name, image, description, daily_rent, is_available
    """
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='car_images')
    description = models.TextField()
    daily_rent = models.PositiveIntegerField()

    is_available = models.BooleanField()

    def get_absolute_url(self):
        return reverse('car-details', kwargs={'pk': self.pk})


class Booking(models.Model):
    car = models.ForeignKey(Car)

    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_phone_number = models.CharField(max_length=100)

    booking_start_date = models.DateField()
    booking_end_date = models.DateField()
    booking_message = models.TextField()

    is_approved = models.BooleanField()


