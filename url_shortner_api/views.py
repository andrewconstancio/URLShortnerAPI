import uuid
from django.http import HttpResponse

from .models import URL
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    return HttpResponse("HELLLLLO")

@csrf_exempt
def createShortURL(request, link):
    if request.method == "POST":
        url = link
        uid = str(uuid.uuid4())[:5]
        new_url = URL(url=url, slug=uid)
        new_url.save()
        rep = "www.shurl3.xyz/" + str(new_url.slug)
        return HttpResponse(rep)

@csrf_exempt
def go(request, pk):
    url_details = URL.objects.get(slug=pk)
    return redirect("https://" + url_details.url)