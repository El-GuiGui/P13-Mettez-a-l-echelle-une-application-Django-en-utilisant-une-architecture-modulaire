from django.shortcuts import render
from .models import Letting


def index(request):
    """
    Affiche la liste de tous les lettings.

    Args:
        request: L'objet de requête HTTP.

    Returns:
        HttpResponse: La page HTML affichant la liste des lettings.
    """
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """
    Affiche les détails d'un letting spécifique.

    Args:
        request: L'objet de requête HTTP.
        letting_id: L'identifiant du letting à afficher.

    Returns:
        HttpResponse: La page HTML affichant les détails d'un letting.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
