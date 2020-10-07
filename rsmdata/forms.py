from django import forms
from .models import Registration, Employee, Education

MARITAL_STATUS = (
        ("single", "Single"),
        ("married", "Married"),
    )


class RegistrationoForm(forms.ModelForm):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'First name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last name'
        self.fields['phone_no'].widget.attrs['placeholder'] = 'Phone number'
        self.fields['email'].widget.attrs['placeholder'] = 'Email address'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'

    class Meta:
        model = Registration
        fields = ['first_name', 'last_name', 'phone_no', 'email', 'password']


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Email address'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    # message = forms.CharField(widget=forms.Textarea)


class CVForm(forms.ModelForm):  
    marital_status = forms.ChoiceField(choices=MARITAL_STATUS)
    dob = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y'),
        input_formats=('%d/%m/%Y', )
        )

    class Meta:
        model = Employee
        fields = '__all__'
        # fields = ['full_name','email','phone_no','address','skills','pincode','dob','gender','marital_status']


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        # fields = '__all__'
        exclude = ('employee',)