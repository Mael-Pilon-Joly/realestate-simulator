from typing import List
from immobilier.models import Propriete

class IService:
    
    def recuperer_tous_les_proprietes():
        return Propriete.objects.all()
    
    @staticmethod
    def determiner_proprietes_proches(proprietes: List[Propriete], entitee_visee, nombre_km):
        startX = entitee_visee.position_x
        startY = entitee_visee.position_y
        endX = startX + entitee_visee.largeur
        endY = startY + entitee_visee.longueur

        proprietes_proches = []

        for p in proprietes:
            pStartX = p.position_x - 1000 * nombre_km
            pStartY = p.position_y - 1000 * nombre_km 
            pEndX = pStartX + p.largeur + 2000 * nombre_km
            pEndY = pStartY + p.longueur + 2000 * nombre_km

            if (startX <= pEndX and endX >= pStartX) and (startY <= pEndY and endY >= pStartY):
                proprietes_proches.append(p)
        
        return proprietes_proches   
    
    @staticmethod
    def determiner_type_proprietes_dans_perimetre(proprietes: List[Propriete]):
        listProprietesDansPerimetre = []

        for p in proprietes:
            if p.type_propriete not in listProprietesDansPerimetre:
                listProprietesDansPerimetre.append(p.type_propriete)

        return listProprietesDansPerimetre
    
    @staticmethod
    def determine_proprietes_dans_perimetre(proprietes: List[Propriete]) -> List[Propriete]:
        listProprietesDansPerimetre = []

        for p in proprietes:
            if p.type_propriete not in listProprietesDansPerimetre:
                listProprietesDansPerimetre.append(p)

        return listProprietesDansPerimetre
