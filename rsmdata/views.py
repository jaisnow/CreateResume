# import pdb;pdb.set_trace()
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import (
    RegistrationoForm, LoginForm, CVForm, EducationForm
)

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

from django.contrib import messages


# def index(request):
#   import pdb;pdb.set_trace()
#   return render(request, 'rsmdata/index.html', {})
class HomeView(View):

    def get(self, request, *args, **Kwargs):
        return render(request, 'rsmdata/home.html') 


class Index(View):

    def get(self, request, *args, **Kwargs):
        reg_form = RegistrationoForm()
        return render(request, 'rsmdata/index.html', {'reg_form':reg_form})

    def post(sef, request, *args, **Kwargs):
        reg_form = RegistrationoForm(request.POST)
        email = request.POST.get('email')
        if User.objects.filter(username=email).exists():
            messages.error(request, 'Email address already exists!')
        elif reg_form.is_valid():
            form_obj = reg_form.save(commit=False)
            # first_name = request.POST.get('first_name')
            pwd = request.POST.get('password')
            user = User.objects.create_user(email, email, pwd)
            user.save()
            reg_form.save()
            messages.success(request, 'User successfully Registered!')
            return redirect('rsmdata:login')
        # messages.error(request, 'Incmplete form.')
        return render(request, 'rsmdata/index.html', {'reg_form':reg_form})


class Login(View):

    def get(self, request, *args, **Kwargs):
        # import pdb;pdb.set_trace()
        login_form = LoginForm()
        ctx = {} 
        ctx['form'] = login_form
        return render(request, 'rsmdata/login.html', ctx)

    def post(self, request, *args, **Kwargs):
        # import pdb;pdb.set_trace()
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        login_form = LoginForm(request.POST)
        if user is not None and login_form.is_valid():
            login(request, user)
            # Redirect to a success page.
            return redirect('rsmdata:home')
        else:
            # Return an 'invalid login' error message.
            messages.error(request, 'Wrong credential entered!')
            return render(request, 'rsmdata/login.html', {'form': login_form})


def logout_view(request):
    logout(request)
    return redirect('rsmdata:home')


class Forgetpassword(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'rsmdata/reset-password.html')

    def post(self, request, *args, **kwargs):
        pass


class CreateEmployeeBioView(View):

    def get(self, request, *args, **kwargs):
        # import pdb;pdb.set_trace()
        import random
        edu_id = random.randint(0, 500)
        # if 'education' in request.session:
        #     edu_id = len(request.session['education'])
        # else
        ctx = {
            'form': CVForm(),
            'eduform': EducationForm(),
            'edu_id': edu_id
        }
        return render(request, 'rsmdata/employeeBio.html', ctx)

    def post(self, request, *args, **kwargs):
        # import pdb;pdb.set_trace()
        form_obj = CVForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            messages.success(request, 'Data is successfully submitted!')
            return redirect('rsmdata:home')
        return render(request, 'rsmdata/employeeBio.html', {'form': form_obj})


class EducationView(View):

    def get(sef, request, *args, **kwargs):
        import pdb;pdb,set_trace()
        pass

    def post(self, request, *args, **kwargs):
        # import pdb;pdb.set_trace()
        form = EducationForm(request.POST)
        # if form.is_valid():
        #     education = {
        #             'id': int(request.POST.get('eduction_id')), 
        #             'education' :request.POST.get('education'),
        #             'board' : request.POST.get('board'),
        #             'passing_out_year' : request.POST.get('passing_out_year'),
        #             'university' : request.POST.get('university'),
        #             'course' : request.POST.get('course'),
        #             'specification' : request.POST.get('specification'),
        #             'percent' : request.POST.get('percent')
        #         }
        #     if 'education' in request.session:
        #         request.session['education'].append(education)
        #     else:
        #         request.session['education'] = [education]

        ctx = {
            'form': CVForm(),
            'eduform': EducationForm(),
        }
        return render(request, 'rsmdata/employeeBio.html', ctx)