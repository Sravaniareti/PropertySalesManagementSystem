# Generated by Django 4.2.7 on 2024-02-02 11:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('salesmanagementapp', '0025_postreport'),
    ]

    operations = [
        migrations.AddField(
            model_name='sendenquiry',
            name='sent_enquiry_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]