from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader

from .models import JoueurTennis

def members(request):
  mesJoueurs = JoueurTennis.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mesJoueurs': mesJoueurs,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  monJoueur = JoueurTennis.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'monJoueur': monJoueur,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  mydata = JoueurTennis.objects.all()
  template =loader.get_template('testing.html')
  context = {
    'mesJoueurs': mydata,
  }
  return HttpResponse(template.render(context, request))

#def members(request):
#  template = loader.get_template('first.html')
#  return HttpResponse(template.render())

#def members(request):
#    return HttpResponse("Hello world!")
