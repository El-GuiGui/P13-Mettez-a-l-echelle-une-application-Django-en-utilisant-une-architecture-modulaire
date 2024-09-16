from django.shortcuts import render


def index(request):
    """
    Affiche la page d'accueil du site.

    Args:
        request: L'objet de requête HTTP.

    Returns:
        HttpResponse: La page HTML de l'index du site.
    """
    return render(request, "index.html")
