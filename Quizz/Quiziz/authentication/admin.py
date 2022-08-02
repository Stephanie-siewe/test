from django.contrib import admin

# Register your models here.
from authentication.models import User


class AdminUser(admin.UserAdmin):
    pass
admin.site.register(User,AdminUser)