from django.contrib import admin

# Register your models here.
from .models import Get_Data_From_User_Model

# Register your models here.
class AdminTest(admin.ModelAdmin):
     list_display = ('username','area_type','availability','location','size','society','total_sqft','bath','balcony')
admin.site.register(Get_Data_From_User_Model,AdminTest)

