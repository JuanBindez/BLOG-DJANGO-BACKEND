from django.http import HttpResponse

def teste_django(request):
    return HttpResponse("teste django ok!")