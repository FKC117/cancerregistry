from django.http import JsonResponse


def index(request):
    return JsonResponse({"service": "National Cancer Registry", "status": "ok"})
