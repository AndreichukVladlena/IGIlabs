from django.urls import path
from . import views

app_name = 'zooShop_app'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('products', views.ProductsList, name = 'products'),
    path('products/<int:id>', views.product_detail, name = 'product_details'),
    path('<str:type>', views.ProductsList,name='product_list_by_type'),
    path('register/', views.RegisterUser.as_view(), name = 'register'),
    path('logout/', views.logout_user, name = 'logout'),
    path('login/', views.LoginUser.as_view(), name = 'login'),
    path("create/", views.product_create, name='create'),
    path("products/edit/<int:id>/", views.product_edit),
    path("products/delete/<int:id>/", views.product_delete),

]