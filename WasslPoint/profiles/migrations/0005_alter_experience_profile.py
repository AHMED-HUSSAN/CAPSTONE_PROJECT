# Generated by Django 5.2 on 2025-04-24 07:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_personalinformation_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experience', to='profiles.studentprofile'),
        ),
    ]
