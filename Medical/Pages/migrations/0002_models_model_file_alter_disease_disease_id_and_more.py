# Generated by Django 4.0.3 on 2022-04-25 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='models',
            name='model_file',
            field=models.FileField(default='null', upload_to='Files'),
        ),
        migrations.AlterField(
            model_name='disease',
            name='disease_Id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='doc_Id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='engineer',
            name='eng_Id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='models',
            name='model_Id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
