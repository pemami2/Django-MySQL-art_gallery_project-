from django.contrib import admin

# Register your models here.
from .models import Artist, Artshow, Artwork, Style, Location, Contact, Customer

admin.site.register(Artshow)
admin.site.register(Artist)
admin.site.register(Artwork)
admin.site.register(Style)
admin.site.register(Location)
admin.site.register(Contact)
admin.site.register(Customer)

