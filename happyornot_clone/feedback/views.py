from django.shortcuts import render, redirect
from .models import Feedback

def feedback_form(request):
    if request.method == 'POST':
        user = request.POST['user']
        comment = request.POST['comment']
        rating_str = (request.POST['rating'])
        if rating_str and rating_str.isdigit():
            rating = int(rating_str)
        else:
            rating = 0
        Feedback.objects.create(user=user, comment=comment, rating=rating)
        # return redirect('feedback_results')
        return render(request, 'feedback/form.html', {'form_submitted':True})
    else:
        return render(request, 'feedback/form.html')

# def submit(request):
#     user = request.POST.getlist('user')

def feedback_results(request):
    feedback_counts = Feedback.objects.count()
    feedback_ratings = Feedback.objects.values('rating')
    return render(request, 'feedback/results.html', {'feedback_counts': feedback_counts, 'feedback_ratings': feedback_ratings})
