from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello Home")
def contact(request):
    return HttpResponse("Hello contact")