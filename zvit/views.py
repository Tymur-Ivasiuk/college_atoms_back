from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import *

from zvit.forms import *
from zvit.utils import *


class ZvitView(FormView):
    template_name = 'zvit/zvit.html'
    form_class = ZvitForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(f'context - {context}')
        return context

    def post(self, request, *args, **kwargs):
        form = ZvitForm(request.POST)
        if form.is_valid():
            new_doc_url = create_zvit(title=request.POST['title'], date=request.POST['date'], executor=request.POST['executor'])
            messages.success(request, new_doc_url)
        else:
            messages.error(request, "Error")

        return redirect(request.path)


def getScore():
    url = 'https://script.google.com/macros/s/AKfycbzKn9Kztv3Xr_2F8k2_HW9v4exCkEU7pqieLmqgoGCCHOgoUM3y6UWo9L1uaYwfVIrg/exec'
    data = {
        "password": "1234",
        "actionType": "GET-STUDENTS-NAME",
        "groupName": "31-КН",
    }
    response = requests.get(url, data)
    return response.text

class ScoreView(TemplateView):
    template_name = 'zvit/score.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['response'] = getScore()
        return context
# def ZvitView(request):
#     return HttpResponse("<h1>HTREWJ</h1>")