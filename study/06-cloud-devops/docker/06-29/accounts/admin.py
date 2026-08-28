from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomerUser, Notice


@admin.register(CustomerUser)
class CustomerUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('추가정보', {'fields': ('nickname',)}),
    )
    list_display = ['username', 'email', 'nickname', 'is_staff', 'is_active']


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title', 'content']
    ordering = ['-created_at']
