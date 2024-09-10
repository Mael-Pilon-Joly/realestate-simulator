from django.db import models

# Create your models here.

class Utilisateur(models.Model):
    TypeUtilisateur = [
        ("AD", "ADMINISTRATEUR"),
        ("IV", "INVESTISSEUR")
    ]

    type_utilisateur = models.CharField(max_length=2, choices=TypeUtilisateur)
    nom = models.CharField(max_length=32)
    prenom = models.CharField(max_length=32)
    courriel_electronique = models.EmailField(unique=True)
    hash_mot_de_passe = models.CharField(max_length=128)


class Propriete(models.Model):
    TypePropriete = [
       ("LB", "LIBRE"),
       ("IM", "IMMOBILIER"),
       ("RS", "RESTAURATION"),
       ("CM", "COMMERCIAL"),
       ("ID", "INDUSTRIEL")
       ("SP", "SERVICE_PUBLIC")
       ("SS", "SERVICE_SOCIAL"),
       ("VT", "VERT"),
       ("ED", "EDUCATION"),
       ("TS", "TRANSPORT")
    ]

    type_service = models.CharField(
        max_length=2,
        choices=TypePropriete)
    
    disponible = models.BooleanField()
    proprietaire = models.ForeignKey(Utilisateur)
    valeur_courrante = models.IntegerField()
    valeur_achat = models.IntegerField()
    position_x = models.IntegerField()
    position_y = models.IntegerField()
    longueur = models.IntegerField()
    largeur = models.IntegerField()
    condition_pourcentage = models.FloatField()

class Transaction:

    TypeTransaction = [
        ("VT", "VENTE"),
        ("AC", "ACHAT")
    ]

    type_de_transaction = models.CharField(max_length=2, choices=TypeTransaction)
    propriete = models.OneToOneField(Propriete,on_delete=models.CASCADE, parent_link=True,  primary_key=True)
    vendeur = models.OneToOneField(Utilisateur,on_delete=models.CASCADE, parent_link=True,  primary_key=True)
    acheteur = models.OneToOneField(Utilisateur,on_delete=models.CASCADE, parent_link=True,  primary_key=True)
    prix = models.FloatField()
    date = models.DateField()

class Habitant(models.Model):
    age = models.IntegerField()
    est_employe = models.BooleanField
    propriete = models.OneToOneField('Propriete', on_delete=models.CASCADE)
    satisfaction = models.FloatField(default=0.0)
    





    