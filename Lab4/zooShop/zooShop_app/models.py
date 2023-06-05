from django.db import models

# Create your models here.
class Product(models.Model):
    vendor_code = models.CharField(max_length = 20, help_text="Enter vendor code")
    amount = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length = 20, help_text="Enter name")
    description = models.TextField(help_text="Enter description")
    cost = models.IntegerField()
    product_type = models.ForeignKey('ProductType', on_delete=models.SET_NULL, null=True, help_text="Choose product type")
    provider = models.ForeignKey('Provider', on_delete=models.SET_NULL, null=True, help_text="Choose provider")
    photo = models.ImageField(upload_to='images', blank=True)

    def __str__(self) :
        return f'{self.name}, {self.cost}'

class Provider(models.Model):
    name = models.CharField(max_length=20, help_text="Enter name")
    address = models.CharField(max_length=20, help_text="Enter owner")
    phone_number = models.CharField(max_length=20, help_text="Enter phone number")

    def __str__(self):
        return f'{self.name}, {self.address}, {self.phone_number}'

class ProductType(models.Model):
    designation = models.CharField(max_length=20, help_text="Enter type")

    def __str__(self):
        return self.designation
#
#     # def get_absolute_url(self):
#     #     return reverse('main:car_list_by_carcass', args=[str(self.designation)])

class Client(models.Model):
    first_name = models.CharField(max_length=20, help_text='Enter first name')
    last_name = models.CharField(max_length=20, help_text='Enter last name')
    date_of_birth = models.DateField(help_text="Enter date of birth")
    email = models.EmailField(help_text="Enter email")
    phone_number = models.CharField(max_length=15, help_text='Enter phone number')

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

    def get_absolute_url(self):
        return reverse('client-detail', args=[str(self.id)])