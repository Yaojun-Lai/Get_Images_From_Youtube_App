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
    keywords = request.POST.get('text-input')
    k = int(request.POST.get('text-input2'))
    image_file = request.FILES.get('image-input')
    final_sims, imageNames = get_Images(k, keywords, image_file)
    image_data = zip(final_sims, imageNames)
    return render(request, 'displayImage.html', {'image_data': image_data})
    # return render(request, 'displayFinalNumber.html')