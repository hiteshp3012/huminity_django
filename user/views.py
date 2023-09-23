from django.shortcuts import render

from .models import*

# Create your views here.
def home(req):
    ndata=notification.objects.all().order_by('-id')[0:4]
    edata = events.objects.all().order_by('-id')[0:1]
    return render(req,'user/index.html',{"d":ndata})

def ourevents(req):
    edata = events.objects.all().order_by('-id')
    return render(req,'user/ourevents.html',{"event":edata})

def memberships(req):
    return render(req,'user/membership.html')

def donatenow(req):
    return render(req,'user/donatenow.html')

def imagegallery(req):
    gdata=gallery.objects.all()
    mydict={"d":gdata}
    return render(req,'user/gallery.html',mydict)


    return render(req,'user/imagegallery.html',mydict)

def aboutus(req):
    return render(req,'user/aboutus.html')

def contactus(request):
     status=False
     if request.method=='POST':
        FirstName =request.POST.get("fname","")
        LastName=request.POST.get("lname","")
        Email=request.POST.get("email","")
        MobileNo=request.POST.get("mobile","")
        Address=request.POST.get("add","")
        Zip=request.POST.get("zip","")
        Message=request.POST.get("msg","")
        x=contact(fname=FirstName,lname=LastName,email=Email,mobile=MobileNo,address=Address,zip=Zip,message=Message)
        x.save()
        status=True

     return render(request,'user/contactus.html',{'s':status})

def login(req):
    return render(req,'user/login.html')

def videogallery(request):
	vdata=video.objects.all().order_by('-id')
	return render(request,'user/videos.html',{'video':vdata})


