from django.contrib import admin
from books.models import book,catagory,burrowedbook,student,adminn
# Register your models here.
admin.site.register(book)
admin.site.register(catagory)
admin.site.register(student)
admin.site.register(adminn)
admin.site.register(burrowedbook)