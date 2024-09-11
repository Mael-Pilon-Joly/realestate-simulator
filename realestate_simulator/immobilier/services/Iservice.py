from typing import List, TypeVar

from realestate_simulator.immobilier.models import Propriete


class IService:
  
  def recuperer_tous_les_proprietes():
    return Propriete.objects.all()
  
  def determiner_proprietes_proches(proprietes: List[Propriete], entitee_visee, nombre_km):
    # Définir les bornes de la propriété visée
    startX = entitee_visee.position_x
    startY = entitee_visee.position_y
    endX = startX + entitee_visee.largeur
    endY = startY + entitee_visee.longueur

    # Liste des propriétés proches qui overlap
    proprietes_proches = []

    for p in proprietes:
        # Définir les bornes de la propriété actuelle
        pStartX = p.position_x - 1000 * nombre_km  # n km de marge de chaque côté
        pStartY = p.position_y - 1000 * nombre_km 
        pEndX = pStartX + p.largeur + 2000 * nombre_km
        pEndY = pStartY + p.longueur + 2000 * nombre_km

        # Vérifier s'il y a un chevauchement
        if (startX <= pEndX and endX >= pStartX) and (startY <= pEndY and endY >= pStartY):
            proprietes_proches.append(p)
    
    return proprietes_proches   
  
  T = TypeVar('T')
  
  def determiner_propriete_dans_perimetre(proprietes: List[Propriete]):
     listProprietesDansPerimetre = []

     for p in proprietes:
            if p.type_propriete not in listProprietesDansPerimetre :
              listProprietesDansPerimetre.append(p.type_propriete)

     return listProprietesDansPerimetre