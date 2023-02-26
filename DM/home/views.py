from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .models import menteelist,mentee,UserType,mentor
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import logout
# Create your views here.

def home(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')




class Student_Reg(TemplateView):
    template_name = 'signup.html'
    def post(self , request,*args,**kwargs):
        name = request.POST['username']
        email= request.POST['email']
        password= request.POST['password']
        print(email)
        print("--"*100)
        if User.objects.filter(email=email) or menteelist.objects.filter(mentee_name=name):
            print ('pass')
            return render(request,'signup.html',{'message':"already added the username or email"})
       
        else:
            if mentor.objects.filter(mentor_name=name):
                user = User.objects._create_user(username=name,password=password,email=email,first_name=name,is_staff='1',last_name='1')
                user.save()
                teacher=mentor()
                teacher.mentor_name=name
                teacher.mentor_email=email
                teacher.mentor_password=password
                teacher.save()
                return render(request, 'signup.html', {'message':"successfully added"})
            else:
                user = User.objects._create_user(username=name,password=password,email=email,first_name=name,is_staff='0',last_name='2')
                user.save()
                us = menteelist()
                us.mentee_name=name
                us.mentee_email=email
                us.mentee_password=password
                us.save()
                usertype = UserType()
                usertype.user = user
                usertype.type = "student"
                usertype.save()
                return render(request, 'signup.html', {'message':"successfully added"})




class loginview(TemplateView):
    template_name = 'login.html'


    def post(self, request, *args, **kwargs):
       
        
        email = request.POST['email']
        password = request.POST['password']
        name=request.POST['username']
        print(name)

        user = authenticate(username=name, password=password)

        

        if user is not None:
            login(request, user)
            
               
            if user.is_superuser:
                return redirect('/admin')
            elif  user.last_name=='1':
                
                print(user.username)
                students = mentee.objects.filter(mentor_name=user.username)              
                return render(request, 'mentorlog.html',{'students': students})
            elif user.last_name=='2':# User.objects.filter(last_name='2'):
                return render(request, 'menteelog.html') 
                # elif UserType.objects.get(user_id=user.id).type == "user":
                #     return redirect('/user')
                # elif UserType.objects.get(user_id=user.id).type == "public":
                #     return redirect('/public')

            else:
                return render(request, 'login.html', {'message': " User Account Not Authenticated"})


        else:
            return render(request, 'login.html', {'message': "Invalid Username or Password"})



def logout_view(request):
    logout(request)
    return render(request,'login.html')


def profile(request):
    return render(request,'profile.html')

def updateprofile(request):
    def post(self , request,*args,**kwargs):
        name = request.POST['username']
        email= request.POST['email']
        print(name,email)
        print("**"*100)
        dob= request.POST['dob']
        age = request.POST['age']
        bloodgroup= request.POST['bloodgroup']
        religion= request.POST['religion']
        caste = request.POST['caste']
        parish= request.POST['parish']
        address= request.POST['address']
        contactaddress = request.POST['contactaddress']
        contactnumber= request.POST['contactnumber']
        telephone= request.POST['telephone']
        

        if mentee.objects.filter(mentee_name=mentee):
            mt=menteelist()
            mt.mentee_name=name
            mt.mentee_email=email
            mt.mentee_age=age
            mt.mentee_bg=bloodgroup
            mt.mentee_relegion=religion
            mt.mentee_caste=caste
            mt.mentee_parish=parish
            mt.mentee_paddress=address
            mt.mentee_caddress=contactaddress
            mt.mentee_mob=contactnumber
            mt.mentee_tel=telephone

            mt.save()

    

    return render(request,'updateprofile.html')