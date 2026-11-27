from django.contrib import admin
from .models import Parish, Specialty, Service, Provider, ProviderService
# Importing tables from models.py


# Lets you add a provider's services and prices on the provider's own page
class ProviderServiceInline(admin.TabularInline):
    model = ProviderService
    extra = 2

# put Provider on the admin site, using the settings in the class right below
@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ("name", "parish", "phone", "last_confirmed")
    list_filter = ("parish",)
    search_fields = ("name", "address")
    inlines = [ProviderServiceInline]

# The list shows each service's name, specialty and procedure tickbox. You can filter by specialty and by procedure or not, and search by name.
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "specialty", "is_procedure")
    list_filter = ("specialty", "is_procedure")
    search_fields = ("name",)

# These two tables are just a name each, so they need no special settings. This is the plain way to put them on the admin site.
admin.site.register(Parish)
admin.site.register(Specialty)

# Some more explanation if its still hard to get 

# models.py  = what is stored       (the blueprint)
# admin.py   = how you edit it      (the control panel)
# db.sqlite3 = where it lives       (the actual data)
