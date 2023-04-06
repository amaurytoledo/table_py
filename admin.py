from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from django.utils.translation import ugettext_lazy as _

from .models import MyTable

@admin.register(MyTable)
class MyTableAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }
    list_display = ('name', 'description',)
    search_fields = ('name', 'description',)
