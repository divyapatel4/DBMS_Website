from django.contrib import admin
from .models import *

admin.site.register(Visitor)
admin.site.register(Animal)
admin.site.register(Staff)
admin.site.register(WildlifeSanctuary)
admin.site.register(Sighted)
admin.site.register(Patient)
admin.site.register(Expenditure)
admin.site.register(PriceList)
admin.site.register(MobileNo)
admin.site.register(PreysUpon)
admin.site.register(SpeciesData)
admin.site.register(Visited)

# admin.site.register(PriceList)        #Not working for some reason
# admin.site.regsiter(Department)       #Not working for some reason

# Register your models here.
