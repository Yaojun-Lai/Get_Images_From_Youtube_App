from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('enternumber/',views.display_enterNumberHtml),
    path('displayFinalNumber/', views.display_enterKeywordHtml),
    path('showfinalimage/', views.show_final_image)

]