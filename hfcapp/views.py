from django.shortcuts import render,HttpResponse
from .models import Transformationimg,gellaryimg,Packages,Orders
from .models import Resultsimg,Rewardsimg,morePackages
from math import ceil
# Create your views here.
def index(request):
    packege = Packages.objects.all()
    gellarys = gellaryimg.objects.all()
    tansformations = Transformationimg.objects.all()
    params = {'gellaryimg':gellarys,'Transformationimg':tansformations,'Packages':packege}
    return render(request,"index1.html",params)

def more_gallery(request):
    result = Resultsimg.objects.all()
    reward = Rewardsimg.objects.all()
    params = {'Rewardsimg':reward,'Resultsimg':result}
    return render(request,"more-gallery.html",params)   

def paymenta(request,myid):
    if request.method == "POST":
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        name = request.POST.get('name','')
        montha = request.POST.get('montha','')
        singlePricea = request.POST.get('singlePricea','')
        couplePricea = request.POST.get('couplePricea','')
        select = request.POST.get('select','')
        ordera = Orders(email=email, phone=phone,name=name,montha=montha,singlePricea=singlePricea,couplePricea=couplePricea,select=select)
        ordera.save()
        return render(request,"success.html")
    else:    
        order = Packages.objects.filter(id = myid)
        return render(request,"payment.html",{'Packages':order[0]})
    
def morepackage(request):
    packege = morePackages.objects.all()
    params = {'morePackages':packege}
    return render(request,"more-plan.html",params)
    
def paymentas(request,myid):
    if request.method == "POST":
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        name = request.POST.get('name','')
        singlePricea = request.POST.get('singlePricea','')
        couplePricea = request.POST.get('couplePricea','')
        select = request.POST.get('select','')
        ordera = Orders(email=email, phone=phone,name=name,singlePricea=singlePricea,couplePricea=couplePricea,select=select)
        ordera.save()
        return render(request,"success.html")
    else:    
        order = morePackages.objects.filter(id = myid)
        return render(request,"paymenta.html",{'morePackages':order[0]})    