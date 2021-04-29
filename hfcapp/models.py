from django.db import models

# Create your models here.
class Transformationimg(models.Model):
    image = models.ImageField(upload_to="transformation\img")

class gellaryimg(models.Model):
    image = models.ImageField(upload_to="gellary\img")

class Resultsimg(models.Model):
    image = models.ImageField(upload_to="result\img")

class Rewardsimg(models.Model):
    image = models.ImageField(upload_to="reward\img")    


class Packages(models.Model):
    Packages_id = models.AutoField
    month = models.IntegerField()
    singlePrice = models.IntegerField(default=0)
    couplePrice = models.IntegerField(default=0)
    facility1 = models.CharField(max_length=200)
    facility2 = models.CharField(max_length=200)
    facility3 = models.CharField(max_length=200,default=0)
    facility4 = models.CharField(max_length=200,default=0)
    facility5 = models.CharField(max_length=200,default=0)

#========================== more packages =================
class morePackages(models.Model):
    Packages_id = models.AutoField
    days = models.CharField(max_length=200,default=0)
    packagetitile = models.CharField(max_length=200,default=0)
    singlePrice = models.IntegerField(default=0)
    couplePrice = models.IntegerField(default=0)
    facility1 = models.CharField(max_length=200)
    facility2 = models.CharField(max_length=200)
    facility3 = models.CharField(max_length=200,default=0)
    facility4 = models.CharField(max_length=200,default=0)
    facility5 = models.CharField(max_length=200,default=0)
#================================Ordersss Details =================================================================
class Orders(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100,default=0)
    phone = models.IntegerField(default=0)
    montha = models.IntegerField(default=0)
    singlePricea = models.IntegerField(default=0)
    couplePricea = models.IntegerField(default=0)
    select = models.CharField(max_length=200,default=0)

    def __str__(self):
        return self.name
