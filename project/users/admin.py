from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Order
from django.conf import settings

admin.site.site_header = settings.ADMIN_SITE_HEADER
admin.site.site_title = settings.ADMIN_SITE_TITLE
admin.site.index_title = settings.ADMIN_INDEX_TITLE


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('id_key',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('id_key',)}),
    )

    def get_queryset(self, request):
        return CustomUser.objects.all()
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'offer_name', 'id')