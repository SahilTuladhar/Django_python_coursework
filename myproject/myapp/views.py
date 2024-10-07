from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User , auth
from django.contrib import messages
from .models import Feature , Posts

# Create your views here.

def index(request):
   
    features = Feature.objects.all()

    return render(request , 'index.html', {'features': features})




def register(request):
  
    if request.method == 'POST':
        Username = request.POST['username']
        Email = request.POST['email']
        Password = request.POST['password']
        Re_password = request.POST['re-password'] 

        if Password == Re_password:
            if User.objects.filter(username = Username).exists():
                messages.info( request , 'Username already exists')
                return redirect('register')
            
            elif User.objects.filter(email = Email).exists():
                messages.info( request , 'Email already exists')
                return redirect('register')
        
            else:

                user = User.objects.create_user(username= Username  , email = Email , password = Password)
                user.save()
                messages.info( request  , 'User created successfully')

                return redirect('login')
        else:
            messages.info( request , 'Password does not match')
            return redirect(register)
    else:
        return render(request , 'register.html')
    
def login(request):
        
    if request.method == "POST":    
        Username = request.POST['username']
        Password = request.POST['password']
        
        user = auth.authenticate(username = Username , password = Password)   # checks whether the Username and password pair exists , if it does it returns the user object else it returns none

        if user is not None:

            auth.login(request , user)  
            return redirect('/')
        
        else: 

            messages.info(request , "User has not been found")
            return redirect('login')
    
    else:
          
        return render(request , 'login.html')
    
def logout(request):

    auth.logout(request)

    return redirect('login')
 
def post(request , val):

    return render(request , 'post.html' ,  {'val' : val})


def counter(request):

    posts = Posts.objects.all()
    return render(request , 'counter.html' , {'posts' : posts})