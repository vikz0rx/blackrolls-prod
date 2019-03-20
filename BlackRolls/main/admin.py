from django.contrib import admin
from django.utils.html import format_html
from .models import *

@admin.register(FoodKind)
class FoodKindAdmin(admin.ModelAdmin):
    list_display = ('title', )

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="50" />'.format(obj.image.url))

    image_tag.short_description = ''

    list_display = ('image_tag', 'kind', 'title', 'cost', 'cost_on_sale', 'weight', )