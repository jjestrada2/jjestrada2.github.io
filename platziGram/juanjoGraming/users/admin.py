from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
#models
from users.models import Profile
from django.contrib.auth.models import User

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=('pk','user','phone_number','website','picture')
    list_display_links=('pk','user')
    list_editable=('phone_number','website','picture')

    search_fields=(
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name'
        'phone_number'
    )

    list_filter=(
        'user__is_active',
        'user__is_staff',
        'created',
        'modified',
    )

    fieldsets=(
        ('Profile',{
            'fields':(('user','picture'),),
        }),
        ('Extrainfo',{
            'fields': (
                ('phone_number'),
                ('biography')                
            )
        }),
        ('Metadata',{
            'fields':(('created','modified'),),
        })
    )
    readonly_fields=('created','modified',)



   
