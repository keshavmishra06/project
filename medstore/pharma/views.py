from django.views import generic
from .models import Order
from django.shortcuts import render

def form(request):
    return render(request, 'pharma/orderform.html')

def forminsert(request):
    order=Order()
    order.cust_id=request.POST['cid']
    order.fname=request.POST['fname']
    order.lname=request.POST['lname']
    order.phn_no=request.POST['pno']
    order.med_name=request.POST['medname']
    order.qty=request.POST['quantity']
    order.save()
    return render(request, 'pharma/index.html')

def table(request):
    order=Order.objects.all()
    dic={"order":order}
    return render(request, 'pharma/table.html',dic)
def home(request):
    return render(request,'pharma/index.html')






