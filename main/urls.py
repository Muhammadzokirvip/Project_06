from django.urls import path
from . import views

urlpatterns = [
    # front
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('news', views.news, name='news'),
    # dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/region/create', views.create_region, name='create_region'),
    path('dashboard/region/list', views.regions, name='regions'),
    path('dashboard/region/update/<int:id>/', views.region_update, name='region_update'),
    path('dashboard/region/delete/<int:id>/', views.region_delete, name='region_delete'),


    path('dashboard/categoriya/create', views.create_categoriya, name='create_categoriya'),
    path('dashboard/categoriya/list', views.create_categoriya, name='categoriya'),
    path('dashboard/categoriya/update/<int:id>/', views.category_update, name='categoriya_update'),
    path('dashboard/categoriya/delete/<int:id>/', views.categoriya_delete, name='categoriya_delete'),
]