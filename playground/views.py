from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from .wholeProcess import whole_process
from .getImages import get_Images
# Create your views here.
def say_hello(request):
    return render(request, 'displayFinalNumber.html')

def display_downloadVideoHtml(request):
    return render(request, 'downloadVideo.html')

@csrf_exempt
def display_enterKeywordHtml(request):
    text_value = request.POST.get('text-input')
    title, description = whole_process(text_value)
    return render(request, 'enterKeyword.html', {'title':title, 'description':description})

@csrf_exempt
def show_final_image(request):
    text_value = request.POST.get('text-input')
    final_sims, imageNames = get_Images(text_value)
    return render(request, 'displayImage.html', {'final_sims': final_sims, 'imageNames': imageNames})
    # return render(request, 'displayFinalNumber.html')