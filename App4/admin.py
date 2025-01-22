from django.contrib import admin
from .models import Signup,Data


@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'rating', 'description', 'image')  # Fields to display in list view
    search_fields = ('name', 'category')  # Add search functionality
    list_filter = ('category', 'rating')  # Add filters for admin interface
    ordering = ('name',)  # Default ordering by name
    fieldsets = (
        (None, {'fields': ('name', 'description', 'image', 'category', 'rating')}),  # Fields to edit
    )


class MemberAdmin(admin.ModelAdmin):
    list_display = ("user", "pasw", "email",)

admin.site.register(Signup, MemberAdmin)