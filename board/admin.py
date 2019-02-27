from django.contrib import admin
from .models import BoardMessage
# Register your models here.
class PTTadmin(admin.ModelAdmin):
    list_display = ('id','title','date','author','content')
    search_fields = ('title',)
    ordering = ('id','date')

admin.site.register(BoardMessage, PTTadmin)
