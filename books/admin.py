from django.contrib import admin

# Register your models here.
from books.models import Books,Publisher,Bookauthors
admin.site.register(Books)
admin.site.register(Publisher)
admin.site.register(Bookauthors)
