from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome):
    return HttpResponse('<h1>Vai Corinthians. Seja bem vindo {} </h1>' .format(nome))