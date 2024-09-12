from typing import List
from immobilier.models import Propriete 
from immobilier.services.Iservice import IService  


class ServiceValeur(IService):

    def determiner_valeur_ajustement_environment_proche(self, propriete: Propriete, listProprietes: List[Propriete]):
        typesProprietesAProximite = self.determiner_type_proprietes_dans_perimetre(listProprietes)

        # Ajuster la valeur en fonction des types de propriétés à proximité
        match propriete.type_propriete:
            case "IM":
                if "SP" in typesProprietesAProximite:
                    propriete.valeur_courrante += 0.1 * propriete.valeur_courrante
                if "VT" in typesProprietesAProximite:
                    propriete.valeur_courrante += 0.15 * propriete.valeur_courrante
                if "ID" in typesProprietesAProximite:
                    propriete.valeur_courrante -= 0.20 * propriete.valeur_courrante
                if "RS" in typesProprietesAProximite:
                    propriete.valeur_courrante += 0.1 * propriete.valeur_courrante
                if "CM" in typesProprietesAProximite:
                    propriete.valeur_courrante += 0.1 * propriete.valeur_courrante
                if "SS" in typesProprietesAProximite:
                    propriete.valeur_courrante += 0.05 * propriete.valeur_courrante
                if "TS" in typesProprietesAProximite:
                    propriete.valeur_courrante += 0.15 * propriete.valeur_courrante
            
            case "VT":
                if "IM" in typesProprietesAProximite:
                    propriete.valeur_courrante += 0.1 * propriete.valeur_courrante
                if "ID" in typesProprietesAProximite:
                    propriete.valeur_courrante -= 0.15 * propriete.valeur_courrante
            
            case "ID":
              if "IM" in typesProprietesAProximite:
                    propriete.valeur_courrante += 0.1 * propriete.valeur_courrante
              if "TS" in typesProprietesAProximite:
                    propriete.valeur_courrante += 0.15 * propriete.valeur_courrante
            
            case "CM":
                if "IM" in typesProprietesAProximite:
                    propriete.valeur_courrante += 0.15 * propriete.valeur_courrante
                if "ED" in typesProprietesAProximite:
                    propriete.valeur_courrante += 0.1 * propriete.valeur_courrante
                if "TS" in typesProprietesAProximite:
                    propriete.valeur_courrante += 0.15 * propriete.valeur_courrante
            
            case "RS":
                if "IM" in typesProprietesAProximite:
                    propriete.valeur_courrante += 0.1 * propriete.valeur_courrante

            case "SS":
                if "IM" in typesProprietesAProximite:
                    propriete.valeur_courrante += 0.05 * propriete.valeur_courrante
                if "ID" in typesProprietesAProximite:
                    propriete.valeur_courrante -= 0.1 * propriete.valeur_courrante
            
            case "TS":
                if "IM" in typesProprietesAProximite:
                    propriete.valeur_courrante += 0.1 * propriete.valeur_courrante
                if "ID" in typesProprietesAProximite:
                    propriete.valeur_courrante += 0.1 * propriete.valeur_courrante
                if "CM" in typesProprietesAProximite:
                    propriete.valeur_courrante += 0.1 * propriete.valeur_courrante

    def determiner_valeur_ajustement_environment_loin(self, propriete: Propriete, listProprietes: List[Propriete]):
        typesProprietesEloignees = self.determiner_type_proprietes_dans_perimetre(listProprietes)


        match propriete.type_propriete:
            case "IM":
                if "SP" not in typesProprietesEloignees:
                    propriete.valeur_courrante -= 0.15 * propriete.valeur_courrante
                if "SS" not in typesProprietesEloignees:
                    propriete.valeur_courrante -= 0.05 * propriete.valeur_courrante 
                if "VT" not in typesProprietesEloignees:
                    propriete.valeur_courrante -= 0.1 * propriete.valeur_courrante
            case "ID":
              if "IM" not in typesProprietesEloignees:
                    propriete.valeur_courrante -= 0.10 * propriete.valeur_courrante 
            case "SS":
              if "IM" not in typesProprietesEloignees:
                    propriete.valeur_courrante -= 0.5 * propriete.valeur_courrante  
            case "CM":
              if "TS" not in typesProprietesEloignees:
                    propriete.valeur_courrante -= 0.10 * propriete.valeur_courrante 