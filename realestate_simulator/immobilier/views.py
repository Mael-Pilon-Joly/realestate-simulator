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

def propriete_par_id(request, id):
    try:
      propriete = Propriete.get(id=id)
    except Propriete.DoesNotExist:
        raise Http404("Proprieté non trouvée")
    
def transactions(request):
    transactions = Transaction.objects.all()
    return JsonResponse(list(transactions), safe=True)

def transaction_par_id(request, id):
    try:
      transaction = Transaction.get(id=id)
    except Transaction.DoesNotExist:
        raise Http404("Transaction non trouvée")

def transactions_par_utilisateur(request, utilisateur_id):
    try:
        transactions = Transaction.objects.filter(utilisateur_id=utilisateur_id)
    except Transaction.DoesNotExist:
        raise Http404("Aucune transaction trouvée pour cet utilisateur")
    return JsonResponse(list(transactions.values()), safe=False)

def liste_habitants(request):
    habitants = Habitant.objects.all()
    return JsonResponse(list(habitants.values()), safe=False)

def habitants_par_propriete(request, propriete_id):
    try:
        habitants = Habitant.objects.filter(propriete_id=propriete_id)
    except Habitant.DoesNotExist:
        raise Http404("Aucun habitant trouvé pour cette propriété")
    return JsonResponse(list(habitants.values()), safe=False)