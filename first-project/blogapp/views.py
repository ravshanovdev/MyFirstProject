from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def kirmaview(request):
    return HttpResponse('Assalomu alaykum')
def about(request):
    return HttpResponse('karochi hozir malumot yoq.')
