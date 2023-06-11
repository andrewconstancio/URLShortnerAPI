import re
import uuid
from django.http import HttpResponse, JsonResponse

from .models import URL
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    return HttpResponse("<h1>Welcome to shurl3.xyz! (URL shortner API)</h1>")

@csrf_exempt
def createShortURL(request, link):
    if request.method == "POST":
        uid = str(uuid.uuid4())[:5]
        url = re.sub(r"https://", "", link)
        url = re.sub(r"http://", "", url)
        new_url = URL(url=url, slug=uid)
        new_url.save()
        rep = "www.shurl3.xyz/" + str(new_url.slug)
        return JsonResponse({"short_url" : rep})
    else:
        return JsonResponse({"error" : "Invalid Request"})

@csrf_exempt
def go(request, pk):
    try:
        url_details = URL.objects.get(slug=pk)
        return redirect("https://" + url_details.url)
    except:
        return JsonResponse({"error" : "Invalid Request"})