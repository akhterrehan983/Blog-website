from django.shortcuts import render, redirect
from .models import User,Post,Liked_post,Comment_post
from django.contrib import messages
from django.http import HttpResponseRedirect 
from django.core.files.storage import FileSystemStorage
# from datetime import datetime
from datetime import date
from django.contrib.sessions.models import Session
# from django.contrib.auth.models import User,auth
x=0
def index(request):
    global x
    x=-5
    lis=  Post.objects.all()
    c=Post.objects.count()
    l=[]
    l.append(lis[0])
    l.append(lis[1])
    l.append(lis[2])
    # x= User.objects.all()
    latest=lis[c-1]
    old=lis[0]
    
    p=lis[c-1]
    p1=lis[c-2]  
    for i in range(0,c): 
        if (lis[i].likes_count > l[0].likes_count): 
            l[2] = l[1] 
            l[1] = l[0] 
            l[0] = lis[i] 
        elif (lis[i].likes_count > l[1].likes_count): 
            l[2] = l[1] 
            l[1] = lis[i] 
        elif (lis[i].likes_count > l[2].likes_count): 
            l[2] = lis[i]
    
    if(request.session.get('is_logged')):
        acc_email=request.session['is_logged']
        user_obj=User.objects.filter(email=acc_email)
        email=request.session.get('is_logged')
        check = Liked_post.objects.filter(liker_email=email,post_id=p.id)
        check1 = Liked_post.objects.filter(liker_email=email,post_id=p1.id)
        # if(request.session.get('page_post')):
        #     del request.session['page_post']
        return render(request,"bs1.html",context={'user_obj':user_obj,'l':l,'p':p,'p1':p1,'check':check,'check1':check1,"latest":latest,"old":old})
    else:
        return render(request,"login.html")

def login(request):
    # if(request.session.has_key('is_logged')):
    #     return redirect('/')
    lis=  Post.objects.all()
    c=Post.objects.count()
    l=[]
    l.append(lis[0])
    l.append(lis[1])
    l.append(lis[2])
    x= User.objects.all()
    p=lis[c-1]
    p1=lis[c-2]  
    for i in range(0,c): 
        if (lis[i].likes_count > l[0].likes_count): 
            l[2] = l[1] 
            l[1] = l[0] 
            l[0] = lis[i] 
        elif (lis[i].likes_count > l[1].likes_count): 
            l[2] = l[1] 
            l[1] = lis[i] 
        elif (lis[i].likes_count > l[2].likes_count): 
            l[2] = lis[i]
    if(request.method=="POST"):
        eml=request.POST.get("Email")
        passw=request.POST.get("Password")

        if User.objects.filter(email=eml).exists() and User.objects.filter(password=passw).exists():
            user_obj = User.objects.filter(email=eml)
            request.session['is_logged'] = eml
            check = Liked_post.objects.filter(liker_email=eml,post_id=p.id)
            check1 = Liked_post.objects.filter(liker_email=eml,post_id=p1.id)
            return render(request,"bs1.html",context={'user_obj':user_obj,'l':l,'p':p,'p1':p1,'eml':eml,'check':check,'check1':check1})
        else:
            messages.warning(request,'Invalid email or Password')
            return HttpResponseRedirect('login') 
    else:
        return render(request,"login.html")

def register(request):
    if(request.method=="POST"):
        address = request.POST.get("Address")
        f_name = request.POST.get("FirstName")
        l_name= request.POST.get("LastName")
        email = request.POST.get("Email")
        password=request.POST.get("Password")
        cpassword=request.POST.get("confirm Password")
        phone_no = request.POST.get("Telephone")
        gender   = request.POST.get("Gender")
        
        
        if User.objects.filter(email=email).exists():
            messages.info(request,'User Already Exists with this Email')
            return HttpResponseRedirect('register')
        else:
            if password==cpassword:
                user = User(address=address, first_name=f_name,last_name=l_name,email=email,password=password,phone_no=phone_no,gender=gender)
                user.save()
                messages.info(request,'User Created')
                return HttpResponseRedirect('login')
            else:
                messages.info(request,'Password Does not Match')
                return HttpResponseRedirect('register')           
    return render(request,"register.html")

def posts(request):
    if(request.method=="POST" and request.FILES['myfile']):
        heading = request.POST.get("heading")
        desc    = request.POST.get("desc")
        myfile   = request.FILES['myfile']
        fs = FileSystemStorage()
        filename= fs.save(myfile.name, myfile)
        url=fs.url(filename)
        acc_email=request.session['is_logged']
        post = Post(blog_heading=heading,description=desc,post_pic=url,email=acc_email)
        post.save()
        # post_id = Post.objects.values('id').filter(email=acc_email,post_pic=url)[0]['id']
        # l_post = Liked_post(liker_email=acc_email,post_id=post_id,is_liked=False)
        # l_post.save()
        # user_obj=User.objects.filter(email=acc_email)
        return redirect('/')
    

def logout(request):
    try:
        del request.session['is_logged']
        del request.session['page_post']
        return render(request,"login.html")
    except KeyError:
        return render(request,"register.html")

def likecomment(request):

            
    # c=Post.objects.filter(blog_heading="What Happens in a Black Hole?")
    # f="likes_count"
    # c = Post.objects.first()
    # field_value = getattr(c,f)
    
    email=request.session['is_logged']
    post_id= request.GET.get('post_id')
    post_obj= Post.objects.filter(id=post_id)
    if(Liked_post.objects.filter(liker_email=email,post_id=post_id,is_liked=False).exists()):
        Liked_post.objects.filter(liker_email=email,post_id=post_id).update(is_liked=True)
        val= Post.objects.values('likes_count').filter(id=post_id)[0]['likes_count']
        Post.objects.filter(id=post_id).update(likes_count=val+1)

    elif(Liked_post.objects.filter(liker_email=email,post_id=post_id,is_liked=True).exists()):
        val= Post.objects.values('likes_count').filter(id=post_id)[0]['likes_count']
        Post.objects.filter(id=post_id).update(likes_count=val-1)
        Liked_post.objects.filter(liker_email=email,post_id=post_id).update(is_liked=False)
        
    else:
        liked_post=Liked_post(liker_email=email,post_id=post_id,is_liked=True)
        liked_post.save()
        val= Post.objects.values('likes_count').filter(id=post_id)[0]['likes_count']
        Post.objects.filter(id=post_id).update(likes_count=val+1)
    

  
    # return redirect("/see_post")    # else:
    return redirect("/")
    

    
def see_post(request):
    email=request.session['is_logged']   
    post_id= request.GET.get('post_id')
    l=Comment_post.objects.filter(post_id=post_id)
   
    check1=None    
    # post_obj= Post.objects.filter(id=post_id)
    request.session["page_post"]=post_id
    if(request.method=="POST"):
        post_id=request.POST.get("post_id")
        if(Liked_post.objects.filter(liker_email=email,post_id=post_id,is_liked=False).exists()):
            Liked_post.objects.filter(liker_email=email,post_id=post_id).update(is_liked=True)
            val= Post.objects.values('likes_count').filter(id=post_id)[0]['likes_count']
            Post.objects.filter(id=post_id).update(likes_count=val+1)

        elif(Liked_post.objects.filter(liker_email=email,post_id=post_id,is_liked=True).exists()):
            val= Post.objects.values('likes_count').filter(id=post_id)[0]['likes_count']
            Post.objects.filter(id=post_id).update(likes_count=val-1)
            Liked_post.objects.filter(liker_email=email,post_id=post_id).update(is_liked=False)
            
        else:
            liked_post=Liked_post(liker_email=email,post_id=post_id,is_liked=True)
            liked_post.save()
            val= Post.objects.values('likes_count').filter(id=post_id)[0]['likes_count']
            Post.objects.filter(id=post_id).update(likes_count=val+1) 
    # if(request.session.get("page_post")):
    #     post_obj= Post.objects.filter(id=post_id)
    #     # check1= Liked_post.objects.values('is_liked').filter(id=post_id,liker_email=email)
    #     return render(request,"post.html",{'post_obj':post_obj,"check1":check1,"l":l})
    # else:
    #     request.session["page_post"]=post_id
    post_obj= Post.objects.filter(id=post_id)
    
    check1= Liked_post.objects.values('is_liked').filter(id=post_id,liker_email=email)
    return render(request,"post.html",{'post_obj':post_obj,"check1":check1,"l":l})






def post_list(request):
    global x
    posts=Post.objects.all()
    if(request.GET.get("more_posts")=="1"):
        count=Post.objects.count()
        inc=count%5
        x+=inc
        return render(request,"mpost.html",{"multi_post":posts})
       

    if(request.method=="POST"):
        x+=5
        # global post_list
        posts=Post.objects.all()
        count=Post.objects.count()
        multi_post=[]
        if(x<count):
            c=count-x
            for i in range(x,x+5):
                try:
                    multi_post.append(posts[i])
                except IndexError:
                    pass
                # temp.append(multi_post[i])
            return render(request,"mpost.html",{"multi_post":multi_post})    
        else:
            x-=5
            messages.info(request,'No post available')
            return HttpResponseRedirect('post_list')
    
    return render(request,"mpost.html",{"multi_post":posts})
    
def blog_comment(request):
    email=request.session["is_logged"]
    if(request.method=="POST"):
        comment=request.POST.get("comment")
        post_id=request.POST.get("post_id")
        c_obj=Comment_post(commenter_email=email,post_id=post_id,comment=comment)
        c_obj.save()
    # l=Comment_post.objects.filter(id=post_id)
    post_obj= Post.objects.filter(id=post_id)
    check1= Liked_post.objects.values('is_liked').filter(id=post_id,liker_email=email)
    # if(request.session.get(["page_post")):
    idd=request.session['page_post']
    l=Comment_post.objects.filter(post_id=idd)
    return render(request,"post.html",{'l':l,"post_obj":post_obj,"check1":check1})
            
