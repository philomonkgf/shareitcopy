from django.contrib import admin
from .models import Newuser,NewImage
from django.contrib.auth.admin import UserAdmin

# Register your models here.

# class NewuserAdmin(admin.ModelAdmin):
#     list_display = ['username','email','is_active','is_superuser']
#     readonly_fields= ('token','email',)
#     fields = ('email','username','password',)



class NewuserAdmin(UserAdmin):
    list_display = ['username','email','is_active','is_superuser']
    readonly_fields= ('token','date_create','last_login')
    
    fieldsets = (
        (None, {
            "fields": ('email','username','first_name','last_name','bio','is_superuser','is_active','password','date_create','last_login','token',
                
            ),
        }),
    )
    add_fieldsets = (
        (None, {
            "fields": ('email','username','password1','password2','first_name','last_name','bio'
                
            ),
        }),
    )
    


class NewimageAdmin(admin.ModelAdmin):
    list_display = ['name','post','total_likes']
    



  
    
admin.site.register(NewImage,NewimageAdmin)    
admin.site.register(Newuser,NewuserAdmin)