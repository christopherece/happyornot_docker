from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from feedback.models import Feedback
from django.db.models import Count


# Create your views here.
def register(request):
    return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now login!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials! Try Again!')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    return redirect(request, 'feedback.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def feedback_count(request):
    feedback_counts = Feedback.objects.values('rating').annotate(total=Count('rating')).order_by('rating')
    return JsonResponse(list(feedback_counts), safe=False)

def excellent_feedback(request):
    return render(request, 'accounts/excellent_feedback.html')
