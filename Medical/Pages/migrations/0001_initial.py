# Generated by Django 4.0.3 on 2022-04-24 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('disease_Id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=250)),
                ('department', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('doc_Id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=250)),
                ('birthdate', models.DateTimeField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=50)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=14, unique=True)),
                ('phone', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Engineer',
            fields=[
                ('eng_Id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=250)),
                ('birthdate', models.DateTimeField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=50)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=14, unique=True)),
                ('phone', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Models',
            fields=[
                ('model_Id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('preprocessing', models.TextField(unique=True)),
                ('accuracy', models.DecimalField(decimal_places=2, max_digits=3)),
                ('meta_data', models.TextField()),
                ('disease', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Pages.disease')),
                ('engID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Pages.engineer')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor_Specialize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease_ID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Pages.disease')),
                ('doc_ID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Pages.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='dataSet')),
                ('model_ID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Pages.models')),
            ],
        ),
    ]
