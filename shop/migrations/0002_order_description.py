# Generated by Django 3.1.4 on 2021-04-03 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='description',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
