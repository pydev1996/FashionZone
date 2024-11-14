from django.contrib import admin
from .models import Customer,Product,Orders,Feedback
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Customer, CustomerAdmin)

class ProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product, ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    pass
admin.site.register(Orders, OrderAdmin)

class FeedbackAdmin(admin.ModelAdmin):
    pass
admin.site.register(Feedback, FeedbackAdmin)
# Register your models here.
from django.contrib import admin
from .models import Designer

from django.contrib import admin
from .models import Designer, DesignerImage

class DesignerImageInline(admin.TabularInline):
    model = DesignerImage
    extra = 1  # Number of empty image fields to display

@admin.register(Designer)
class DesignerAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'address')
    search_fields = ('name', 'contact')
    inlines = [DesignerImageInline]
