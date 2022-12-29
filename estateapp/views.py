
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
from django.core.paginator import Paginator , EmptyPage, PageNotAnInteger
from django.core.paginator import Paginator
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# from .models import Item
from django.db.models import Q

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


def signOut(request):
    logout(request)
    return redirect('/login')

def filterBy(request, id):
    categories = Category.objects.all()
    filter_price = Filter_Price.objects.all()
    item = Item.objects.filter(filter_price = id).all();
    return render(request, 'filterBy.html', {'categories':categories, 'filter_price':filter_price,'item':item})

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





def allproperties(request):

    items = Item.objects.all().order_by("-id")
    page =Paginator(items, 9)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    params= {'page':page,'items': items}
    return render(request, 'properties.html',params)


def about(request):
    # return HttpResponse(contact)
    return render(request, 'about.html')

# //to disply category wise product in index
class ProductCategory(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['allcategories'] =Category.objects.all()[:5]
        context['item'] = Item.objects.all()[:5]






        return context



# class ItemDetail(TemplateView):
#     template_name = "details.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         slug = self.kwargs['slug']
#         item = Item.objects.all().filter(slug = slug)
#         context['item'] =   Item.objects.all().filter(slug = slug)
#         return context

def Search(request):
    # query = request.GET['query']
    allcategories = Category.objects.all()
    query = request.GET.get('query', '')

    items = Item.objects.filter(location__icontains = query)
    page =Paginator(items, 9)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    params = {'allitems':items,'allcategories':allcategories,'page':page}
    return render(request, 'search.html', params)

# def Search(request):
#     items = Item.objects.filter(
#         Q(category__icontains=request.GET['name']) |
#         Q(location__icontains=request.GET['query'])
#     )
#     params = {'allitems':items}
#     return render(request, 'search.html', params)



def buy(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    item = Item.objects.all()
    filter_price = Filter_Price.objects.all()

    CATID = request.GET.get('categories')
    PRICE_FILTER_ID = request.GET.get('filter_price')
    page =Paginator(item, 9)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)


    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        item = item.filter(category=category)
        page =Paginator(item, 9)
        page_list = request.GET.get('page')
        page = page.get_page(page_list)


    if  PRICE_FILTER_ID :
        item = Item.objects.filter(filter_price= PRICE_FILTER_ID )
        page =Paginator(item, 9)
        page_list = request.GET.get('page')
        page = page.get_page(page_list)




    return render(request, 'buy.html', {'categories':categories,
                                              'category':category,
                                              'page':page,
                                              'item':item,
                                              'filter_price':filter_price,
                                              'allcategories':categories,

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

@login_required(login_url ="/login")
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



# def item_detail(request,slug):
    # item=get_object_or_404(Item,id=id)
    # ItemAll =Item.objects.all()
    # item= Item.objects.filter(slug=slug)
    # return render(request,'details.html',{'item':item,'ItemAll':ItemAll})

def item_detail(request, id):
    # context ={}
    # context["item"] = Item.objects.filter(id = id)
    # return render(request, "details.html", context)
    product_details = Item.objects.get(id=id)
    print(id)

    return render(request, "details.html",{'context':product_details})
