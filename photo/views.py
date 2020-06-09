from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.urls import reverse
from .models import images
from datetime import datetime
from django.db.models import F
# create a super user
superuser = User.objects.filter(is_superuser=True)
if superuser.count() == 0:
    superuser=User.objects.create_user("admin","admin@admin","1234")
    superuser.is_superuser = True
    superuser.is_staff = True
    superuser.save()

# Create your views here.
def index(request):
    return render(request, "photo/index.html")

def home(request):
    if not request.user.is_authenticated:
        return render(request, "photo/login.html")
    # image = images.objects.get(userid=request.user).image
    all_entries = images.objects.all()
    # context = {
    #     "user":request.user,
    #     "image_title":all_entries.title,
    #     "description":all_entries.description,
    #     "image":all_entries.picture
    # }
    return render(request, "photo/home.html",{'images':all_entries})

def login_view(request):
    if request.method == "POST":
        username = request.POST["user_name"]
        password = request.POST["password_form"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            # return render(request,"photo/index.html")
            return HttpResponseRedirect(reverse("home"))
            user.is_active = True
        else:
            return render(request,"photo/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))
    # return render(request,"photo/index.html")

def signin(request):
    if request.method == "POST":
        first_name = request.POST["firstname"]
        last_name = request.POST["lastname"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        user =User.objects.create_user(username,email,password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        return render(request, "photo/login.html")
    return render(request, "photo/signin.html")

def uploadImage(request):
    if request.method == "POST":
        image_title = request.POST["image_title"]
        description = request.POST["image_description"]
        image = request.FILES["image_url"]
        myDate = datetime.now()
        formatedDate = myDate.strftime("%Y-%m-%d %H:%M:%S")
        add=images(userid=request.user,title=image_title,description=description,date=formatedDate,picture=image)
        add.save()
        return HttpResponseRedirect(reverse("home"))

    return render(request, "photo/upload.html")


def mygallery(request,user):
    if not request.user.is_authenticated:
        return render(request, "photo/login.html")
    # image = images.objects.get(userid=request.user).image
    all_entries = images.objects.filter(userid=request.user)
    # context = {
    #     "user":request.user,
    #     "image_title":all_entries.title,
    #     "description":all_entries.description,
    #     "image":all_entries.picture
    # }
    return render(request, "photo/mygallery.html",{'images':all_entries})


def viewimage(request,user,id):
    if not request.user.is_authenticated:
        return render(request, "photo/login.html")
    imagefile = images.objects.filter(id=id)
    return render(request, "photo/imageview.html",{'image':imagefile})

def viewimageother(request,user,id):
    if not request.user.is_authenticated:
        return render(request, "photo/login.html")
    imagefile = images.objects.filter(id=id)
    return render(request, "photo/imageview.html",{'image':imagefile})

def deleteImage(request,user,id):
    if not request.user.is_authenticated:
        return render(request, "photo/login.html")
    imagefile = images.objects.get(pk=id).delete()

    # all_entries = images.objects.filter(userid=request.user)
    return HttpResponseRedirect(reverse("home"))

def editimage(request,user,id):
    imagefile = images.objects.filter(id=id)
    return render(request, "photo/editinfo.html", {'image':imagefile})

def updateimage(request,user,id):
    if request.method == "POST":
        image_title = request.POST["image_title"]
        description = request.POST["image_description"]
        images.objects.select_related().filter(id=id).update(title=image_title,description=description)
        imagefile = images.objects.filter(id=id)
        return render(request, "photo/imageview.html",{'image':imagefile})

def voteimage(request, user, id):
    # if votes.objects.filter(userid=request.user,imageid=id).votes_num == 1:
    #     message = "You already voted"
    #     return render(request, "photo/imageview.html",{'image':imagefile},message)
    # image_vote = images.objects.get(imageid=id).image_vote
    review = images.objects.get(pk=id)
    review.votes.up(id)
    imagefile = images.objects.filter(id=id)
    # add=votes(userid=request.user,imageid=id,votes_num=1)
    # add.save()
    # images.objects.filter(id=id).update(image_vote=F("image_vote") + 1)
    return render(request, "photo/imageview.html", {'image':imagefile})
