from django.utils import translation


# Função para manipular o context de todas as views
def my_context(request):
    html_language = translation.get_language()
    return {
        'html_language': html_language,
    }
