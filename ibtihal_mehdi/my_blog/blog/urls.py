from django import views
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path("",views.home,name="Aceuil"),
    path("afficher",views.afficher,name="afficher"),
    path("ajouter",views.ajouter,name="ajouter"),
    path("supprimer/<int:id>",views.supprimer,name="supprimer"),
    path("modifier/<int:id>",views.modifier,name="modifier"),
    path("ajouterc",views.ajouterc,name="ajouterc"),
    path("afficherc",views.afficherc,name="afficherc"),
    path("login",views.login,name="login"),
 ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)