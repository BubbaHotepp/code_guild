from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, UserProfile


class ProfileInline(admin.StackedInline):
    model= UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    inlines = (ProfileInline,)
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'get_location')
    list_filter = ('username', 'last_name', 'is_staff', 'is_active')
    list_select_related = ('userprofile',)
    fieldsets = (
        (None, {'fields': ('username', 'password', 'first_name', 'last_name', 'email',)}),
        ('Persmissions', {'fields': ('is_staff', 'is_active')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )
    search_fields = ('username', 'last_name')
    ordering = ('username', 'last_name')

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)
    
    def get_location(self, instance):
        return instance.userprofile.location
    get_location.short_discription = 'Location'


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile)
