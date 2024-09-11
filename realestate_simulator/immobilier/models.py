from django.db import models
from datetime import *
from django.utils import timezone

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UtilisateurManager(BaseUserManager):
    def create_user(self, courriel_electronique, password=None, **extra_fields):
        if not courriel_electronique:
            raise ValueError('L\'utilisateur doit avoir un courriel électronique')
        email = self.normalize_email(courriel_electronique)
        user = self.model(courriel_electronique=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, courriel_electronique, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(courriel_electronique, password, **extra_fields)

class Utilisateur(AbstractBaseUser, PermissionsMixin):
    TypeUtilisateur = [
        ("AD", "ADMINISTRATEUR"),
        ("IV", "INVESTISSEUR")
    ]

    type_utilisateur = models.CharField(max_length=2, choices=TypeUtilisateur)
    nom = models.CharField(max_length=32)
    prenom = models.CharField(max_length=32)
    password = models.CharField(max_length=128, default=make_password('defaultpassword'))
    courriel_electronique = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now(), editable=False)

    objects = UtilisateurManager()

    USERNAME_FIELD = 'courriel_electronique'
    REQUIRED_FIELDS = ['nom', 'prenom']

    def __str__(self):
        return self.courriel_electronique


class Propriete(models.Model):
    TypePropriete = [
       ("LB", "LIBRE"),
       ("IM", "IMMOBILIER"),
       ("RS", "RESTAURATION"),
       ("CM", "COMMERCIAL"),
       ("ID", "INDUSTRIEL"),
       ("SP", "SERVICE_PUBLIC"),
       ("SS", "SERVICE_SOCIAL"),
       ("VT", "VERT"),
       ("ED", "EDUCATION"),
       ("TS", "TRANSPORT")
    ]

    type_propriete = models.CharField(
        max_length=2,
        choices=TypePropriete)
    
    disponible = models.BooleanField()
    proprietaire = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, null=True)
    valeur_courrante = models.IntegerField()
    valeur_achat = models.IntegerField()
    position_x = models.IntegerField()
    position_y = models.IntegerField()
    longueur = models.IntegerField()
    largeur = models.IntegerField()
    condition_pourcentage = models.FloatField()

class Transaction(models.Model):

    TypeTransaction = [
        ("VT", "VENTE"),
        ("AC", "ACHAT")
    ]

    type_de_transaction = models.CharField(max_length=2, choices=TypeTransaction)
    propriete = models.OneToOneField(Propriete,on_delete=models.CASCADE)
    vendeur = models.OneToOneField(Utilisateur,related_name='transactions_as_vendeur', on_delete=models.CASCADE)
    acheteur = models.OneToOneField(Utilisateur,related_name='transactions_as_acheteur', on_delete=models.CASCADE)
    prix = models.FloatField()
    date = models.DateField()

class Habitant(models.Model):
    age = models.IntegerField()
    est_employe = models.BooleanField(default=False)
    propriete = models.OneToOneField('Propriete', on_delete=models.CASCADE, null=True)
    satisfaction = models.FloatField(default=0.0)
    





    