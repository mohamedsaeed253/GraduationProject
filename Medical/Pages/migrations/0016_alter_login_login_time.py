# Generated by Django 4.0.3 on 2022-06-18 12:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0015_alter_login_login_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='login_time',
            field=models.DateTimeField(auto_created=datetime.timezone, auto_now_add=True),
        ),
    ]
