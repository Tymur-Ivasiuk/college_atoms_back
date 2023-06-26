import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def subscribers(request):
    url = "https://script.google.com/macros/s/AKfycbz28vJX12t_YhijaRkqaBz_KSGoUIXCnY4zGGVXRgCEGHBI5-qS5Pins5iNVTit9p8O/exec"

    data = dict(request.POST)
    data['password'] = '1234'

    r = requests.post(url, data=data)
    print(data, r.text)
    return JsonResponse(r.json())
