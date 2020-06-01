from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
def index(request):

        context = {
            'name':'Example Name',
            'description': 'Example Description'
        }

        return render(request, "index.html", context)

