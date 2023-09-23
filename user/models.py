from django.db import models

# Create your models here.
class contact(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email=models.CharField(max_length=120)
    mobile=models.CharField(max_length=20)
    address=models.CharField(max_length=200)
    zip=models.CharField(max_length=10)
    message=models.CharField(max_length=600)


class gallery(models.Model):
    pdes=models.CharField(max_length=205)
    gpic=models.ImageField(upload_to='static/gallery/',default="")
    gdate=models.DateField()

class events(models.Model):
    city=models.CharField(max_length=100)
    etitle=models.CharField(max_length=400)
    epurpose=models.TextField(max_length=2000)
    epic=models.ImageField(upload_to='static/events',default="")
    edate=models.DateField()
    sthanks=models.CharField(max_length=200)

class city(models.Model):
    cityname=models.CharField(max_length=50)
    cdate=models.DateField()

    def __str__(self):
        return self.cityname

class membership(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField()
    gender=models.CharField(max_length=50)
    email=models.EmailField(max_length=60)
    mobile=models.CharField(max_length=60)
    city=models.ForeignKey(city,on_delete=models.CASCADE)
    profession= models.CharField(max_length=100)
    address= models.TextField(max_length=700)
    mdate=models.DateField()

class donate(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.CharField(max_length=15)
    city = models.ForeignKey(city,on_delete=models.CASCADE)
    occupation=models.CharField(max_length=100)
    address = models.TextField(max_length=100)
    amount=models.FloatField()
    ddate=models.DateField()

class notification(models.Model):
    news=models.TextField(max_length=500)
    ndate=models.DateField()

class video(models.Model):
	vtitle=models.CharField(max_length=200)
	vdes=models.TextField(max_length=600)
	thumb=models.ImageField(upload_to='static/thumbnail/',default="")
	vlink=models.CharField(max_length=500)
	vdate=models.DateField()
