
from email import message
from unicodedata import category
import django
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from estateapp.forms import ItemForm
# from .models import Item
from .models import *


# Create your views here.

# def index(request):
#     items = Item.objects.all()
#     params= {'items': items}
#     return render(request, 'home.html',params)

# def index(request,category_slug=None):
#     category = None
#     categories = Category.objects.all()
#     item = Item.objects.all()
#     if category_slug:
#         category = get_object_or_404(Category,slug=category_slug)
#         item = item.filter(category=category)
#     return render(request, 'home.html', {'categories':categories,
#                                               'category':category,
#                                               'item':item,
#                                               })



# def ReadCat(request, id):
#     cats = Category.objects.get(cat_id =id)
#     items= Item.objects.filter(category= cats)
#     context = {'cat':cats, 'items':items}
#     return render(request, 'category.html', context)

# def ReadCat(request, slug):
#    if(Category.objects.filter(slug=slug)):
#     items = Item.objects.filter(category_slug = slug)
#     category = Category.objects.filter(slug= slug).first()
#     context = {'items':items, 'category':category}
#     return render(request, 'home.html',context)

#    else:
#     messages.warning(request, "No such category Founded")
#     return redirect('Home')
    # cats = Category.objects.get(cat_id =id)
    # items= Item.objects.filter(category= cats)
    # context = {'cat':cats, 'items':items}
    # return render(request, 'category.html', context)



def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        en=contactEnquiry(name=name,email=email,phone=phone,message=message)
        en.save()

    return render(request, 'contact.html')


def register(request):
        if request.method =='POST':

            username = request.POST['username']
            email = request.POST['email']
            pass1 = request.POST['pass1']
            pass2 = request.POST['pass2']

            if pass1 != pass2:
                messages.error(request, "password do not match")
                return HttpResponseRedirect('register')
            myuser = User.objects.create_user(username, email, pass1 )
            myuser.save()
            messages.success(request, f'Your account has been created. You can log in now!')
            return HttpResponseRedirect('login')

        else:
            # return HttpResponse('404- Not Found')
            return render(request,'register.html')

def login_user(request):
    if request.method =='POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername,password=loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request, "Successfully Logged In")
            return HttpResponseRedirect('sell')
        else:
            messages.success(request,"Invalid Credentials,Please try again")
    return render(request, 'login.html')


def logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

    return render('home')
# def sell(request,category_slug=None):

#     if request.method== "POST":
#         name = request.POST.get('name')
#         location = request.POST.get('location')
#         area = request.POST.get('area')

#         category = Category.objects.get(slug = request.POST['category'])

#         price = request.POST.get('price')
#         image = request.POST.get('image')
#         data =Item(name= name,location=location,area=area,category=category,price=price,image=image)
#         data.save()



#     category=Category.objects.all()
#     context = {'category':category}
#     return render(request, 'sell.html',context
#        )

# def get(self,request):
#     land = Item.objects.filter(slug= slug)
#     return render(request, 'details.html')


def item_detail(request,id):
    # item=get_object_or_404(Item,id=id)
    ItemAll =Item.objects.all()
    item=Item.objects.filter(id=id)
    return render(request,'details.html',{'item':item[0],'ItemAll':ItemAll})



def allproperties(request):

    items = Item.objects.all().order_by("-id")
    params= {'items': items}
    return render(request, 'properties.html',params)


def about(request):
    # return HttpResponse(contact)
    return render(request, 'about.html')

# //to disply category wise product in index
class ProductCategory(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['allcategories'] = Category.objects.all()
        return context

class ItemDetail(TemplateView):
    template_name = "detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_slug = self.kwargs['slug']
        item = Item.objects.get(slug = url_slug)     #get fetchfor one obj, slug is db model and url_slug is url's slug
        context['itemVar'] =  item
        return context

def Search(request):
    # query = request.GET['query']
    query = request.GET.get('query', '')

    items = Item.objects.filter(location__icontains = query)
    params = {'allitems':items}
    return render(request, 'search.html', params)



def buy(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    item = Item.objects.all()
    filter_price = Filter_Price.objects.all()

    CATID = request.GET.get('categories')
    PRICE_FILTER_ID = request.GET.get('filter_price')


    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        item = item.filter(category=category)
    if  PRICE_FILTER_ID :
        item = Item.objects.filter(filter_price= PRICE_FILTER_ID )


    return render(request, 'buy.html', {'categories':categories,
                                              'category':category,
                                              'item':item,
                                              'filter_price':filter_price,
                                              })

    category = None
    categories = Category.objects.all()
    item = Item.objects.all()






    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        item = item.filter(category=category)


    return render(request, 'buy.html', {'categories':categories,
                                              'category':category,

                                              })


def sell(request):
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('buy')
    else:
        form = ItemForm()
    context = {
        "form":form
    }


    return render(request, 'sell.html',context
       )


