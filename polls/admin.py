from django.contrib import admin

from .models import *

class MainAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'photo',)
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')

class DateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'salary', 'area_name', 'published_at', 'cat')
    list_display_links = ('id', 'name')
    search_fields = ('id','name')

class DecemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'decDay')
    list_display_links = ('id', 'decDay')
    search_fields = ('decDay',)


admin.site.register(Mein, MainAdmin)
admin.site.register(Date, DateAdmin)
admin.site.register(decemberDay, DecemberAdmin)
