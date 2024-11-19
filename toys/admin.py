from django.contrib import admin

from toys.models import Toy


class ToyAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "toy_category",
        "release_data",
    ]

# Register your models here.
admin.site.register(Toy)