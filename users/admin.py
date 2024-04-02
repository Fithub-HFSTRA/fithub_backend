from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser
from .models import Plan, Workout, Workout_Type

class PlanInline(admin.StackedInline):
    model = Plan
    extra = 1

class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'first_name', 'current_workout_plan', 'last_name', 'is_staff', 'age', 'weight', 'get_friends_count']
    inlines = [PlanInline]
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'age', 'gender', 'weight', 'height', 'blood_type', 'wheelchair', 'current_workout_plan')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    def get_friends_count(self, obj):
        return obj.friends_list.count()
    get_friends_count.short_description = 'Friends Count'

@admin.register(Workout_Type)
class WorkoutTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)
    search_fields = ('name',)

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('workout_type', 'workout_days','workout_length','equipment_needed')
    list_filter = ('workout_type',)
    search_fields = ('workout_type__name', 'description')

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'creator', 'difficulty_level')
    list_filter = ('difficulty_level',)
    search_fields = ('name', 'creator__username', 'description')
    filter_horizontal = ('workouts',)
# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)