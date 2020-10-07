from django.urls import path
from django.urls import path, include

from .views import (
	Index, Login, HomeView, logout_view, Forgetpassword, 
	CreateEmployeeBioView, EducationView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('accounts/register/', Index.as_view(), name='register'),
    path('accounts/login/', Login.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('forget-password/', Forgetpassword.as_view(), name='forget_pwd'),
    path('employee-bio/', CreateEmployeeBioView.as_view(), name='employee_bio'),
    path('education/', EducationView.as_view(), name='education'),

    #auth usr forget password
    path('accounts/', include('django.contrib.auth.urls')),
	# path('accounts/signup', signup , name = 'signup'),
]