from django.contrib import admin

# Register your models here.
from .models import Registration, Employee, Education, Certifications


class RegistrationAdmin(admin.ModelAdmin):
	# fields = ('first_name', 'last_name', 'phone_no', 'email', 'password')
	# field is for  detail page
	fieldsets = [
		(None, {'fields': ['first_name', 'last_name', 'phone_no']}),
		('Login info', {'fields': ['email', 'password']})
	]
	list_display = ('first_name', 'last_name', 'phone_no', 'email', 'password')
	list_filter = ['first_name']
	search_fields = ['first_name', 'last_name', 'phone_no', 'email']


class EmployeeAdmin(admin.ModelAdmin):
	list_display = ('full_name','email','phone_no','address','skills','pincode','dob','gender','marital_status')	


class EducationAdmin(admin.ModelAdmin):
	list_display = ('employee','education','board','passing_out_year','university','course','specification','percent')


class CertificationsAdmin(admin.ModelAdmin):
	list_display = ('employee','certification_name','certificatio_body','year')


admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Certifications, CertificationsAdmin)