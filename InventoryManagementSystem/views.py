from django.shortcuts import render,redirect
from InventoryManagementSystem.models import *

# Create your views here.
def showIndex(request):
    return render(request,"admin_login.html")
def admin_login(request):
    un=request.POST.get("t1")
    up=request.POST.get("t2")
    if un=="Preeti" and up=="Ranjan":
        return render(request,'admin_home.html',{"username":un})
    else:
        return render(request,"admin_login.html",{"message":"Invalid User*"})
def add_new(request):
    return render(request,"add_new.html")
def save_product(request):
    cm=request.POST.get("p1")
    cv=request.POST.get("p2")
    md=request.POST.get("p3")
    cn=request.POST.get("p4")
    en=request.POST.get("p5")
    ProductModel(carmodel=cm,variant=cv,mdate=md,chasis_no=cn,engine_no=en).save()
    return render(request,"add_new.html")
def view_details(request):
    return render(request,"view_details.html",{"data":ProductModel.objects.all()})


def total_car(request):
    result=len(ProductModel.objects.all())
    return render(request,"total_car.html",{"data":result})


def change_details(request):
   result= ProductModel.objects.all()
   return render(request,"update.html",{"data":result})


def update_data(request,pk):
    res=ProductModel.objects.get(car_serial_no=pk)
    return render(request,"changedata.html",{"data":res})


def update(request):
    st=request.POST.get("c1")
    cs=request.POST.get("c3")
    sd=request.POST.get("c2")
    result=ProductModel.objects.get(car_serial_no=cs)
    OrderModel(shipping_date=sd,product_id=cs).save()
    result.status=st
    result.save()
    return render(request,"changedata.html")


def total_shipped(request):
    result=len(ProductModel.objects.filter(status="inactive"))
    return render(request,"total_shipped.html",{"data":result})


def manufacture(request):
   result=ProductModel.objects.all()
   return render(request,"manufacture.html",{"data":result})


def fetch(request,pk):
    res = ProductModel.objects.get(car_serial_no=pk)
    return render(request, "fetch.html", {"data": res})


def car_stock(request):
    result = len(ProductModel.objects.filter(status="active"))
    return render(request, "total_stock.html", {"data": result})


def serial(request):
    result = ProductModel.objects.all()
    return render(request, "serial.html", {"data": result})


def fetch_serial(request,pk):
    res = ProductModel.objects.get(car_serial_no=pk)
    return render(request, "fetch_serial.html", {"data": res})


def status(request):
    result = ProductModel.objects.all()
    return render(request, "status.html", {"data": result})


def fetch_status(request,pk):
    res = ProductModel.objects.get(car_serial_no=pk)
    return render(request, "fetch_status.html", {"data": res})


def shipping(request):
    result = OrderModel.objects.all()
    return render(request, "shipping.html", {"data": result})


def fetch_shipping(request,pk):
    res = ProductModel.objects.get(car_serial_no=pk)
    t_id=OrderModel.objects.get(product_id=pk)
    return render(request,"fetch_shipping.html", {"data": res,"id":t_id})


def track(request):
    result = OrderModel.objects.all()
    return render(request, "track.html", {"data": result})


def fetch_track(request,pk):
    res = ProductModel.objects.get(car_serial_no=pk)
    t_id = OrderModel.objects.get(product_id=pk)
    return render(request, "fetch_track.html", {"data": res, "id": t_id})