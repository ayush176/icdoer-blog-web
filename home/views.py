from django.shortcuts import render , HttpResponse , redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from blog.models import Post

# HTML views
def home(request):
    allPost = Post.objects.all()
    context = {'allPost':allPost}
    return render(request, 'home/home.html',context)

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)<3 or len(email)<8 or len(phone)<10 or len(content)<4:
            messages.error(request, 'Please enter information correctly.')
        else:
            contact = Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request, 'Your massage has been recorded successfully')
    return render(request, 'home/contact.html')

def search(request):
    if request.method == 'GET':
        query = request.GET['query']
        if len(query) > 50:
            allPosts = []
        else:
            allPostsTitle = Post.objects.filter(title__icontains=query)
            allPostsContent = Post.objects.filter(content__icontains=query)
            allPosts = allPostsTitle.union(allPostsContent)

        if len(allPosts)==0:
            messages.warning(request, 'No search result found. Please refine your query.')
        return render(request,'home/search.html',{'allPosts':allPosts , 'query':query})

    return render(request, 'home/search.html')

# Authentication APIs
def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        #check for errorneous inputs
        if len(username) > 10:
            messages.error(request,'Username must be less than 10 characters.')
            return redirect('home')    

        if username.isalnum() == False:
            messages.error(request,'Useranme should contain only alphabets and numbers.')
            return redirect('home')

        if pass1!=pass2:
            messages.error(request,'Passwords did not match.')
            return redirect('home')    

        try:
            checkuser = User.objects.get(username=username)
            messages.error(request,'Username already taken.')
            return redirect('home')
        except:    
            #create the user

            myuser = User.objects.create_user(username,email,pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            messages.success(request,'Your iCoder account has been created successfully.')
            return redirect('home')

    else:
        return HttpResponse('404 - NOT FOUND')

def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']

        user = authenticate(username=loginusername,password=loginpass)

        if user is not None:
            login(request,user)
            messages.success(request,'Successfully Logged In')
            return redirect('home')
        
        else:
            messages.error(request,'Invalid credentials. Please try again.')
            return redirect('home')
    else:
        return HttpResponse('404 - NOT FOUND')

def handleLogout(request):
    logout(request)
    messages.success(request,'Successfully Logged Out')
    return redirect('home')