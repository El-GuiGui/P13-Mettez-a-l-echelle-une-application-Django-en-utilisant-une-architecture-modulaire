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


def custom_404_view(request, exception):
    """
    Affiche une page personnalisée pour les erreurs 404 (Page non trouvée).

    Args:
        request: L'objet de requête HTTP.
        exception: L'exception déclenchée par l'erreur 404.

    Returns:
        HttpResponse: La page HTML 404 personnalisée avec le statut HTTP 404.
    """
    return render(request, "404.html", status=404)


def custom_500_view(request):
    """
    Affiche une page personnalisée pour les erreurs 500 (Erreur interne du serveur).

    Args:
        request: L'objet de requête HTTP.

    Returns:
        HttpResponse: La page HTML 500 personnalisée avec le statut HTTP 500.
    """
    return render(request, "500.html", status=500)


def trigger_error(request):
    """
    Provoque une erreur serveur pour tester la page d'erreur 500.

    Args:
        request: L'objet de requête HTTP.

    Raises:
        ValueError: Erreur volontaire déclenchée pour simuler une erreur serveur.
    """
    raise ValueError("Erreur serveur pour tester la page 500")
