from django.contrib import admin
# from django.contrib.auth import get_user_model
from accounts.models import MyUser as User

# User = get_user_model()

class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "is_active", "activate_code")

admin.site.register(User, UserAdmin)
