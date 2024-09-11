from typing import List
from immobilier.models import Propriete, Quartier
from realestate_simulator.immobilier.services.Iservice import IService

class ServiceCriminalite(IService):

     def determiner_proprietes_proches(proprietes: List[Propriete], quartier_vise: Quartier):
          return super().determiner_proprietes_proches(quartier_vise, nombre_km=0)
     
     def determiner_taux_criminalite(self, proprietesDansQuartier: List[Propriete], quartier_vise: Quartier):
        typesProprietesDansQuartier = self.determiner_propriete_dans_perimetre(proprietesDansQuartier)

        