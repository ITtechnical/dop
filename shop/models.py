from django.db import models
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.conf import settings
from django.db.models import Sum
import datetime
from .utils import incrementor

# Create your models here.


class UserSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    session = models.OneToOneField(Session, on_delete=models.CASCADE)

# Create your models here.
class Customer(models.Model):
    gender = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    id = models.CharField(max_length=200, primary_key=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    date_created = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    gender = models.CharField(max_length=7, choices=gender)
    accross_back = models.CharField(max_length=10, null=True, blank=True)
    around_arm = models.CharField(max_length=10, null=True, blank=True)
    bust = models.CharField(max_length=10, null=True, blank=True)
    hips = models.CharField(max_length=10, null=True, blank=True)
    waist = models.CharField(max_length=10, null=True, blank=True)
    dress_lenght = models.CharField(max_length=10, null=True, blank=True)
    shoulder_to_under_bust = models.CharField(max_length=10,null=True, blank=True)
    upper_bust = models.CharField( max_length=10, null=True, blank=True)
    under_bust = models.CharField(max_length=10, null=True, blank=True)
    shoulder_to_waist = models.CharField(max_length=10, null=True, blank=True)
    s_n = models.CharField(max_length=10, null=True, blank=True)
    top_or_shirt_length = models.CharField(max_length=10,null=True, blank=True)
    skirt_or_trouser_length = models.CharField(max_length=10,null=True, blank=True)
    half_length = models.CharField(max_length=10, null=True, blank=True)
    chest = models.CharField(max_length=10, null=True, blank=True)
    sleeves = models.CharField(max_length=10, null=True, blank=True)
    thigh = models.CharField(max_length=10, null=True, blank=True)
    bar = models.CharField(max_length=10, null=True, blank=True)
    neck = models.CharField(max_length=10, null=True, blank=True)
    knee = models.CharField(max_length=10, null=True, blank=True)
    calf = models.CharField(max_length=10, null=True, blank=True)
    seat = models.CharField(max_length=10, null=True, blank=True)
      
    def __str__(self):
        return self.first_name + " " + self.last_name
    
    def save(self, *args, **kwargs):
        
        today = datetime.datetime.now()
        
        if not self.date_created:
            self.date_created = today
            
        if not self.id:
            number = incrementor()
            self.id = "CUS" + str(number())
            while Customer.objects.filter(id=self.id).exists():
                self.id = "CUS" + str(number())
        super(Customer, self).save(*args, **kwargs)
    


class Order(models.Model):
    status = (
        ('Pending', 'Pending'),
        ('Closed', 'Closed'),
    )
    id = models.CharField(max_length=100, primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    description = models.CharField(max_length=10, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=15,choices=status)
    order_date = models.DateField(null=True, blank=True)
    payment = (
        ('Part Payment', 'Part Payment'),
        ('Full Payment', 'Full Paument'),
        ('No Payment', 'No Payment'),
    )
    payments = models.CharField(max_length=15, choices=payment)
    closing_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.id
       
    def save(self, *args, **kwargs):

        today = datetime.datetime.now()

        if not self.order_date:
            self.order_date = today
            
        if self.price == self.amount_paid:
            self.payments = 'Full Payment'
        elif self.amount_paid > 0 and self.amount_paid < self.price:
            self.payments = 'Part Payment'
        else:
            self.payments = 'No Payment'

        if not self.id:
            number = incrementor()
            self.id = "ORD" + str(number())
            while Order.objects.filter(id=self.id).exists():
                self.id = "ORD" + str(number())
        super(Order, self).save(*args, **kwargs)
    
    
    def total(self):
        sum = 0
        today = datetime.datetime.now()
        total_order = Order.objects.filter(balance__gt=0.00, order_date__year=today.year)
        for obj in total_order:
             sum += obj
        return sum
        

class Revenue(models.Model):
    code = (
        ('Orders', 'Orders'),
        ('Sales', 'Sales'),
    )
    id = models.CharField(max_length=100, primary_key=True)
    account_code = models.CharField(max_length=10, choices=code, default='Sales')
    amount = models.DecimalField( max_digits=10, decimal_places=2, default=0.00)
    orderno = models.CharField(max_length=100,null=True, blank=True)
    created_date = models.DateField()
    
    def __str__(self):
        return self.account_code + " " + str(self.amount)
    
    def save(self, *args, **kwargs):
        today = datetime.datetime.now()

        if not self.created_date:
            self.created_date = today
        
        if not self.id:
            number = incrementor()
            self.id = "REV" + str(number())
            while Revenue.objects.filter(id=self.id).exists():
                self.id = "REV" + str(number())
        super(Revenue, self).save(*args, **kwargs)


class Expenditure(models.Model):
    code = (
        ('T&T', 'T&T'),
        ('Salaries', 'Salaries'),
        ('Bills', 'Bills'),
    )
    id = models.CharField(max_length=100, primary_key=True)
    account_code = models.CharField(max_length=10, choices=code)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_date = models.DateField()

    def __str__(self):
        return self.account_code + " " + str(self.amount)

    def save(self, *args, **kwargs):
        today = datetime.datetime.now()

        if not self.created_date:
            self.created_date = today

        if not self.id:
            number = incrementor()
            self.id = "EXP" + str(number())
            while Expenditure.objects.filter(id=self.id).exists():
                self.id = "EXP" + str(number())
        super(Expenditure, self).save(*args, **kwargs)
