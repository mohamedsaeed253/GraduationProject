# Generated by Django 4.0.3 on 2022-06-08 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0007_alter_login_login_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='name',
            field=models.CharField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='engineer',
            name='name',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]