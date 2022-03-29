from django.contrib import admin
from .models import Mahsulot, CostomUser


# Register your models here.

@admin.register(Mahsulot)
class MahsulotAdmin(admin.ModelAdmin):
    list_display = ('tur','nom','rang','narx','avatar','son','sana')
    list_filter = ('tur','nom','rang','sana')
    search_fields = ('nom',)
    readonly_fields = ('avatar',)


    
admin.site.register(CostomUser)