# Generated by Django 5.2 on 2025-05-05 10:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0027_remove_companyprofileeditrequest_address_line_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyprofile',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.city'),
        ),
    ]
