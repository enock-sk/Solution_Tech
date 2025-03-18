from django.shortcuts import render, redirect
from django.contrib import messages

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def services(request):
    return render(request, 'main/services.html')

def portfolio(request):
    return render(request, 'main/portfolio.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Simulate saving or sending (replace with real logic later)
        print(f"Contact: {name}, {email}, {message}")
        messages.success(request, "Thank you! Your message has been sent.")
        return redirect('contact')
    return render(request, 'main/contact.html')