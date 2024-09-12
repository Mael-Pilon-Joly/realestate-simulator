from typing import List
from immobilier.models import Propriete, Quartier
from immobilier.services.Iservice import IService

class ServiceCriminalite(IService):

     def determiner_proprietes_proches(self, proprietes: List[Propriete], quartier_vise: Quartier):
        return IService.determiner_proprietes_proches(quartier_vise, nombre_km=1)
     
     
     def determiner_taux_criminalite_selon_immobilier_proche(self, proprietesDansQuartier: List[Propriete], quartier_vise: Quartier):
        # Call the static method directly from the IService class
        proprietes_dans_quartier = IService.determine_proprietes_dans_perimetre(proprietesDansQuartier)
        taux_criminalite_cartier_vise = quartier_vise.taux_de_criminalite

        for t in proprietes_dans_quartier:
                if t.type_propriete == "SS":
                     if t.condition_pourcentage >= 0.80:
                         taux_criminalite_cartier_vise *= 0.9
                     else:
                         taux_criminalite_cartier_vise *= 1.15
                if t.type_propriete == "ID":
                     if t.condition_pourcentage >= 0.80:
                        taux_criminalite_cartier_vise *= 0.95
                     else:
                        taux_criminalite_cartier_vise *= 1.1
                if t.type_propriete == "TS":
                     if t.longueur * t.largeur >= 15000:
                        taux_criminalite_cartier_vise *= 1.1
                if t.type_propriete == "CM":
                     if t.condition_pourcentage >= 0.80:
                        taux_criminalite_cartier_vise *= 0.85
                     else:
                        taux_criminalite_cartier_vise *= 1.1
                if t.type_propriete == "VT":
                        if t.condition_pourcentage >= 0.80:
                            taux_criminalite_cartier_vise *= 0.90
                        else:
                            taux_criminalite_cartier_vise *= 1.1
                if t.type_propriete == "SP":
                        if t.condition_pourcentage >= 0.80:
                            taux_criminalite_cartier_vise *= 0.85
                        else:
                            taux_criminalite_cartier_vise *= 1.15

        return taux_criminalite_cartier_vise
            