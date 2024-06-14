from django.db import models

# Create your models here.
from django.db import models

class Malade(models.Model):
    STATUT_CHOICES = [
        ('Married', 'Married'),
        ('Single', 'Single'),
        ('Divorced', 'Divorced'),
        ('Other', 'Other')
    ]

    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    adresse_naissance = models.CharField(max_length=200)
    adresse_actuelle = models.CharField(max_length=200)
    numero_telephone = models.CharField(max_length=15)
    numero_identite = models.CharField(max_length=20)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES)
    occupation = models.CharField(max_length=100)
    est_retraite = models.BooleanField(default=False)
    contact_personnel = models.CharField(max_length=100)
    numero_maison = models.CharField(max_length=10)
    numero_deuxieme_personne = models.CharField(max_length=15)
    nom_maladie_chronique = models.CharField(max_length=200)
    description_maladie = models.TextField()
    effets_maladie = models.TextField()
    description_deuxieme_maladie = models.TextField(blank=True, null=True)
    effets_deuxieme_maladie = models.TextField(blank=True, null=True)
    analyse_maladie = models.FileField(upload_to='analyses/')
    analyse_deuxieme_maladie = models.FileField(upload_to='analyses/', blank=True, null=True)
    medicaments= models.TextField()
    contact_medecin = models.CharField(max_length=200)
   

    def __str__(self):
        return f" {self.numero_identite} {self.nom} {self.prenom} "


class Doctor(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    id_docteur = models.CharField(max_length=20, unique=True)
    specialite = models.CharField(max_length=200)
    numero_telephone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nom} {self.prenom}"