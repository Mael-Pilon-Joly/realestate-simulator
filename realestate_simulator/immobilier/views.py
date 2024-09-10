from django.shortcuts import render
from django.http import Http404, JsonResponse
from .models import Utilisateur, Propriete, Transaction, Habitant

# Create your views here.

def liste_utilisateur(request):
    utilisateurs = Utilisateur.objects.all()
    return JsonResponse(list(liste_utilisateur), safe=True)

def utilisateur_par_email(request, email):
    try:
        utilisateur = Utilisateur.get(email=email)
    except Utilisateur.DoesNotExist:
        raise Http404("Utilisateur non trouvé")
    return JsonResponse(utilisateur)

def liste_propriete(request):
    proprietes = Propriete.objects.all()
    return JsonResponse(list(proprietes), safe=True)