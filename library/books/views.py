import datetime

from django.shortcuts import render,get_object_or_404,redirect
from books.models import catagory,book
from django.http import HttpResponse
from datetime import datetime,date,timedelta
from django.utils import timezone
# Create your views here.
from books.models import book,catagory,student,adminn,burrowedbook
def base(request,ip):
    a = get_object_or_404(student, pk=ip)
    d = {"student": a}
    return render(request, "layouts/base.html", d)
def abase(request,ip):

    a = get_object_or_404(adminn, pk=ip)
    d = {"admin": a}
    return render(request, "layouts/abase.html", d)
def ahome(request,ib):
    catagories = catagory.objects.all()
    a=get_object_or_404(adminn,pk=ib)
    d = {"catagories": catagories,"admin":a}
    return render(request,"ahome.html",d)
def home(request,ib):
    catagories = catagory.objects.all()
    a = get_object_or_404(student, pk=ib)
    d = {"catagories": catagories,"student":a}
    return render(request,"home.html",d)
def login(request):
    if request.method=="POST":
        name=request.POST["Username"]
        password=request.POST["password"]
        c=student.objects.filter(name=name).count()
        if c== 1:
            x=student.objects.filter(name=name).first()
            if password==x.password:
                return base(request,x.id)
            else:
                return render(request,"login.html")
        else:
            return render(request, "login.html")

    elif request.method=="GET":
        return render(request,"login.html")
def alogin(request):
    if request.method=="POST":
        name=request.POST["Username"]
        password=request.POST["password"]
        c=adminn.objects.filter(name=name).count()
        if c== 1:
            x=adminn.objects.filter(name=name).first()
            if password==x.password:
                return abase(request,x.id)
            else:
                return render(request,"alogin.html")
        else:
            return render(request, "alogin.html")

    elif request.method=="GET":
        return render(request,"alogin.html")
def info(request,ib,pro_info):
    c=get_object_or_404(catagory,pk=pro_info)
    a = get_object_or_404(student, pk=ib)
    b=book.objects.all()
    context={"c":c ,"b":b,"student":a}
    return render(request,"info.html",context)
def ainfo(request,ib,pro_info):
    c = get_object_or_404(catagory, pk=pro_info)
    a = get_object_or_404(adminn, pk=ib)
    b = book.objects.all()
    context = {"c": c, "b": b,"admin":a}
    return render(request, "ainfo.html", context)
def viewp(request,ic):
    ad=get_object_or_404(adminn,pk=ic)
    d={"admin":ad}
    return render(request,"viewp.html",d)
def aregister(request):
    if request.method == "GET":
         return render(request, "aregister.html")
    if request.method=="POST":
        pr=adminn()
        pr.name=request.POST["username"]
        pr.password = request.POST["password"]
        pr.save()
        return redirect("alogin")
def register(request):
    if request.method == "GET":
         return render(request, "register.html")
    if request.method=="POST":
        pr=student()
        pr.name=request.POST["username"]
        pr.password = request.POST["password"]
        pr.save()
        return redirect("login")
def viewps(request,ic):
    ad=get_object_or_404(student,pk=ic)
    d={"student":ad}
    return render(request,"viewps.html",d)
def search(request,ib):
    a = get_object_or_404(adminn, pk=ib)
    d={"admin":a}
    if request.method=="POST":
        searchname=request.POST["searchname"]
        try:
            val = int(searchname)
        except ValueError:
            return render(request, "search.html", d)
        students=student.objects.filter(pk=val)
        context={"student":students,"admin":a}
        return render(request,"search.html",context)

    elif request.method=="GET":
           return render(request,"search.html",d)
def edit(request,ic):
    ad=get_object_or_404(student,pk=ic)
    d={"student":ad}
    return render(request,"edit.html",d)
def update(request,pro_id):
    pr = get_object_or_404(student, pk=pro_id)
    pr.name = request.POST["name"]
    pr.password = request.POST["password"]
    pr.save()
    return redirect("home",pro_id)
def aedit(request,ic):
    ad=get_object_or_404(adminn,pk=ic)
    d={"admin":ad}
    return render(request,"aedit.html",d)
def aupdate(request,pro_id):
    pr = get_object_or_404(adminn, pk=pro_id)
    pr.name = request.POST["name"]
    pr.password = request.POST["password"]
    pr.save()
    return redirect("ahome",pro_id)
def students(request,ib):
    s=student.objects.all()
    a = get_object_or_404(adminn, pk=ib)
    d={"student":s,"admin":a}
    return render(request,"students.html",d)
def delete(request,pro_id,ib):
    books=get_object_or_404(book,pk=pro_id)
    books.delete()
    return redirect("ahome",ib)
def add(request,ib):
    a = get_object_or_404(adminn, pk=ib)
    if request.method == "GET":
        c=catagory.objects.all()
        d={"catagory":c,"admin":a}
        return render(request, "add.html",d)
    if request.method=="POST":
        pr=book()
        pr.name=request.POST["name"]
        pr.img = request.POST["img"]
        pr.disc = request.POST["disc"]
        pr.price = request.POST["price"]
        m=catagory.objects.get(pk=request.POST["catagory"])
        pr.catagory =m
        pr.save()
        return redirect("ahome",ib)
def bedit(request,pro_id,ic):
    ad=get_object_or_404(adminn,pk=ic)
    pr = get_object_or_404(book, pk=pro_id)
    c = catagory.objects.all()
    d={"admin":ad,"book":pr,"catagory":c}
    return render(request,"bedit.html",d)
def bupdate(request,pro_id,ib):
    pr = get_object_or_404(book, pk=pro_id)
    pr.name = request.POST["name"]
    pr.img = request.POST["img"]
    pr.disc = request.POST["disc"]
    pr.price = request.POST["price"]
    m = catagory.objects.get(pk=request.POST["catagory"])
    pr.catagory = m
    pr.save()
    return redirect("ahome",ib)
def burrow(request,ib,b):
    b=get_object_or_404(book,pk=b)
    pr=burrowedbook()
    pr.name=b.name
    pr.img = b.img
    pr.disc = b.disc
    pr.price = b.price
    pr.num=ib
    pr.catagory =b.catagory
    pr.save()
    b.delete()
    return redirect("home",ib)
def returnn(request,ib,b):
    b=get_object_or_404(burrowedbook,pk=b)
    pr=book()
    pr.name=b.name
    pr.img = b.img
    pr.disc = b.disc
    pr.price = b.price
    pr.catagory =b.catagory
    pr.save()
    b.delete()
    return redirect("home",ib)
def burrowed(request,ib):
    bb=burrowedbook.objects.filter(num=ib)
    dd=timezone.now()
    for i in bb:
        x=i.created_at+timedelta(days=3)
        if dd>=x:
            returnn(request,ib,i.id)
    a = get_object_or_404(student, pk=ib)
    b={"burrowed":bb,"student":a}
    return render(request,"burrowed.html",b)
def aburrowed(request,ib):
    a=get_object_or_404(adminn,pk=ib)
    b=burrowedbook.objects.all()
    s=student.objects.all()
    d={"admin":a,"student":s,"burrowed":b}
    return render(request,"aburrowed.html",d)
def alibrary(request,ib):
    a=get_object_or_404(adminn,pk=ib)
    b=book.objects.all()
    d={"book":b,"admin":a}
    return render(request,"alibrary.html",d)
def library(request,ib):
    a=get_object_or_404(student,pk=ib)
    b=book.objects.all()
    d={"book":b,"student":a}
    return render(request,"library.html",d)
def burrowedd(request,ib):
    a=get_object_or_404(student,pk=ib)
    b=burrowedbook.objects.all()
    s=student.objects.all()
    d={"student":a,"students":s,"burrowed":b}
    return render(request,"burrowedd.html",d)

