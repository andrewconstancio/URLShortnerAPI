import datetime
import re
import uuid
from django.http import HttpResponse, JsonResponse
from .models import URL
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    print(request.GET.get("test"))
    return HttpResponse("<h1>Welcome to shurl3.xyz! (URL shortner API)</h1>")

@csrf_exempt
def createShortURL(request):
    if request.method == "POST" and "long_url" in request.GET:
        link = request.GET["long_url"]
        uid = str(uuid.uuid4())[:5]
        url = re.sub(r"https://", "", link)
        url = re.sub(r"http://", "", url)
        new_url = URL(url=url, slug=uid, date_created=datetime.datetime.now())
        new_url.save()
        rep = "www.shurl3.xyz/" + str(new_url.slug)
        return JsonResponse({"short_url" : rep}, status=200)
    else:
        return JsonResponse({"error" : "Invalid Request"}, status=400)

@csrf_exempt
def go(request, pk):
    try:
        url_details = URL.objects.get(slug=pk)
        return redirect("https://" + url_details.url)
    except:
        return JsonResponse({"error" : "Invalid Request"}, status=400)