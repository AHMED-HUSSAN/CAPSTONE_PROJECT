# Generated by Django 5.2 on 2025-05-06 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0034_rename_company_url_companyprofileeditrequest_company_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyprofileeditrequest',
            name='reviewed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
