from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from .wholeProcess import whole_process
from .getImages import get_Images
# Create your views here.
def say_hello(request):
    return render(request, 'hello.html', {'name':'Mosh'})

def display_enterNumberHtml(request):
    return render(request, 'enterNumber.html')

@csrf_exempt
def display_enterKeywordHtml(request):
    text_value = request.POST.get('text-input')
    whole_process(text_value)
    return render(request, 'enterKeyword.html')

@csrf_exempt
def show_final_image(request):
    text_value = request.POST.get('text-input')
    get_Images(text_value)
    return render(request, 'displayImage.html')
    # return render(request, 'displayFinalNumber.html')