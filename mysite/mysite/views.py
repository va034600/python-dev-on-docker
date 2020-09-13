from django.http import HttpResponse


def index(request):
    v = 1
    return HttpResponse(f"hello{v}")
