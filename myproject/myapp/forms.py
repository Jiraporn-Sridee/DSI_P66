from django.forms import ModelForm
from myapp.models import *
from django import forms
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper



class customerloginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    
    def __init__(self, *args, **kwargs):
        super(customerloginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

class Createtransaction(forms.Form):
    class Meta:
        model = Transaction
        fields = ['image']

class customerregistrationForm(forms.ModelForm):
    GENDER = (('', 'Choose...'), ('M', 'Male'),
              ('F', 'Female'), ('L', 'LGBTQ'))
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First name', 'style':'background-color: #417E77; '}))
    surname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last name', 'style':'background-color: #417E77; '}))
    gender = forms.ChoiceField(choices=GENDER)
    country = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Country', 'style':'background-color: #417E77; '}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone number', 'style':'background-color: #417E77; '}))
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Address', 'style':'background-color: #417E77; '}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email', 'style':'background-color: #417E77; '}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'style':'background-color: #417E77; '}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'style':'background-color: #417E77; '}))

    class Meta:
        model = customer
        fields = ['name', 'surname', 'gender', 'country',
                  'phone', 'address', 'email', 'username', 'password']
    def __init__(self, *args, **kwargs):
        super(customerregistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                "Customer with this useername already exists")

        return username

class ProfileForm(forms.ModelForm):
    GENDER = (('', 'Choose...'), ('M', 'Male'),
              ('F', 'Female'), ('L', 'LGBTQ'))
    name = forms.CharField(widget=forms.TextInput(attrs={'style':'background-color: #417E77; '}))
    surname = forms.CharField(widget=forms.TextInput(attrs={ 'style':'background-color: #417E77; '}))
    gender = forms.ChoiceField(choices=GENDER)
    country = forms.CharField(widget=forms.TextInput(attrs={'style':'background-color: #417E77; '}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'style':'background-color: #417E77; '}))
    address = forms.CharField(widget=forms.TextInput(attrs={'style':'background-color: #417E77; '}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'style':'background-color: #417E77; '}))
    class Meta:
        model = customer
        fields = ['name', 'surname', 'gender', 'country','phone', 'address','email']

class Report_Problem(forms.ModelForm):
    
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'style':'background-color: #417E77; '}))
    problem = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Problem', 'style':'background-color: #417E77; '}))
    product_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Product ID', 'style':'background-color: #417E77; '}))
    info = forms.CharField(widget=forms.TextInput(attrs={'style':'background-color: #417E77; '}))

    class Meta:
        model = Report_issue
        fields = ['email', 'problem', 'product_id' ,'info']

    def __init__(self, *args, **kwargs):
        super(Report_Problem, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False