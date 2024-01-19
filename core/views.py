from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import HttpResponse
from django.template import loader

def index(request):

    context = {
        # 'curso': 'Programação Web com Django Framework',
    }
    return render(request, 'index.html', context)