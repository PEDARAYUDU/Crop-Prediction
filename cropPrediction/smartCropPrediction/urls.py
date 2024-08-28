from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("predictionform/",views.predict, name= "predictionform"),
    path('prediction_crop/', views.prediction_crop, name='prediction_crop'),
    # path("prediction_factor/",views.prediction_factor,name="prediction_factor"),
    path('demo/',views.demo, name='demo'),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('result/',views.result,name="resut"),
    
    
]