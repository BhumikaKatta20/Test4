# Generated by Django 2.2.3 on 2020-12-03 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RC_loan', '0006_loan_data_date_of_apply'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan_data',
            name='loan_amount',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='loan_data',
            name='monthly',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='loan_data',
            name='year',
            field=models.CharField(default='', max_length=50),
        ),
    ]