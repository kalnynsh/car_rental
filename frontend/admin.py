from django.contrib import admin
from frontend.models import Car
from frontend.models import Booking


class BookingModelAdmin(admin.ModelAdmin):
    list_display = [
        'customer_name',
        'booking_start_date',
        'booking_end_date',
        'is_approved',
    ]

    list_filter = ['is_approved']

    search_fields = ['customer_name']


admin.site.register(Car)
admin.site.register(Booking, BookingModelAdmin)
