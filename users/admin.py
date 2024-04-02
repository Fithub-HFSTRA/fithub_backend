from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'first_name', 'last_name', 'is_staff', 'Age', 'Weight', 'get_friends_count']

    def get_friends_count(self, obj):
        return obj.Friends_List.count()
    get_friends_count.short_description = 'Friends Count'

# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)