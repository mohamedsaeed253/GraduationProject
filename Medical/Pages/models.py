from email.mime import image
from django.db import models
from pkg_resources import require


# Create your models here.
gender_types = [
        ('male','Male'),
        ('female','Female')
    ]
class Engineer(models.Model):
    eng_Id=models.AutoField(primary_key=True, unique=True)
    name= models.CharField(max_length=250, unique=True)
    birthdate= models.DateField(null=True, blank=True)
    gender= models.CharField(max_length=50, choices=gender_types)
    email= models.EmailField(max_length=50, unique=True)
    password= models.CharField(max_length=14, unique=True, null=False)
    phone= models.IntegerField(unique=True)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    doc_Id=models.AutoField(primary_key=True, unique=True)
    name= models.CharField(max_length=250, unique=True)
    birthdate= models.DateField(null=True, blank=True)
    gender= models.CharField(max_length=50, choices=gender_types)
    email= models.EmailField(max_length=50, unique=True)
    password= models.CharField(max_length=14, unique=True)
    phone= models.IntegerField(unique=True)

    def __str__(self):
        return self.name


class Models(models.Model):
    model_Id=models.AutoField(primary_key=True, unique=True)
    model_name= models.CharField(max_length=250, unique=True)
    model_file=models.FileField(upload_to='Files',default='null')
    description= models.TextField()
    preprocessing= models.TextField(unique=True)
    disease= models.ForeignKey('Disease', on_delete=models.PROTECT)
    engID= models.ForeignKey('Engineer', on_delete=models.PROTECT)
    meta_data= models.TextField()

    def __str__(self):
        return self.model_name


class Disease(models.Model):
    disease_Id=models.AutoField(primary_key=True, unique=True)
    disease_name= models.CharField(max_length=250)
    department= models.CharField(max_length=250)

    def __str__(self):
        return self.disease_name


class Doctor_Specialize(models.Model):
    doc_ID=models.ForeignKey('Doctor', on_delete=models.PROTECT)
    disease_ID=models.ForeignKey('Disease', on_delete=models.PROTECT)

    def __str__(self):
        return self.doc_ID

class DataSet(models.Model):
    images=models.FileField(upload_to='dataSet')
    disease_ID=models.ForeignKey('Disease', on_delete=models.PROTECT)

    def __str__(self):
        return str(self.images)

class Login(models.Model): 
    username= models.CharField(max_length=50)
    login_time= models.DateTimeField()

    def __str__(self):
        return self.username

    
class Images(models.Model):
    image = models.FileField(upload_to='Images')

    def __str__(self):
        return str(self.image)

class BioModels(models.Model):
    biomodel_Id=models.AutoField(primary_key=True, unique=True)
    biomodel_name= models.CharField(max_length=250, unique=True)
    biomodel_file=models.FileField(upload_to='BioFiles',default='null')