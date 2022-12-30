from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from projectapp.models import *;
from django.contrib import messages
from pymongo import *;
import smtplib
import random
from tensorflow import keras
from keras.preprocessing import image
import cv2
import numpy as np
from projectapp.form import *;
from django.core.files.storage import FileSystemStorage
import imghdr
from email.message import EmailMessage

special_char='[@_!$%^&*()<>?/\|}{~:]#'
client = MongoClient("mongodb://localhost:27017/")
db = client["project"]
col = db["projectapp_signup"]
otp1 = random.randint(100000, 999999)
otp1 = str(otp1)


model = keras.models.load_model("D:/project/project/projectapp/beprojectmodel/beproject.h5")

def login(request):
   if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
       
        a=col.find({"username":username,"password":password})
        b=""
        for x in a:
            b=x
        if len(b)!=0:
            return redirect("http://127.0.0.1:8000/facescan")
        
        else:
            messages.error(request,"Incorrect Username or Password")
            return render(request,"landingpage.html")
   return render(request,"landingpage.html")
def signup(request):
    if request.method=="POST":
        firstname=request.POST.get("firstname")
        lastname=request.POST.get("lastname")
        username=request.POST.get("username")
        password=request.POST.get("password")
        confirmpassword=request.POST.get("confirmpassword")
        mailbox=request.POST.get("mailbox")
       
        ans=col.find({"username":username}).count()>0
        if ans==True:
        
            messages.error(request,"Username already taken")
        elif firstname.isalpha()==False:
            messages.error(request,"Firstname should only contain alphabets")
        elif lastname.isalpha()==False:
            messages.error(request,"Lastname should only contain alphabets")
        elif '@' not in mailbox:
            messages.error(request,"Invalid Email")
        elif any(x.isalpha() for x in password)==False or any(x.isnumeric() for x in password)==False or any(x in special_char for x in password) == False:
            messages.error(request,"Password should be alphanumeric")
        elif password==username:
            messages.error(request,"Username and Password cannot be same")
        elif confirmpassword!=password:
            messages.error(request,"Confirmpassword and Password should match")
        else:
               
            mysignup=Signup(firstname=firstname,lastname=lastname,username=username,password=password,mailbox=mailbox)
            mysignup.save() 
            messages.success(request,"Registration done") 
           
           
    return render(request,"signup.html")

  

def forgot(request):
    if request.method=="POST":
        username=request.POST.get("username")
        mailbox=request.POST.get("mailbox")
        userans=col.find({"username":username,"mailbox":mailbox}).count()>0
        if userans==False:
            messages.error(request,"Invalid credentials")
        else:
            s=smtplib.SMTP("smtp.gmail.com" , 587) 
            s.starttls()
            s.login("skinalyze123@gmail.com" , "nbnzzhjjmeytuypk")
            
            s.sendmail("skinalyze123@gmail.com" , mailbox , "Your OTP is "+otp1)
            s.quit()
            return redirect("http://127.0.0.1:8000/otp")
            
    return render(request,"forgot.html")


def otp(request):
   
    if request.method=="POST":
        otp=request.POST.get("otp")
        if otp!=otp1:
          
            messages.error(request,"Invalid OTP")
        

        else:
            return redirect("http://127.0.0.1:8000/update")
            

    return render(request,"otp.html") 


def update(request):
    
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        confirmpassword=request.POST.get("confirmpassword")
        userans=col.find({"username":username}).count()>0
        if userans!=True:
            messages.error(request,"Invalid Username")
        elif any(x.isalpha() for x in password)==False or any(x.isnumeric() for x in password)==False or any(x in special_char for x in password) == False:
            messages.error(request,"Password should be alphanumeric")
        elif confirmpassword!=password:
            messages.error(request,"Confirmpassword and Password should match")
        elif username==password:
            messages.error(request,"Username and Password cannot be same")
        else:
            col.update_one({"username":username},{"$set":{"password":password}})
            return redirect("http://127.0.0.1:8000/")
            
    return render(request,"update.html")

def facescan(request):
    form=""
    username=""
    if request.method=="POST":
        form=ImageForm(request.POST,request.FILES)
        username=request.POST.get("username")
        
        
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/facescan')
        else:
            form = ImageForm()
                 
     
    return render(request, 'facescan.html',{'form':form})

def result(request):
    if request.method=="POST":
        username=request.POST.get("username")
  
    return render(request,"result.html")

def result_wrinkles(request):
    return render(request,"result_wrinkles.html")
def result_puffyeyes(request):
    return render(request,'result_puffyeyes.html')
def result_darkspots(request):
    return render(request,'result_darkspots.html')
def finalresult(request):
        context={}
        username=request.POST.get("username")
        context['username']=username
        collection=db['projectapp_facescan']
        ans=collection.find({"username":username})
       
        if ans==False:
            messages.error(request,"Invalid Username")
           
        else:
            path=r"D:/project/project/media/"
            collection=db['projectapp_facescan']
            ans=collection.find({"username":username})
            list1=[]
            
            for x in ans:
                
                list1.append(x['id'])
            
            b=max(list1)
            ans2=collection.find({'id':b})
            for y in ans2:
                z=y['image']
            
                        
            img_path=path+z
           
            img=cv2.imread(img_path)
            print(img)
            img=cv2.resize(img,(200,200))
            print(img)
            x = image.img_to_array(img)
       
            x = x.reshape((1,) + x.shape)
            x /= 255.
            
            result=model.predict([x])
            data={
                1:"dark spots",
                0:"puffy eyes",
                2:"wrinkles",
            }
          
            fresult = data[np.argmax(result, axis=1)[0]]
            predicted_probability = result[0][np.argmax(result, axis=1)[0]]  
            if fresult=="wrinkles":
                return redirect("http://127.0.0.1:8000/result_wrinkles")
            if fresult=="puffy eyes":
                return redirect("http://127.0.0.1:8000/result_puffyeyes")
            if fresult=="dark spots":
                return redirect("http://127.0.0.1:8000/result_darkspots")
        return render(request,"finalresult.html")

def history(request):
    if request.method=="POST":
        mailbox=request.POST.get("mailbox")
        username=request.POST.get("username")
        path=r"D:/project/project/media/"
        a=col.find({"username":username}).count()>0
        if '@' not in mailbox:
            messages.error(request,"Invalid Email")
      
        elif a==False:
            messages.error(request,"Invalid Username")
        else:
            collection=db['projectapp_facescan']
            ans=collection.find({"username":username})
            list1=[]
            for x in ans:
                list1.append(path+x['image'])
            Sender_Email = "skinalyze123@gmail.com"
            Reciever_Email = mailbox
            Password ="nbnzzhjjmeytuypk"

            newMessage = EmailMessage()                         
            newMessage['Subject'] = "History" 
            newMessage['From'] = Sender_Email                   
            newMessage['To'] = Reciever_Email                   
            newMessage.set_content('See the Attachments Please') 
            for file in list1:

                with open(file, 'rb') as f:
                    image_data = f.read()
                    image_type = imghdr.what(f.name)
                    image_name = f.name

                newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                
                smtp.login(Sender_Email, Password)              
                smtp.send_message(newMessage)
           
    return render(request,"History.html")

def know_darkspots(request):
    return render(request,'know_more_darkspots.html')

def know_puffyeyes(request):
    return render(request,'know_more_puffyeyes.html')

def know_wrinkles(request):
    return render(request,'know_more_wrinkles.html')