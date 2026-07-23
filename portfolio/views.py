from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, ContactMessage


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        if name and email and message:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            messages.success(request, 'Thank you! Your message has been sent successfully.')
            return redirect('portfolio:index')
        else:
            messages.error(request, 'Please fill in all required fields.')

    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'portfolio/index.html', context)
