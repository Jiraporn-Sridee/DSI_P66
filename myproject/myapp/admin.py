from django.contrib import admin
from myapp.models import *

class Product_list_Admin(admin.ModelAdmin):
    pass
admin.site.register(Product_list, Product_list_Admin)

class CustomerAdmin(admin.ModelAdmin):
    pass
admin.site.register(customer, CustomerAdmin)

class ReportAdmin(admin.ModelAdmin):
    pass
admin.site.register(Report_issue, ReportAdmin)

class TransactionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Transaction, TransactionAdmin)

class OrderAdmin(admin.ModelAdmin):
    pass
admin.site.register(Order, OrderAdmin)