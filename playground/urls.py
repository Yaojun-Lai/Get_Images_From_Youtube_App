from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('downloadVideo/',views.display_downloadVideoHtml),
    path('displayFinalNumber/', views.display_enterKeywordHtml),
    path('showfinalimage/', views.show_final_image)

]