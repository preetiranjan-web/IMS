"""IMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from InventoryManagementSystem import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.showIndex, name="main"),
    path('admin_login/', views.admin_login, name="admin_login"),
    path("add_new_inventory/", views.add_new, name="add_new_inventory"),
    path("save_product/", views.save_product, name="save_product"),
    path("view_details/", views.view_details, name="view_details"),
    path("change/", views.change_details, name="change"),
    path("total_car/", views.total_car, name="total_car"),
    path("update_data/<int:pk>/", views.update_data, name="update_data"),
    path("update/",views.update,name="update"),
    path("total_shipped/",views.total_shipped,name="total_shipped"),
    path("manufacture/",views.manufacture,name="manufacture"),
    path("fetch/<int:pk>/",views.fetch,name="fetch"),
    path("car_stock/",views.car_stock,name="car_stock"),
    path("serial/",views.serial,name="serial"),
    path("fetch_serial/<int:pk>/",views.fetch_serial,name="fetch_serial"),
    path("status_check/", views.status, name="status_check"),
    path("fetch_status/<int:pk>/",views.fetch_status,name="fetch_status"),
    path("shipping/", views.shipping, name="shipping"),
    path("fetch_shipping/<int:pk>/",views.fetch_shipping,name="fetch_shipping"),
    path("track/", views.track, name="track"),
    path("fetch_track/<int:pk>/",views.fetch_track,name="fetch_track"),



]
