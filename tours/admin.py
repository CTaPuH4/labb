from django.contrib import admin

from .models import Location, Tour


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'price',
        'location',
        'is_published',
    )
    list_editable = (
        'title',
        'price',
        'location',
        'is_published',
    )


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'country',
        'name',
        'is_published',
    )
    list_editable = (
        'country',
        'name',
        'is_published',
    )
