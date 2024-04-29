from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def response(request, operation, first_num, second_num):
    if operation == "add":
       return render(request, "calculator/math.html", {"expression": f"{first_num} + {second_num} = {first_num + second_num}"})
       
    
    elif operation == "sub":
       return render(request, "calculator/math.html", {"expression": f"{first_num} - {second_num} = {first_num - second_num}"})
    
    elif operation == "multi":
       return render(request, "calculator/math.html", {"expression": f"{first_num} * {second_num} = {first_num * second_num}"})
    
    elif operation == "div":
       return render(request, "calculator/math.html", {"expression": f"{first_num} / {second_num} = {first_num / second_num}"})


