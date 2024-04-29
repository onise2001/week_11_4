from django.urls import path
from .views import response

urlpatterns = [
    path("<str:operation>/<int:first_num>/<int:second_num>", response),
   
]
