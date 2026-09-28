from django.contrib import admin

from .models import *

@admin.register(Auto)
class auto(admin.ModelAdmin):
    list_display = ['mark', 'model', 'color']

@admin.register(ModelAuto)
class model(admin.ModelAdmin):
    pass

@admin.register(MarkAuto)
class mark(admin.ModelAdmin):
    pass

@admin.register(Order)
class Order(admin.ModelAdmin):
    pass
