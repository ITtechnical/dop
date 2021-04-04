from django.urls import path
from shop import views


app_name = 'shop'

urlpatterns = [
    path('dashboard', views.Dashboard, name='dashboard'),
    path('newcustomer', views.Customers, name='newcustomer'),
    path('edit/customer/<str:pk>/', views.EditCustomers, name='editcustomer'),
    path('addmeasurement/<str:pk>/', views.Malemeasurement, name="addmeasurement"),
    path('addmeasurements/<str:pk>/', views.Femalemeasurement, name="addmeasurements"),
    path('customerOrder/<str:pk>/', views.customerOrder, name="customerOrder"),
    path('editorder/<str:pk>/', views.EditOrder, name="editorder"),
    path('customerprofile/<str:pk>/', views.customerord, name="customerprofile"),
    path('allorders', views.allorders, name="allorders"),
    path('createrevenue', views.create_revenue, name="createrevenue"),
    path('editrevenue/<str:pk>/', views.edit_revenue, name="editrevenue"),
    path('createexpenditure', views.create_exdenditure, name="createexpenditure"),
    path('ordersdue', views.orders_due, name="ordersdue"),
    path('delayedorders', views.delayed_orders, name="delayedorders"),
    path('accountreceivable', views.account_receivable, name="accountreceivable"),
    path('totalrevenue', views.allrevenue, name="totalrevenue"),
    path('totalexpense', views.allexpenses, name="totalexpense"),
    path('income&expenditure', views.income_expenditure, name="income&expenditure"),
    path('yearlyincome&expenditure', views.stats_income_expenditure,name="yearlyincome&expenditure"),
    path('montlyincome&expenditure', views.montlystats_income_expenditure,name="montlyincome&expenditure"), 
    path('logout', views.logout_request, name="logout"),
    path('signup', views.signup, name="signup"),
]
