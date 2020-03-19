from django.contrib import admin
from .models import User
# Register your models here.

# admin.site.register(User)


class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth')
    fields = ['first_name', 'last_name', ('date_of_birth')]


admin.site.register(User, UserAdmin)
