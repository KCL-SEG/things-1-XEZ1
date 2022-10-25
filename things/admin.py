"""
Configuration of the admin interface for things.
"""
from django.contrib import admin
from .models import Thing
from .models import User

@admin.register(Thing)
class UserAdmin(admin.ModelAdmin):
    """
    Configuration of the admin interface for things.
    """

    list_display = [
        'name', 'quantity',
    ]

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Configuration of the admin interface for users."""

    list_display = [
        'username', 'first_name', 'last_name', 'email', 'is_active',
    ]
