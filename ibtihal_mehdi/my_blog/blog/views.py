from ast import Delete
from contextlib import redirect_stderr
from email import message
from multiprocessing import context
from pyexpat.errors import messages

from .forms import commandForm, productForm
from django.shortcuts import redirect, render
from .models import commande, produit 


def home(request):
    pro_data=produit.objects.all()
    return render(request,'accounts/acceuil.html',{'pro_data':pro_data})

def afficher(request):
    pro_data=produit.objects.all()
    return render(request,'accounts/afficher.html',{'pro_data':pro_data})

def ajouter(request):
 form=productForm
 if request.method == 'POST':
    form=productForm(request.POST)
    if form.is_valid():
       form.save(commit=True)
    return redirect('/afficher')
    
 else:
     return render(request,"accounts/form.html",{'form':form})

def supprimer(request,id):
    pro_data=produit.objects.get(id=id)
    pro_data.delete()
    return redirect('/afficher')

def modifier(request,id):
    pro_data=produit.objects.get(id=id)
    form=productForm(instance=pro_data)
    if request.method == 'POST':
        form=productForm(request.POST,instance=pro_data)
        if form.is_valid():
            form.save()
        return redirect('/afficher')
    else:
     return render(request,"accounts/update.html",{'form':form})

def afficherc(request):
    pro_data=commande.objects.all()
    return render(request,'accounts/afficherc.html',{'pro_data':pro_data})

def ajouterc(request):
 form=commandForm
 if request.method == 'POST':
    form=commandForm(request.POST)
    if form.is_valid():
       form.save(commit=True)
    return redirect('/afficherc')
 return render(request,"accounts/formc.html",{'form':form})

def login (request):
    return render(request,"accounts/login.html")

