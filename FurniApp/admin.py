from django.contrib import admin     
# Register your models here.
from .models import(
    Customer,
    Product,
    Cart,
)

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','user','name','locality','city',
    'zipcode','state']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display =['id','title','selling_price',
    'discounted_price','description','brand','category',
    'product_image']


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display=['id','user','product','quantity']

