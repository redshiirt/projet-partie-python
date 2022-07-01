from distutils.command.upload import upload
from email.mime import image
from email.policy import default
from django.db import models

# Create your models here.
class  produit (models.Model):
    id=models.AutoField(primary_key=1)
    nom=models.CharField(max_length=50)
    description=models.TextField()
    prix=models.IntegerField()
    image=models.ImageField(null=True,blank=True,upload_to="images")
    def __str__(self):
        return self.nom
    
class  commande (models.Model):  
     id_c=models.AutoField(primary_key=1) 
     description=models.TextField()
     prix=models.IntegerField(default=0)
     quantite=models.IntegerField(default=0)
     total=models.IntegerField()
     def __str__(self):
        return self.description
    
class fournisseur (models.Model):
    id_f=models.AutoField(primary_key=1)
    nom=models.CharField(max_length=50)
    description=models.TextField()
    def __str__(self):
        return self.nom
    
