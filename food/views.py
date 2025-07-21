from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect 
from django.template import loader
from food.models import Item
from lorem_text import lorem

from .forms import NameForm,ItemForm,ItemFormModel
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

def get_name(request):
     if request.method == "POST":
        print("in if post")
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        

    # if a GET (or any other method) we'll create a blank form
     else:
        print("in else part")
        form = NameForm()

     data={'form':form,}
     return render(request, "name.html", data)
     
     
def add_item(request):
    if request.method=="POST":
        form=ItemForm(request.POST)
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        price=request.POST.get('price')
        image=request.POST.get('image')

        print(name,desc,price,image)
        print("in if part filled form")

        obj=Item(item_name=name,item_price=price,item_desc=desc,item_image=image)
        obj.save()
        return redirect('food:index')
        
    else:
        print("in else part empty form")
        form=ItemForm()
    data={'form':form,}
    return render(request,"addItem.html",data)

def add_item_model(request):
    form=ItemFormModel(request.POST or None)
    if request.method=="POST":
        if(form.is_valid):
            form.save()
        return redirect('food:index')
    #else:
        #form=ItemFormModel()
    data={'form':form,}
    
    return render(request,"addItem.html",data)

def update_item(request,item_id):
    item=Item.objects.get(id=item_id)
    form=ItemFormModel(request.POST or None,instance=item)
    if request.method=="POST":
        name=request.POST.get('item_name')
        print(name)
        print(request)
        if(form.is_valid):
                form.save()
                return redirect('food:index')
    data={'form':form,
          'item':item,}
    return render(request,"addItem.html",data)

# Create your views here.
# def index(request):
#     template=loader.get_template('index.html')
#     return HttpResponse(template.render())
#     return HttpResponse("This is our first app")

# def index(request):
#     #item_list=Item.objects.all()
#     #template=loader.get_template('food/index.html')
#     #text=lorem.sentence()
#     student=[{'name':'nupur','per':88,'age':21},
#             {'name':'deepika','per':78,'age':23},
#             {'name':'nirmal','per':99,'age':18},
#             {'name':'abc','per':88,'age':16},]
#     data={
#          #'text':text,
#         'title':'data passing',
#         'student':student,
#     }
#     return render(request, 'index.html',data)

def index(request):
    item_list=Item.objects.all()#this returns list of objects
    data={
         'item_list':item_list,
    }
    return render(request,'index.html',data)

class IndexClassView(ListView):
    model=Item
    template_name='index.html'
    context_object_name='item_list'


# def userform(request):
#     print("before get")
#     if request.method=="GET":
#         print("in get")
#         n1=int(request.GET.get('num1'))
#         n2=int(request.GET.get('num2'))
#         res=n1+n2
#         print("n1=",n1,"and n2=",n2,"result=",res)
#     return render(request,'userform.html')

def userform(request):
    data={}
    res=0
    print("before post",request.method)
    if request.method=="POST":
        print("in post")
        n1=int(request.POST.get('num1'))
        n2=int(request.POST.get('num2'))
    

        data={
            'n1':n1,
            'n2':n2,}

        #print("n1=",n1,"and n2=",n2,"result=",res)
    return render(request,'userform.html',data)

def userform27(request):
    data={}
    res=0
    if request.method=="GET":
        num1=request.GET.get("n1")
        num2=request.GET.get("n2")
        res=num1+num2
        data={'res':res}
    return render(request,'userform27.html',data)

def detail(request,item_id):
    item=Item.objects.get(pk=item_id)

    data={
          'item':item,
     }
    return render(request,'detail.html',data)
     #return HttpResponse("This is item no %s" % item_id)

class DetailClassView(DetailView):
    model=Item
    template_name='detail.html'


# def index(request):
#     item_list=Item.objects.all()
#     #template=loader.get_template('index.html')
#     context={
#         'item_list':item_list,
#     }
#     return render(request, 'index.html',context)
