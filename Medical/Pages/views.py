from asyncio.windows_events import NULL
from datetime import datetime
from email.mime import image
from pyexpat import model
from django.shortcuts import render, redirect
from .models import *
import joblib
from cv2 import resize
import pickle
import torch
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

############################################### User ###############################################
class User():
    @staticmethod
    def signIn(request):
        if request.method == 'POST':
            user_name= str(request.POST.get('Username'))
            password= str(request.POST.get('Password'))
            if user_name == "" and password == "":
                fail_password = "Wrong Password"
                return render(request, 'login.html' , {'pagename': 'Login', 'fail_password': fail_password})
            data =Login(username =user_name, login_time=datetime.today())
            data.save()
            name=Doctor.objects.filter(name=user_name).values()
            namee =Engineer.objects.filter(name=user_name).values()
            y = {'name':'null'}
            z = {'name':'null'}
            for x in name:
                y = x
            
            for x in namee:
                z = x

            if user_name == y['name']:
                if y['password'] == password:
                    return redirect(Ddoctor.doc_home,y['doc_Id'])
                else:
                    fail_password = "Wrong Password"
                    return render(request, 'login.html' , {'pagename': 'Login', 'fail_password': fail_password})

            elif  user_name == z['name']:
                if z['password'] == password:
                    return redirect(Eengineer.eng_home,z['eng_Id'])
                else:
                    fail_password = "Wrong Password"
                    return render(request, 'login.html' , {'pagename': 'Login', 'fail_password': fail_password})

            else:
                fail_password = "Wrong Password"
                return render(request, 'login.html' , {'pagename': 'Login', 'fail_password': fail_password})

        else:
            return render(request, 'login.html' , {'pagename': 'Login'})

    @staticmethod
    def signUp(request):
        if request.method == 'POST':
            user_name= request.POST.get('Username')
            e_mail = request.POST.get('email')
            password= request.POST.get('Password')
            gender= request.POST.get('selected')
            date= request.POST.get('date')
            ch_password= request.POST.get('CheckPassword')
            phone=request.POST.get('phone')
            
            Check_box=request.POST.get('doc_choice')
            Check_box2=request.POST.get('eng_choice')

            if password != ch_password:
                Failed = "*The password and the confirm password is not the same"
                return render(request, 'register.html',{'pagename': 'Register', 'check_fail': Failed})
            
            
            if Check_box == "checked":
                try:
                    checkname = Doctor.objects.get(name=user_name)
                    if checkname != NULL:
                        ch_Failed = "*This username is existed"
                        return render(request, 'register.html',{'pagename': 'Register', 'ch_Failed': ch_Failed})
                except:
                    pass
                try:
                    checkmail = Doctor.objects.get(email=e_mail)
                    if checkmail != NULL:
                        ch_Failed = "*This email is existed"
                        return render(request, 'register.html',{'pagename': 'Register', 'che_Failed': ch_Failed})
                except:
                    pass
                try:
                    checkpass = Doctor.objects.get(password=password)
                    if checkpass != NULL:
                        ch_Failed = "*This password is existed"
                        return render(request, 'register.html',{'pagename': 'Register', 'chp_Failed': ch_Failed})
                except:
                    pass
                data =Doctor(name =user_name ,email= e_mail , password= password , phone=phone, gender=gender, birthdate=date)
                data.save()
                return redirect(User.signIn)

            elif Check_box2 == "checked":
                try:
                    checkname = Engineer.objects.get(name=user_name)
                    if checkname != NULL:
                        ch_Failed = "*This username is existed"
                        return render(request, 'register.html',{'pagename': 'Register', 'ch_Failed': ch_Failed})
                except:
                    pass
                try:
                    checkmail = Engineer.objects.get(email=e_mail)
                    if checkmail != NULL:
                        ch_Failed = "*This email is existed"
                        return render(request, 'register.html',{'pagename': 'Register', 'che_Failed': ch_Failed})
                except:
                    pass
                try:
                    checkpass = Engineer.objects.get(password=password)
                    if checkpass != NULL:
                        ch_Failed = "*This password is existed"
                        return render(request, 'register.html',{'pagename': 'Register', 'chp_Failed': ch_Failed})
                except:
                    pass
                data2 =Engineer(name =user_name ,email= e_mail , password= password , phone=phone, gender=gender, birthdate=date)
                data2.save()
                return redirect(User.signIn)

            else:
                pass   

        return render(request, 'register.html',{'pagename': 'Register'})



############################################### Doctor ###############################################

class Ddoctor():
    @staticmethod
    def doctor(request,id):
        user = Doctor.objects.get(doc_Id=id)
        return render(request, 'doctor.html', {'pagename': 'Doctor' , 'user': user})


    @staticmethod
    def check_up(request,id=None,disease=None):
        if id!=None and disease!=None:
            user = Doctor.objects.get(doc_Id=id)
            models = Models.objects.filter(disease=disease).values()
            if request.method == 'POST':
                model_sel= request.POST.get('model')
                image= request.FILES.get('pic')
                print(disease)
                disease = Disease.objects.get(disease_Id=disease)
                data = DataSet(images=image,disease_ID=disease)
                data.save()
                print(image)
                #iimage=Images.objects.get(id=data.id)
                model = Models.objects.get(model_name=model_sel)
                path = "media/" + str(model.model_file)
                print(path)
                try:
                    predict = TF_model.predict(image,path)
                except:
                    pass
                
                return redirect(Ddoctor.result,user.doc_Id,predict)
            return render(request, 'CheckUp2.html', {'pagename': 'Check Up','models': models , 'user': user})
        else:
            user = Doctor.objects.get(doc_Id=id)
            diseases = Disease.objects.all()
            if request.method == 'POST':
                disease_sel= request.POST.get('disease')
                disease = Disease.objects.get(disease_name=disease_sel)
                return redirect(Ddoctor.check_up,user.doc_Id,disease.disease_Id)
            return render(request, 'CheckUp1.html', {'pagename': 'Check Up','diseases':diseases, 'user': user})


    
    @staticmethod
    def result(request,id,predict):
        user = Doctor.objects.get(doc_Id=id)
        ex_result={'0':'Normal Cell',
                        '1':'Abnormal Cell',
                        '2':'Failed'}
        #result = r_r()
        final_result = ex_result[predict]
        return render(request, 'Result.html', {'pagename': 'Check Up', 'user': user, 'result': final_result})


    @staticmethod
    def Biophase(request, id):
        user = Doctor.objects.get(doc_Id=id)
        if request.method == 'POST':
            image = request.FILES.get('pic')
            data = Images(image = image)
            data.save()
            return redirect(Ddoctor.bioAnalysis,user.doc_Id,image)
        return render(request, 'BioAnalysis.html', {'pagename': 'Image Analysis', 'user': user})


    @staticmethod
    def bioAnalysis(request,id,image):
        user = Doctor.objects.get(doc_Id=id)
        print(image)
        image = "Images/" + image
        print(image)
        image = Images.objects.get(image=image)
        print(image)
        imgpath = "/media/" + str(image)
        if request.method == 'POST':
            model = request.POST.get('model')
            biomodel = BioModels.objects.get(biomodel_name=model)
            modelpath = "media/" + str(biomodel.biomodel_file)
            print(modelpath)
            filter = TF_model.load_from_path(modelpath)
            filter.summary()
            image = reshape(image)
            process_img = filter.predict(image)
            process_img = convert2uint8(process_img)
            return render(request, 'BioAnalysis1.html', {'pagename': 'Image Analysis', 'user': user, 'image':process_img})

        return render(request, 'BioAnalysis1.html', {'pagename': 'Image Analysis', 'user': user, 'image':imgpath})


    @staticmethod
    def doc_home(request,id):
        user = Doctor.objects.get(doc_Id=id)
        return render(request, 'doc_home.html', {'pagename': 'Home', 'user': user})


    @staticmethod
    def doc_profile(request,id):
        user = Doctor.objects.get(doc_Id=id)
        date= str(user.birthdate)
        if request.method == 'POST':
            user_name= request.POST.get('Username')
            e_mail = request.POST.get('email')
            password= request.POST.get('Password')
            gender= request.POST.get('selected')
            date= request.POST.get('date')
            ch_password= request.POST.get('CheckPassword')
            phone=request.POST.get('phone')
            
            if password != ch_password:
                Failed = "The password and the confirm password is not the same"
                return render(request, 'doc_profile.html', {'pagename': 'Edit', 'user': user , 'date' : date , 'check_fail': Failed})

            elif gender == "Gender...":
                Failed = "Enter  your gender, Please."
                return render(request, 'doc_profile.html', {'pagename': 'Edit', 'user': user , 'date' : date , 'check_fail2': Failed})

            else:
                data =Doctor(doc_Id=user.doc_Id , name=user_name ,email= e_mail , password= password , phone=phone, gender=gender, birthdate=date)
                data.save()
                return redirect(Ddoctor.doc_profile,user.doc_Id)

        return render(request, 'doc_profile.html', {'pagename': 'Edit', 'user': user , 'date' : date})



############################################### Engineer ###############################################

class Eengineer():
    @staticmethod
    def upload(request,id):
        user = Engineer.objects.get(eng_Id=id)
        diseases = Disease.objects.all()
        if request.method == 'POST':
            mod_name= request.POST.get('Modelname')
            dis = request.POST.get('selected')
            disease = Disease.objects.get(disease_name=dis)
            mod_file = request.FILES.get('mod_file')
            pre= request.POST.get('preprocessing')
            meta= request.POST.get('meta_data')
            data = Models(model_name= mod_name, model_file= mod_file, preprocessing= pre, disease= disease, engID=user, meta_data= meta)
            data.save()
            return redirect(Eengineer.thanks,user.eng_Id)
        return render(request, 'engineer.html', {'diseases':diseases, 'pagename': 'Engineer', 'user': user})


    @staticmethod
    def thanks(request,id):
        user = Engineer.objects.get(eng_Id=id)
        return render(request, 'thanks.html', {'pagename': 'Thank you', 'user': user})


    @staticmethod
    def dataset(request,id):
        user = Engineer.objects.get(eng_Id=id)
        diseases = Disease.objects.all()
        return render(request, 'dataset.html', {'pagename': 'Data set', 'user': user, 'diseases': diseases})


    @staticmethod
    def imagedata(request,id,disease):
        user = Engineer.objects.get(eng_Id=id)
        sel_disease = Disease.objects.get(disease_name=disease)
        images = DataSet.objects.filter(disease_ID=sel_disease.disease_Id)
        list=[]
        for path in images:
            image = "/media/" + str(path.images)
            list.append(image)
        return render(request, 'imagedata.html', {'pagename': 'Data set', 'user': user, 'images': list})


    @staticmethod
    def eng_profile(request,id):
        user = Engineer.objects.get(eng_Id=id)
        models = Models.objects.filter(engID=user.eng_Id)
        date= str(user.birthdate)
        if request.method == 'POST':
            if request.POST.get('delete'):
                model = Models.objects.get(model_Id = request.POST.get('delete'))
                model.delete()
                return render(request, 'eng_profile.html', {'pagename': 'Edit', 'user': user , 'date' : date , 'models':models})
                
            user_name= request.POST.get('Username')
            e_mail = request.POST.get('email')
            password= request.POST.get('Password')
            gender= request.POST.get('selected')
            date= request.POST.get('date')
            ch_password= request.POST.get('CheckPassword')
            phone=request.POST.get('phone')
            print(gender)
            
            if password != ch_password:
                Failed = "The password and the confirm password is not the same"
                return render(request, 'eng_profile.html', {'pagename': 'Edit', 'user': user , 'date' : date , 'check_fail': Failed})

            elif gender == "Gender...":
                Failed = "Enter  your gender, Please."
                return render(request, 'eng_profile.html', {'pagename': 'Edit', 'user': user , 'date' : date , 'check_fail2': Failed})

            else:
                data =Engineer(eng_Id=user.eng_Id , name =user_name ,email= e_mail , password= password , phone=phone, gender=gender, birthdate=date)
                data.save()
                return redirect(Eengineer.eng_profile,user.eng_Id)
                
        return render(request, 'eng_profile.html', {'pagename': 'Edit', 'user': user , 'date' : date , 'models':models})


    @staticmethod
    def edit_model(request,id,mod):
        user = Engineer.objects.get(eng_Id=id)
        model = Models.objects.get(model_Id=mod)
        Diseases = Disease.objects.all()
        if request.method == 'POST':
            mod_name= request.POST.get('Modelname')
            dis = request.POST.get('selected')
            disease = Disease.objects.get(disease_name=dis)
            mod_file = request.FILES.get('mod_file')
            pre= request.POST.get('preprocessing')
            meta= request.POST.get('meta_data')
            data = Models(model_Id=model.model_Id, model_name= mod_name, model_file= mod_file, preprocessing= pre, disease= disease, engID=user, meta_data= meta)
            data.save()
        return render(request, 'dis_eng_profile.html', {'pagename': 'Profile', 'user': user, 'model': model, 'diseases': Diseases})


    @staticmethod
    def eng_home(request,id):
        user = Engineer.objects.get(eng_Id=id)
        return render(request, 'eng_home.html', {'pagename': 'Home', 'user': user})



############################################### Model ###############################################

class Model():
    def _init_(self,model,model_extension): 
        self.__model = model 
        self.__model_extension = model_extension

    def setmodel(self,modelname,extension):
        self.__model = modelname
        self.__model_extension = extension

    def get_model(self):
        return self.__model

    def get_extension(self):
        return self.__model_extension



############################################### Tensorflow models ###############################################

class TF_model(Model): 
    """extensions tf or HDF5 [".tf",".h5",".HDF5",".Pb"]"""
    @staticmethod 
    def load_from_path(path): 
        model = keras.models.load_model(path)
        model.summary()
        return model


    try:
        @staticmethod
        def predict(image,path):
            image = plt.imread(image)
            imagepro = np.expand_dims(image,axis=0)
            result=str(int(np.round(TF_model.load_from_path(path).predict(imagepro))[0][0]))
            return result
    except:
        pass




############################################### sklearn models ###############################################

class Sklearn_model(Model): 
    """extensions pickle [".pkl"]""" 
    @staticmethod 
    def load_from_path(path): 
        model = pickle.load(open(path, 'rb'))
        return model

    @staticmethod
    def predict(image,path):
        result=Sklearn_model.load_from_path(path).predict(image)
        return result


############################################### Pytorch models ###############################################

class Pytorch_model(Model): 
    """extensions torchscript [".pt" , ".pth" ]"""
    @staticmethod 
    def load_from_path(path): 
        model = torch.load(path)
        return model

    @staticmethod
    def predict(image,path):
        result= Pytorch_model.load_from_path(path).eval(image)
        return result


# Create your views here.
def basehome(request):
    return render(request, 'base_home.html', {'pagename': 'Home'})




def error(request): 
    return render(request, 'error.html',{'pagename': 'Error404'})


def reshape(image): 
    import cv2 
    reshapedimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    return reshapedimage.astype("float32") 
def convert2uint8(image): 
    return image.astype("uint8")