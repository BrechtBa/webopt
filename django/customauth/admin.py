from django.contrib import admin


from .models import User

class UserAdmin(admin.ModelAdmin):
	list_display = ('email', 'first_name', 'last_name', 'is_active', 'date_joined', 'is_staff')
	ordering = ('date_joined',)
	fieldsets = [
		('User',       		{'fields': ['email','first_name','last_name','date_joined','is_active','last_login']}),
		('Permissions', 	{'fields': ['is_superuser','is_staff','user_permissions','groups']}),
	]
admin.site.register(User, UserAdmin)