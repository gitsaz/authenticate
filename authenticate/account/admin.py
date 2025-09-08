from django.contrib import admin

# Register your models here.
from .models import(
    User,
    Message
)

admin.site.register(User)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    search_fields = ("name", "email", "created_at")
    list_filter = ("created_at",)
    
