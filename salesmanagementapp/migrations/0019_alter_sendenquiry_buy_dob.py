# Generated by Django 4.2.7 on 2024-02-01 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesmanagementapp', '0018_alter_sendenquiry_buy_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendenquiry',
            name='buy_dob',
            field=models.DateField(null=True),
        ),
    ]
