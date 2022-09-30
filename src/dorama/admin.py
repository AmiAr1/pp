from django.contrib import admin

from . import models

# admin.site.register(models.Dorama)

@admin.register(models.Dorama)
class  DoramaModel(admin.ModelAdmin):
    list_display = ["name"]
    save_on_top = True
    save_as_continue = True
    save_as =True