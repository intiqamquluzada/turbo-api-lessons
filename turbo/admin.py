from django.contrib import admin
from turbo.models import *


class ImageInline(admin.StackedInline):
    model = CarImages
    extra = 1


class CarAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    readonly_fields = ("user_view_count", )


admin.site.register(Car, CarAdmin)
admin.site.register(Model)
admin.site.register(Marka)
admin.site.register(Color)
admin.site.register(Condition)
admin.site.register(Tags)
