from typing import List
from immobilier.models import Propriete


def determiner_proprietes_proches(proprietes: List[Propriete], propriete_visee: Propriete, nombre_km):
    # Définir les bornes de la propriété visée
    startX = propriete_visee.position_x
    startY = propriete_visee.position_y
    endX = startX + propriete_visee.largeur
    endY = startY + propriete_visee.longueur

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

def determiner_valeur_ajustement_environment_proche(propriete: Propriete, listProprietes: List[Propriete]):
    typesProprietesAProximite = []
    
    for p in listProprietes:
        if p.type_propriete not in typesProprietesAProximite:
          typesProprietesAProximite.append(p.type_propriete)

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

