import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from feedback.models import Feedback
from speaker.models import Speaker
from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt




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
        return render(request, 'accounts/dashboard.html')

@login_required(login_url='login')
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now Logged Out!')
    return redirect(request, 'accounts/login.html')

@login_required(login_url='login')
def dashboard(request):

    return render(request, 'accounts/dashboard.html')

@login_required(login_url='login')
def feedback_count(request):
    ratings = ['Excellent', 'Good', 'Average', 'Poor', 'Bad']
    data = []
    for rating in ratings:
        feedbacks = Feedback.objects.filter(rating=rating)
        count = feedbacks.count()
        
        data.append({'rating': rating, 'total': count})

    return JsonResponse(data, safe=False)

@login_required(login_url='login')
def feedback_detail(request):
    speaker = request.GET.get('speaker', '')
    comment = request.GET.get('comment', '')
    rating = request.GET.get('rating', '')
    feedback_date = request.GET.get('date', '')

    context = {
        'speaker': speaker,
        'comment': comment,
        'rating': rating,
        'feedback_date': feedback_date
    }
    return render(request, 'feedback_detail.html', context)

@login_required(login_url='login')
def excellent_feedback(request):
    print(request)
    feedbacks = Feedback.objects.filter(rating='Excellent')
    return render(request, 'accounts/excellent_feedback.html', {'feedbacks': feedbacks})

@login_required(login_url='login')
def good_feedback(request):
    feedbacks = Feedback.objects.filter(rating='Good')
    return render(request, 'accounts/good_feedback.html', {'feedbacks': feedbacks})

@login_required(login_url='login')
def average_feedback(request):
    feedbacks = Feedback.objects.filter(rating='Average')
    return render(request, 'accounts/average_feedback.html', {'feedbacks': feedbacks})

@login_required(login_url='login')
def poor_feedback(request):
    feedbacks = Feedback.objects.filter(rating='Poor')
    return render(request, 'accounts/poor_feedback.html', {'feedbacks': feedbacks})

@login_required(login_url='login')
def bad_feedback(request):
    feedbacks = Feedback.objects.filter(rating='Bad')
    return render(request, 'accounts/bad_feedback.html', {'feedbacks': feedbacks})