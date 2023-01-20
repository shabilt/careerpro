from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account


class AccountAdmin(UserAdmin):
    list_display = ('pk','phone','date_joined', 'last_login','role','email', 'is_admin','is_active')
    search_fields = ('pk','phone',)
    readonly_fields=('pk', 'date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ('pk',)


admin.site.register(Account, AccountAdmin)