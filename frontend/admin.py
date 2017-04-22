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

    list_editable = ['is_approved']

    actions = ['email_customers']

    def email_customers(self, request, queryset):
        for booking in queryset:
            if booking.is_approved:
                email_body = """Dear {},
        We are pleased to inform you that your booking has been approved.
        Thanks
                """.format(booking.customer_name)
            else:
                email_body = """Dear {},
        Unfortunately we do not have the capacity right now to accept your
        booking.
        Thanks
        """.format(booking.customer_name)

                print(email_body)

    email_customers.short_description = "" \
        "Send email customer with approved or not message"

admin.site.register(Car)
admin.site.register(Booking, BookingModelAdmin)
