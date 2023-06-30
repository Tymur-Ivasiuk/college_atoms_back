import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def subscribers(request):
    url = "https://script.google.com/macros/s/AKfycbwvaVas2ZEQejU3Cqd7E23uwim7I7puLvf6MFJXJWcgA9V05Ot7APQssMLy2ueWyq8R/exec"

    data = dict(request.POST)
    data['password'] = '1234'

    r = requests.post(url, data=data)
    print(data, r.text)
    return JsonResponse(r.json())
