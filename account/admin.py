from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import CustomUserModel




@admin.register(CustomUserModel) #decoratorü ile admin.site.register() olayından kurtulmuş olduk. 
class CustomAdmin(UserAdmin):

    list_display =(
        'username', 'email'
    )
    fieldsets = UserAdmin.fieldsets +  (
        ('Avatar Değiştirme Alanı', {
            'fields' : ['avatar']
        }), 
    )

