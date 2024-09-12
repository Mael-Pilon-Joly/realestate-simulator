from django.apps import apps
from django.test import TestCase
from immobilier.services.Iservice import IService
from .serviceValeur import ServiceValeur
from .serviceCriminalite import ServiceCriminalite

Propriete = apps.get_model(app_label='immobilier', model_name='Propriete')
Quartier = apps.get_model(app_label='immobilier', model_name='Quartier')

class ImmobilierTestCase(TestCase):
    def setUp(self):
        self.quartier_vise = Quartier.objects.create(taux_de_criminalite=0.5, point_x_depart=100, point_y_depart=100, longueur=2000, largeur=3000)
        
        # B dans A (1km) C dans A (3km)
        self.propriete_a = Propriete.objects.create(type_propriete="IM", disponible=True, proprietaire=None,
                                                    valeur_courrante=100, valeur_achat=0, position_x=100, position_y=200,
                                                    largeur=50, longueur=100, condition_pourcentage=80.0)
        self.propriete_b = Propriete.objects.create(type_propriete="VT", disponible=True, proprietaire=None,
                                                    valeur_courrante=100, valeur_achat=0, position_x=925, position_y=800,
                                                    largeur=50, longueur=300, condition_pourcentage=80.0)
        self.propriete_c = Propriete.objects.create(type_propriete="TS", disponible=True, proprietaire=None,
                                                    valeur_courrante=100, valeur_achat=0, position_x=2500, position_y=2800,
                                                    largeur=50, longueur=100, condition_pourcentage=80.0)
        self.liste_proprietes = [self.propriete_a, self.propriete_b, self.propriete_c]

        # Pour test taux criminalité
        self.propriete_ss = Propriete.objects.create(type_propriete="SS", disponible=True, proprietaire=None,
                                                     valeur_courrante=100, valeur_achat=0, position_x=200,
                                                     position_y=200, largeur=100, longueur=200,
                                                     condition_pourcentage=0.85)
        
        self.propriete_id = Propriete.objects.create(type_propriete="ID", disponible=True, proprietaire=None,
                                                     valeur_courrante=100, valeur_achat=0, position_x=300,
                                                     position_y=300, largeur=100, longueur=200,
                                                     condition_pourcentage=0.75)
        
        self.propriete_cm = Propriete.objects.create(type_propriete="CM", disponible=True, proprietaire=None,
                                                     valeur_courrante=100, valeur_achat=0, position_x=400,
                                                     position_y=400, largeur=100, longueur=200,
                                                     condition_pourcentage=0.80)
        self.proprietes_dans_quartier = [self.propriete_ss, self.propriete_id, self.propriete_cm]


    def test_proprietes_dans_rayon_1_km(self):
        proprietes_dans_rayon_1_km = IService.determiner_proprietes_proches(self.liste_proprietes, self.propriete_a, 1)
        self.assertTrue(self.propriete_b in proprietes_dans_rayon_1_km)
        self.assertFalse(self.propriete_c in proprietes_dans_rayon_1_km)
    
    def test_proprietes_dans_rayon_3_km(self):
        proprietes_dans_rayon_3_km = IService.determiner_proprietes_proches(self.liste_proprietes, self.propriete_a, 3)
        self.assertTrue(self.propriete_b in proprietes_dans_rayon_3_km)
        self.assertTrue(self.propriete_c in proprietes_dans_rayon_3_km)

 
    def test_valeur_ajuster_propriete_immobilier(self):
        serviceValeur = ServiceValeur()  
        serviceValeur.determiner_valeur_ajustement_environment_proche(self.propriete_a, self.liste_proprietes)
        self.assertEqual(self.propriete_a.valeur_courrante, 132.25)  
    
    def test_taux_criminalite_adjustment(self):
        serviceCriminalite = ServiceCriminalite()

        actual_taux_criminalite_calculer = serviceCriminalite.determiner_taux_criminalite_selon_immobilier_proche(self.proprietes_dans_quartier, self.quartier_vise)

        expected_taux_criminalite = 0.5 * 0.9 * 1.1 * 0.85  
        self.assertAlmostEqual(actual_taux_criminalite_calculer, expected_taux_criminalite, places=5)

    def test_taux_criminalite_no_change(self):
        serviceCriminalite = ServiceCriminalite()

        self.propriete_ss.condition_pourcentage = 0.75
        self.propriete_ss.save()

        actual_taux_criminalite_calculer = serviceCriminalite.determiner_taux_criminalite_selon_immobilier_proche(self.proprietes_dans_quartier, self.quartier_vise)

        expected_taux_criminalite = 0.5 * 1.15 * 1.1 * 0.85
        self.assertAlmostEqual(actual_taux_criminalite_calculer, expected_taux_criminalite, places=5)