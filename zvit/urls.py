from django.urls import path

from zvit.views import *
from zvit.viewsApi import *

urlpatterns = [
    path('', ZvitView.as_view(), name='zvit'),
    path('score', ScoreView.as_view(), name='score'),
]