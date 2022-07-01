from django.contrib import admin
from .models import commande, produit
# Register your models here.
@admin.register(produit)
class produitadmin(admin.ModelAdmin):
    list_display=['id','nom','description','prix','image']
    
@admin.register(commande)
class commandeadmin(admin.ModelAdmin):
    list_display=['id_c','description','prix','quantite','total']