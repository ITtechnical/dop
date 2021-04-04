import django_filters
from django import forms
from django_filters import DateFilter, CharFilter, NumberFilter
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class OrdersFilter(django_filters.FilterSet):
    id = CharFilter(field_name='id', lookup_expr='exact', label='id')
    start_date = DateFilter(field_name="order_date", lookup_expr='gte', label='Start Date',
                            widget=DateInput(
                                attrs={
                                    'class': 'datepicker'
                                }
                            )

                            )

    end_date = DateFilter(field_name="order_date", lookup_expr='lte', label='End Date',
                          widget=DateInput(
                              attrs={
                                  'class': 'datepicker'
                              }
                          )

                          )

    class Meta:
        model = Order
        fields = ['start_date', 'end_date', 'id', 'customer',
                  'order_date', 'status', 'closing_date', 'payments']


class RevenueFilter(django_filters.FilterSet):

    start_date = DateFilter(field_name="created_date", lookup_expr='gte', label='Income Start Date',
                            widget=DateInput(
                                attrs={
                                    'class': 'datepicker'
                                }
                            )

                            )

    end_date = DateFilter(field_name="created_date", lookup_expr='lte', label='Income End Date',
                          widget=DateInput(
                              attrs={
                                  'class': 'datepicker'
                              }
                          )

                          )

    class Meta:
        model = Revenue
        fields = ['start_date', 'end_date', 'id',
                  'account_code', 'amount', 'created_date']

class ExpenditureFilter(django_filters.FilterSet):
    
    start_date = DateFilter(field_name="created_date", lookup_expr='gte', label='Expenditure Start Date',
                            widget=DateInput(
                                attrs={
                                    'class': 'datepicker'
                                }
                            )

                            )

    end_date = DateFilter(field_name="created_date", lookup_expr='lte', label='Expenditure End Date',
                          widget=DateInput(
                              attrs={
                                  'class': 'datepicker'
                              }
                          )

                          )

    class Meta:
        model = Expenditure
        fields = ['start_date', 'end_date', 'id',
                  'account_code', 'amount', 'created_date']
