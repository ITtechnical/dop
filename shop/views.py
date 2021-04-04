from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models.functions import TruncMonth
from django.db.models import Sum
from .forms import *
from .models import *
from .filters import *
from .utils import *
import datetime

# Create your views here.


@login_required
def Dashboard(request):
    today = datetime.datetime.now()
    total = Customer.objects.all().order_by('-id')
    total_customer = total.count()
    total_revenue = Revenue.objects.filter(
        created_date__year=today.year, created_date__month=today.month).aggregate(total_revenue=Sum('amount'))
    total_expenditure = Expenditure.objects.filter(
        created_date__year=today.year, created_date__month=today.month).aggregate(total_expenditure=Sum('amount'))

    if  total_revenue['total_revenue'] and not total_expenditure['total_expenditure']:
        expected_cash = total_revenue['total_revenue']
    elif not total_revenue['total_revenue'] and total_expenditure['total_expenditure']:
        expected_cash = total_expenditure['total_expenditure']
    elif not total_revenue['total_revenue'] and not total_expenditure['total_expenditure']:
        expected_cash = 0.00
    else:
        expected_cash = total_revenue['total_revenue'] - \
            total_expenditure['total_expenditure']

    template = "shop/dashboard.html"
    context = {
        'total': total,
        'total_customer': total_customer,
        'total_revenue': total_revenue,
        'total_expenditure': total_expenditure,
        'expected_cash': expected_cash
    }
    return render(request, template, context)


@login_required
def Customers(request):

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Customer Created Succesfully')
            return redirect('shop:dashboard')

    else:
        form = CustomerForm()
    template = 'shop/customer_form.html'
    context = {'form': form}
    return render(request, template, context)


@login_required
def EditCustomers(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.info(request, 'Customer Saved Succesfully')
            return redirect('shop:dashboard')

    else:
        form = CustomerForm(instance=customer)
    template = 'shop/customer_form.html'
    context = {'form': form}
    return render(request, template, context)


@login_required
def Malemeasurement(request, pk):

    customer = Customer.objects.get(id=pk)
    if request.method == 'POST':
        form = MaleMeasurementForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.info(request, 'Measurement added Succesfully')
            return redirect('shop:dashboard')

    else:
        form = MaleMeasurementForm(instance=customer)
    template = 'shop/malemeasure.html'
    context = {'form': form, 'customer': customer}
    return render(request, template, context)


@login_required
def Femalemeasurement(request, pk):

    customer = Customer.objects.get(id=pk)

    if request.method == 'POST':
        form = FemaleMeasurementForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.info(request, 'Measurement added Succesfully')
            return redirect('shop:dashboard')

    else:
        form = FemaleMeasurementForm(instance=customer)
    template = 'shop/femalemeasure.html'
    context = {'form': form, 'customer': customer}
    return render(request, template, context)


@login_required
def customerOrder(request, pk):

    customers = Customer.objects.get(id=pk)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            orders = form.save(commit=False)
            orders.status = 'Pending'
            orders.customer = customers
            orders.save()
            revid = orders.id
            try:
                rev = Revenue.objects.get(orderno=revid)
                rev.amount = orders.amount_paid
                rev.save()
            except Revenue.DoesNotExist:
                rev = Revenue.objects.create(
                    account_code="Orders", amount=orders.amount_paid, orderno=revid)
            messages.info(request, 'Order Created Succesfully')
            return redirect('shop:dashboard')

    else:
        form = OrderForm(instance=customers)
    template = 'shop/order.html'
    context = {'form': form, 'customer': customers}
    return render(request, template, context)


@login_required
def EditOrder(request, pk):

    order = Order.objects.get(id=pk)
    custid = order.customer.id
    cust = Customer.objects.get(id=custid)

    if request.method == 'POST':
        form = EditOrderForm(request.POST, instance=order)
        if form.is_valid():
            orders = form.save()
            revid = orders.id
            try:
                rev = Revenue.objects.get(orderno=revid)
                rev.amount = orders.amount_paid
                rev.save()
            except Revenue.DoesNotExist:
                rev = Revenue.objects.create(
                    account_code="Orders", amount=orders.amount_paid, orderno=revid)
            messages.info(request, 'Order Saved Succesfully')
            return redirect('shop:customerprofile', custid)

    else:
        form = EditOrderForm(instance=order)
    template = 'shop/editorder.html'
    context = {'form': form, 'cust': cust}
    return render(request, template, context)


@login_required
def customerord(request, pk):
    customer = Customer.objects.get(id=pk)
    totals = Order.objects.filter(customer=pk)

    template = 'shop/customerorders.html'
    context = {'totals': totals, 'customer': customer}
    return render(request, template, context)


@login_required
def allorders(request):
    ord = Order.objects.all().order_by('-id')

    myFilter = OrdersFilter(request.GET, queryset=ord)
    ord = myFilter.qs

    template = 'shop/allorders.html'
    context = {
        'ord': ord,
        'myFilter': myFilter
    }
    return render(request, template, context)


@login_required
def create_revenue(request):

    if request.method == 'POST':
        form = RevenueForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Revenue Created Succesfully')
            return redirect('shop:createrevenue')

    else:
        form = RevenueForm()
    template = 'shop/revenue.html'
    context = {'form': form}
    return render(request, template, context)


@login_required
def edit_revenue(request, pk):
    cc = Revenue.objects.get(id=pk)
    if request.method == 'POST':
        form = RevenueForm(request.POST, instance=cc)
        if form.is_valid():
            form.save()
            messages.info(request, 'Revenue Saved Succesfully')
            return redirect('shop:totalrevenue')

    else:
        form = RevenueForm(instance=cc)
    template = 'shop/revenue.html'
    context = {'form': form}
    return render(request, template, context)


@login_required
def create_exdenditure(request):

    if request.method == 'POST':
        form = ExpenditureForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Expenditure Created Succesfully')
            return redirect('shop:createexpenditure')

    else:
        form = ExpenditureForm()
    template = 'shop/expenses.html'
    context = {'form': form}
    return render(request, template, context)


@login_required
def orders_due(request):
    today = datetime.datetime.now()
    ord = Order.objects.filter(closing_date=today, status="Pending")

    myFilter = OrdersFilter(request.GET, queryset=ord)
    ord = myFilter.qs

    template = 'shop/allorders.html'
    context = {
        'ord': ord,
        'myFilter': myFilter
    }
    return render(request, template, context)


@login_required
def delayed_orders(request):
    today = datetime.datetime.now()
    ord = Order.objects.filter(closing_date__lt=today, status="Pending")

    myFilter = OrdersFilter(request.GET, queryset=ord)
    ord = myFilter.qs

    template = 'shop/allorders.html'
    context = {
        'ord': ord,
        'myFilter': myFilter
    }
    return render(request, template, context)


@login_required
def account_receivable(request):
    today = datetime.datetime.now()
    ord = Order.objects.filter(
        balance__gt=0.00, order_date__year=today.year).order_by('-id')
    total = Order.objects.filter(
        order_date__year=today.year).aggregate(cc=Sum('balance'))

    myFilter = OrdersFilter(request.GET, queryset=ord)
    ord = myFilter.qs
    total = myFilter.qs.aggregate(cc=Sum('balance'))
    template = 'shop/receive.html'
    context = {
        'ord': ord,
        'total': total,
        'myFilter': myFilter
    }
    return render(request, template, context)


@login_required
def allrevenue(request):
    today = datetime.datetime.now()
    ord = Revenue.objects.filter(created_date__year=today.year).order_by('-id')
    total = ord.aggregate(cc=Sum('amount'))

    myFilter = RevenueFilter(request.GET, queryset=ord)
    ord = myFilter.qs
    total = myFilter.qs.aggregate(cc=Sum('amount'))

    template = 'shop/revenueall.html'
    context = {
        'ord': ord,
        'total': total,
        'myFilter': myFilter,
    }
    return render(request, template, context)


@login_required
def allexpenses(request):
    today = datetime.datetime.now()
    ord = Expenditure.objects.filter(
        created_date__year=today.year).order_by('-id')
    total = ord.aggregate(cc=Sum('amount'))

    myFilter = ExpenditureFilter(request.GET, queryset=ord)
    ord = myFilter.qs
    total = myFilter.qs.aggregate(cc=Sum('amount'))

    template = 'shop/expenditureall.html'
    context = {
        'ord': ord,
        'total': total,
        'myFilter': myFilter,
    }
    return render(request, template, context)


@login_required
def income_expenditure(request):
    today = datetime.datetime.now()
    ord = Expenditure.objects.filter(
        created_date__year=today.year).order_by('created_date')
    ords = Revenue.objects.filter(
        created_date__year=today.year).order_by('created_date')
    total = ord.aggregate(expense=Sum('amount'))
    tot = ords.aggregate(cc=Sum('amount'))
    if total['expense'] and tot['cc']:
        bf = tot['cc'] - total['expense']
    elif not total['expense'] and tot['cc']:
        bf = tot['cc']
    elif total['expense'] and not tot['cc']:
        bf = total['expense']
    elif not total['expense'] and not tot['cc']:
        bf = 0.00

    myFilter = ExpenditureFilter(request.GET, queryset=ord)
    myFilter2 = RevenueFilter(request.GET, queryset=ords)
    ord = myFilter.qs
    ords = myFilter2.qs
    total = myFilter.qs.aggregate(expense=Sum('amount'))
    tot = myFilter2.qs.aggregate(cc=Sum('amount'))
    if total['expense'] and tot['cc']:
        bf = tot['cc'] - total['expense']
    elif not total['expense'] and tot['cc']:
        bf = tot['cc']
    elif total['expense'] and not tot['cc']:
        bf = total['expense']
    elif not total['expense'] and not tot['cc']:
        bf = 0.00

    template = 'shop/monthlyincome.html'
    context = {
        'ord': ord,
        'ords': ords,
        'total': total,
        'tot': tot,
        'bf': bf,
        'myFilter': myFilter,
        'myFilter2': myFilter2,
    }
    return render(request, template, context)


@login_required
def stats_income_expenditure(request):
    today = datetime.datetime.now()
    expenses = Expenditure.objects.values('account_code').annotate(
        month=TruncMonth('created_date'), monthly=Sum('amount')).order_by('month')
    income = Revenue.objects.values('account_code').annotate(
        month=TruncMonth('created_date'), monthly=Sum('amount')).order_by('month')
    ord = expenses
    ords = income
    total = Expenditure.objects.aggregate(expense=Sum('amount'))
    tot = Revenue.objects.aggregate(cc=Sum('amount'))
    if total['expense'] and tot['cc']:
        bf = tot['cc'] - total['expense']
    elif not total['expense'] and tot['cc']:
        bf = tot['cc']
    elif total['expense'] and not tot['cc']:
        bf = total['expense']
    elif not total['expense'] and not tot['cc']:
        bf = 0.00

    myFilter = ExpenditureFilter(request.GET, queryset=ord)
    myFilter2 = RevenueFilter(request.GET, queryset=ords)
    ord = myFilter.qs
    ords = myFilter2.qs
    total = ord.aggregate(expense=Sum('amount'))
    tot = ords.aggregate(cc=Sum('amount'))

    if total['expense'] and tot['cc']:
        bf = tot['cc'] - total['expense']
    elif not total['expense'] and tot['cc']:
        bf = tot['cc']
    elif total['expense'] and not tot['cc']:
        bf = total['expense']
    elif not total['expense'] and not tot['cc']:
        bf = 0.00

    template = 'shop/yearly.html'
    context = {
        'ord': ord,
        'ords': ords,
        'total': total,
        'tot': tot,
        'bf': bf,
        'myFilter': myFilter,
        'myFilter2': myFilter2,
    }
    return render(request, template, context)


@login_required
def montlystats_income_expenditure(request):
    today = datetime.datetime.now()
    expenses = Expenditure.objects.values('account_code').annotate(
        month=TruncMonth('created_date'), monthly=Sum('amount')).order_by('month')
    income = Revenue.objects.values('account_code').annotate(
        month=TruncMonth('created_date'), monthly=Sum('amount')).order_by('month')
    ord = expenses.filter(created_date__year=today.year)
    ords = income.filter(created_date__year=today.year)
    total = Expenditure.objects.filter(
        created_date__year=today.year).aggregate(expense=Sum('amount'))
    tot = Revenue.objects.filter(
        created_date__year=today.year).aggregate(cc=Sum('amount'))

    myFilter = ExpenditureFilter(request.GET, queryset=ord)
    myFilter2 = RevenueFilter(request.GET, queryset=ords)
    ord = myFilter.qs
    ords = myFilter2.qs
    total = ord.aggregate(expense=Sum('amount'))
    tot = ords.aggregate(cc=Sum('amount'))

    if total['expense'] and tot['cc']:
        bf = tot['cc'] - total['expense']
    elif not total['expense'] and tot['cc']:
        bf = tot['cc']
    elif total['expense'] and not tot['cc']:
        bf = total['expense']
    elif not total['expense'] and not tot['cc']:
        bf = 0.00

    template = 'shop/yearly.html'
    context = {
        'ord': ord,
        'ords': ords,
        'total': total,
        'tot': tot,
        'bf': bf,
        'myFilter': myFilter,
        'myFilter2': myFilter2,
    }
    return render(request, template, context)


def login_view(request):
    form = UserLoginForm()
    if request.method == 'POST':
        # create an instance the UserLoginForm in the form.py passing in request.Post or None as an argument
        form = UserLoginForm(request.POST)
        if form.is_valid():  # if the data passed to the UserLoginForm in the form.py is passes all the clean data methods
            # get the username form the already clearned data in UserLoginForm class in the form.py and store it into a varible called username
            username = form.cleaned_data.get('username')
            # get the password form the already clearned data in UserLoginForm class in the form.py and store it into a varible called password
            password = form.cleaned_data.get('password')
            # re-authenticate the username and password and store it into variable called user
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('shop:dashboard')

    context = {
        'form': form,  # context is the form itself
    }
    return render(request, 'shop/login.html', context)


@login_required
def logout_request(request):
    logout(request)  # passout the request as an argument to the logout() function
    return redirect("login")  # redirect to the login page

# @unauthenticated_user


def signup(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            user.refresh_from_db()
            return redirect('shop:dashboard')

    template = 'shop/register.html'
    context = {'form': form

               }
    return render(request, template, context)
