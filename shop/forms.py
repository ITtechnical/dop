from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, get_user_model
from .import models
from datetime import date


User = get_user_model()

class DateInput(forms.DateInput):
    input_type = 'date'


class CustomerForm(forms.ModelForm):
    
    class Meta():
        model = models.Customer
        fields = ('first_name', 'last_name','gender', 'location', 'phone')
        
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name...'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name...'}),
            'location': forms.TextInput(attrs={'placeholder': 'Location...'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Mobile Number...'}),
        }
        
        labels ={
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'location': 'Location',
            'phone': 'Mobile No.'
        }
    

class FemaleMeasurementForm(forms.ModelForm):

    class Meta():
        model = models.Customer
        fields = ('accross_back', 'around_arm', 'bust',
                  'hips', 'waist', 'dress_lenght', 'shoulder_to_under_bust', 'upper_bust',
                  'under_bust', 'shoulder_to_waist', 's_n', 'top_or_shirt_length', 'skirt_or_trouser_length', 'half_length', 'sleeves', 'knee', 'thigh', 'seat')

        widgets = {
            'accross_back': forms.TextInput(attrs={'placeholder': 'AB...'}),
            'around_arm': forms.TextInput(attrs={'placeholder': 'Arm...'}),
            'bust': forms.TextInput(attrs={'placeholder': 'Bust...'}),
            'hips': forms.TextInput(attrs={'placeholder': 'Hips...'}),
            'upper_bust': forms.TextInput(attrs={'placeholder': 'Upper bust...'}),
            'under_bust': forms.TextInput(attrs={'placeholder': 'Under bust...'}),
            's_n': forms.TextInput(attrs={'placeholder': 'S-n...'}),
            'waist': forms.TextInput(attrs={'placeholder': 'Waist...'}),
            'dress_lenght': forms.TextInput(attrs={'placeholder': 'Dress Lenght...'}),
            'shoulder_to_under_bust': forms.TextInput(attrs={'placeholder': 'Shoulder To Under Bust...'}),
            'shoulder_to_waist': forms.TextInput(attrs={'placeholder': 'Sleeve To Waist...'}),
            'top_or_shirt_length': forms.TextInput(attrs={'placeholder': 'Blouse...'}),
            'skirt_or_trouser_length': forms.TextInput(attrs={'placeholder': 'Skirt Lenght...'}),
            'half_length': forms.TextInput(attrs={'placeholder': 'Half Lenght...'}),
            'sleeves': forms.TextInput(attrs={'placeholder': 'Sleeves...'}),
            'knee': forms.TextInput(attrs={'placeholder': 'Knee...'}),
            'thigh': forms.TextInput(attrs={'placeholder': 'Thigh...'}),
            'seat': forms.TextInput(attrs={'placeholder': 'Seat...'}),
            
        }

        labels = {
            'accross_back': 'Ab',
            'around_arm': 'Arm',
            'dress_lenght': 'Dress ',
            'shoulder_to_under_bust': 'S-ub',
            'shoulder_to_waist': 'Sleeve To Waist',
            'top_or_shirt_length': 'Blouse',
            'skirt_or_trouser_length': 'Skirt ',
            
        }


class MaleMeasurementForm(forms.ModelForm):
    
    class Meta():
        model = models.Customer
        fields = ('accross_back', 'around_arm',
                  'hips', 'waist', 'top_or_shirt_length', 'skirt_or_trouser_length',
                  'chest', 'sleeves', 'thigh','bar','neck','knee','calf'
                  
                   )

        widgets = {
            'accross_back': forms.TextInput(attrs={'placeholder': 'A b...'}),
            'around_arm': forms.TextInput(attrs={'placeholder': 'Arm...'}),
            'hips': forms.TextInput(attrs={'placeholder': 'Hips...'}),
            'waist': forms.TextInput(attrs={'placeholder': 'Waist...'}),
            'top_or_shirt_length': forms.TextInput(attrs={'placeholder': 'Shirt Lenght...'}),
            'skirt_or_trouser_length': forms.TextInput(attrs={'placeholder': 'Trouser Lenght...'}),
            'chest': forms.TextInput(attrs={'placeholder': 'Chest...'}),
            'sleeves': forms.TextInput(attrs={'placeholder': 'Sleeves...'}),
            'neck': forms.TextInput(attrs={'placeholder': 'Neck...'}),
            'thigh': forms.TextInput(attrs={'placeholder': 'Thigh...'}),
            'bar': forms.TextInput(attrs={'placeholder': 'Bar...'}),
            'knee': forms.TextInput(attrs={'placeholder': 'Knee...'}),
            'calf': forms.TextInput(attrs={'placeholder': 'Calf...'}),
        }

        labels = {
            'accross_back': 'Ab',
            'around_arm': 'Arm',
            'top_or_shirt_length': 'Top to lenght',
            'skirt_or_trouser_length': 'Trouser Length',          
        }


class OrderForm(forms.ModelForm):

    class Meta():
        model = models.Order
        fields = ('price', 'amount_paid', 'balance',
                  'closing_date', 'description')
    
        widgets = {
            'price': forms.TextInput(attrs={'placeholder': 'price...'}),
            'amount_paid': forms.TextInput(attrs={'placeholder': 'Amount Paid...'}),
            'balance': forms.TextInput(attrs={'placeholder': 'Balance...'}),
            'closing_date': DateInput(),
            'description': forms.TextInput(attrs={'placeholder': 'Description'})
        }
        labels = {
            'description': 'Job Description',
            
        }

class EditOrderForm(forms.ModelForm):
    
    class Meta():
        model = models.Order
        fields = ('price', 'amount_paid', 'balance', 'status', 'closing_date', 'description')

        widgets = {
            'price': forms.TextInput(attrs={'placeholder': 'price...'}),
            'amount_paid': forms.TextInput(attrs={'placeholder': 'Amount Paid...'}),
            'balance': forms.TextInput(attrs={'placeholder': 'Balance...'}),
            'closing_date': DateInput(),
            'description': forms.TextInput(attrs={'placeholder': 'Description'})
        }
        labels = {
            'description': 'Job Description',

        }


class ExpenditureForm(forms.ModelForm):

    class Meta():
        model = models.Expenditure
        fields = ('account_code', 'amount')

        widgets = {
            'amount': forms.TextInput(attrs={'placeholder': 'Amount ...'}),
        }
        
        labels = {
            'account_code': 'Accounts Code',
            'amount': 'Amount',
        }


class RevenueForm(forms.ModelForm):
    
    class Meta():
        model = models.Revenue
        fields = ('account_code', 'amount')

        widgets = {
            'amount': forms.TextInput(attrs={'placeholder': 'Amount ...'}),
        }
        
        labels = {
            'account_code': 'Accounts Code  (Orders is not acceptable)',
            'amount': 'Amount',
        }


class UserLoginForm(forms.Form):
    username = forms.CharField(label=False, widget=forms.TextInput(
        attrs={'placeholder': 'Username'}))
    password = forms.CharField(label=False, widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Username or Password incorrect')
            if not user.check_password(password):
                raise forms.ValidationError('Username or Password incorrect')
            if not user.is_active:
                raise forms.ValidationError('Username or Password incorrect')
        return super(UserLoginForm, self).clean(*args, **kwargs)

    class Meta():
        model = models.User
        fields = ('username', 'password')


class CreateUserForm(UserCreationForm):
    username = forms.CharField(label=False, widget=forms.TextInput(
        attrs={'placeholder': 'Username'}))
    first_name = forms.CharField(label=False, widget=forms.TextInput(
        attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(label=False, widget=forms.TextInput(
        attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(label=False, widget=forms.TextInput(
        attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(label=False, widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label=False, widget=forms.PasswordInput(
        attrs={'placeholder': 'Comfirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']

