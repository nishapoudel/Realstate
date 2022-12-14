from django.urls import path, include
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

app_name ="estateapp"
urlpatterns=[
    # path("", views.index, name='home'),
    path("login", views.login_user, name='login'),
    path("register", views.register, name='register'),
    # path('social_auth/', include('social_django.urls', namespace='social')),

    path("", ProductCategory.as_view(), name='home'),

    path("signOut", views.signOut, name='logout'),
    path("filterByPrice/<int:id>", views.filterBy, name='logout'),

    #  path('Item/<slug:slug>/', ItemDetail.as_view(), name="ItemDetail"),


     path("contact/", views.contact, name="Contactus"),

     path("buy", views.buy, name='buy'),
     path('<slug:category_slug>/', views.buy, name="item_by_category"),
     path('item/<int:id>/', views.item_detail, name="item_detail"),

    #   path('item/<slug:slug>/', views.item_detail, name="item_detail"),
#  path('item/<int:id>/', views.item_detail, name="item_detail"),
      path('item/<slug:category_slug>/', views.buy, ),

    #  path('<slug:slug>/', views.item_detail, name="item_detail"),


     path("sell", views.sell, name="sell"),

     path('item/<int:id>/', views.item_detail, name="item_detail"),

     path("about", views.about, name="about"),
    path("properties", views.allproperties, name="allproperties"),





     path("search", views.Search, name="search"),

    #   path('<slug:category_slug>', views.index, name='item_by_category'),
    # path("realestate/<int:id>/", views.ReadCat, name="readcategory"),
    #  path("realestate/<str:slug>/", views.ReadCat, name="readcategory"),

    #  path('', views.story_list, name='story_list'),
    #  path('<slug:category_slug>', views.story_list, name='story_by_category'),
    #  path('<int:id>/', views.story_detail, name='story_detail'),
]  +  static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)