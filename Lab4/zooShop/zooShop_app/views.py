from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout, login
from .models import *
from django.views.generic import DetailView, CreateView
from django.urls import reverse_lazy
from zooShop_app.forms import RegisterUserForm, LoginUserForm, ProductForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from cart.forms import CartAddProductForm
import requests


# Create your views here.

def index(request):
    products = Product.objects.all()[:3]
    joke = requests.get('https://official-joke-api.appspot.com/jokes/random').json()
    cat = requests.get('https://catfact.ninja/fact').json()
    return render(request, 'index.html',
                  context={'products': products, 'joke': joke['setup'] + joke['punchline'], 'cat': cat['fact']})


def ProductsList(request, type=None):
    products = Product.objects.all()
    product_type = None
    product_types = ProductType.objects.all()
    sort_type_price = request.GET.get('sort_price')

    if str(sort_type_price) == 'ascending':
        products = products.order_by('cost')

    elif str(sort_type_price) == 'descending':
        products = products.order_by('-cost')

    if type:
        product_type = get_object_or_404(ProductType, designation=type)
        products = products.filter(product_type=product_type)
        print(product_type)

    return render(request, 'products.html', {'products': products, 'product_type': product_type, 'product_types': product_types})


class ProductDetailView(DetailView):
    model = Product
    cart_product_form = CartAddProductForm()

    template_name = 'product_details.html'


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    cart_product_form = CartAddProductForm()

    return render(request,
                  'product_details.html',
                  {'product': product, 'cart_product_form': cart_product_form})


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('zooShop_app:login')

    def form_valid(self, form):
        user = form.save()

        Client.objects.create(first_name=form.cleaned_data['first_name'],
                              last_name=form.cleaned_data['last_name'],
                              date_of_birth=form.cleaned_data['date_birthday'],
                              email=form.cleaned_data['email'],
                              phone_number=form.cleaned_data['phone_number']).save()

        login(self.request, user)
        return redirect('zooShop_app:index')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'
    success_url = reverse_lazy('zooShop_app:login')

    def get_success_url(self):
        return reverse_lazy('zooShop_app:index')


def logout_user(request):
    logout(request)
    return redirect('zooShop_app:index')


def product_create(request):
    form = ProductForm()

    if request.method == "POST":
        product = Product.objects.create(vendor_code=request.POST.get('vendor_code'),
                                 amount=request.POST.get('amount'),
                                 name=request.POST.get('name'),
                                 description=request.POST.get('description'),
                                 cost=request.POST.get('cost'),
                                 product_type=ProductType.objects.get(id=request.POST.get('product_type')),
                                 provider=Provider.objects.get(id=request.POST.get('provider')),
                                 photo=request.FILES.get('photo')),


    else:
        return render(request, "create_product.html", {"form": form})
    return HttpResponseRedirect("/")


def product_edit(request, id):
    try:
        product = Product.objects.get(id=id)

        form = ProductForm(initial={'vendor_code': product.vendor_code, 'amount': product.amount,'name': product.name,
                                'description': product.description, 'cost': product.cost,
                                'product_type': product.product_type, 'provider': product.provider,
                                'photo': product.photo})

        if request.method == "POST":
            product.vendor_code = request.POST.get('vendor_code')
            product.amount = request.POST.get('amount')
            product.name = request.POST.get('name')
            product.description = request.POST.get('description')
            product.cost = request.POST.get('cost')
            product.product_type = ProductType.objects.get(id=request.POST.get('product_type'))
            product.provider = Provider.objects.get(id=request.POST.get('provider'))
            product.photo = request.FILES.get('photo')
            product.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit_product.html", {"product": product, 'form': form})

    except product.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found :(</h2>")


def product_delete(request, id):
    try:
        product = Product.objects.get(id=id)
        product.delete()
        return HttpResponseRedirect("/")
    except product.DoesNotExist:
        return HttpResponseNotFound("<h2>product not found</h2>")
