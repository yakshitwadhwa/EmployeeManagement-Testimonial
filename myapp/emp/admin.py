from django.contrib import admin
from .models import Emp,Testimonial
# Register your models here.

class EmpAdmin(admin.ModelAdmin):
    list_display=('name','emp_id','working','phone')
    list_editable = ('emp_id',)  # ✅ Tuple
    search_fields=('name','phone')
    list_filter=('working','emp_id')







admin.site.register(Emp,EmpAdmin)
admin.site.register(Testimonial)
