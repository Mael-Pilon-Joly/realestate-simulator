from django.test import TestCase
from immobilier.services.serviceValeur import determiner_proprietes_proches
from immobilier.models import Propriete

# Create your tests here.
class ImmobilierTestCase(TestCase):
    def setUp(self):
        # B dans A (1km) C dans A (3km)
        self.propriete_a = Propriete.objects.create(disponible=True, proprietaire=None, valeur_courrante=0, valeur_achat=0, position_x=100, position_y=200, largeur=50, longueur=100, condition_pourcentage=80.0)
        self.propriete_b = Propriete.objects.create(disponible=True, proprietaire=None, valeur_courrante=0, valeur_achat=0, position_x=925, position_y=800, largeur=50, longueur=300, condition_pourcentage=80.0)
        self.propriete_c = Propriete.objects.create(disponible=True, proprietaire=None, valeur_courrante=0, valeur_achat=0, position_x=2500, position_y=2800, largeur=50, longueur=100, condition_pourcentage=80.0)
        liste_proprietes = []
        liste_proprietes.append(self.propriete_a)
        liste_proprietes.append(self.propriete_b)
        liste_proprietes.append(self.propriete_c)
        self.liste_proprietes  = liste_proprietes
    
    def test_proprietes_dans_rayon_1_km(self):
        proprietes_dans_rayon_1_km = determiner_proprietes_proches(self.liste_proprietes, self.propriete_a, 1)
        self.assertTrue(self.propriete_b in proprietes_dans_rayon_1_km)
        self.assertFalse(self.propriete_c in proprietes_dans_rayon_1_km)
    

    def test_proprietes_dans_rayon_3_km(self):
        proprietes_dans_rayon_3_km = determiner_proprietes_proches(self.liste_proprietes, self.propriete_a, 3)
        self.assertTrue(self.propriete_b in proprietes_dans_rayon_3_km)
        self.assertTrue(self.propriete_c in proprietes_dans_rayon_3_km)