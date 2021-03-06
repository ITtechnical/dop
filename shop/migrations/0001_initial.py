# Generated by Django 3.1.4 on 2021-04-03 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('date_created', models.DateField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=7)),
                ('accross_back', models.CharField(blank=True, max_length=10, null=True)),
                ('around_arm', models.CharField(blank=True, max_length=10, null=True)),
                ('bust', models.CharField(blank=True, max_length=10, null=True)),
                ('hips', models.CharField(blank=True, max_length=10, null=True)),
                ('waist', models.CharField(blank=True, max_length=10, null=True)),
                ('dress_lenght', models.CharField(blank=True, max_length=10, null=True)),
                ('shoulder_to_under_bust', models.CharField(blank=True, max_length=10, null=True)),
                ('upper_bust', models.CharField(blank=True, max_length=10, null=True)),
                ('under_bust', models.CharField(blank=True, max_length=10, null=True)),
                ('shoulder_to_waist', models.CharField(blank=True, max_length=10, null=True)),
                ('s_n', models.CharField(blank=True, max_length=10, null=True)),
                ('top_or_shirt_length', models.CharField(blank=True, max_length=10, null=True)),
                ('skirt_or_trouser_length', models.CharField(blank=True, max_length=10, null=True)),
                ('half_length', models.CharField(blank=True, max_length=10, null=True)),
                ('chest', models.CharField(blank=True, max_length=10, null=True)),
                ('sleeves', models.CharField(blank=True, max_length=10, null=True)),
                ('thigh', models.CharField(blank=True, max_length=10, null=True)),
                ('bar', models.CharField(blank=True, max_length=10, null=True)),
                ('neck', models.CharField(blank=True, max_length=10, null=True)),
                ('knee', models.CharField(blank=True, max_length=10, null=True)),
                ('calf', models.CharField(blank=True, max_length=10, null=True)),
                ('seat', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Expenditure',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('account_code', models.CharField(choices=[('T&T', 'T&T'), ('Salaries', 'Salaries'), ('Bills', 'Bills')], max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('created_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Revenue',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('account_code', models.CharField(choices=[('Orders', 'Orders'), ('Sales', 'Sales')], default='Sales', max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('orderno', models.CharField(blank=True, max_length=100, null=True)),
                ('created_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('amount_paid', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Closed', 'Closed')], max_length=15)),
                ('order_date', models.DateField(blank=True, null=True)),
                ('payments', models.CharField(choices=[('Part Payment', 'Part Payment'), ('Full Payment', 'Full Paument'), ('No Payment', 'No Payment')], max_length=15)),
                ('closing_date', models.DateField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.customer')),
            ],
        ),
    ]
