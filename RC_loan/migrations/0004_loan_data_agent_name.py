# Generated by Django 2.2.3 on 2020-11-30 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RC_loan', '0003_loan_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan_data',
            name='Agent_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
