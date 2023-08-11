from django.shortcuts import render

def index(request):
    return render(request, "main/index.html")

def home(request):
    return render(request, "main/home.html")

def news(request):
    return render(request, "main/news.html")

def ai_gen(request):
    return render(request, "main/ai_gen.html")

def three_d_room(request):
    return render(request, "main/3d_room.html")

def honors(request):
    return render(request, "main/honors.html")