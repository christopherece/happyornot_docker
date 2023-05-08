from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import FeedbackForm
from .models import Feedback
import json



def feedback_form(request):
    return render(request, 'feedback/form.html')

@csrf_exempt
def save_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                 'success': True,
                 'success_message': 'Feedback saved successfully!',
                 'success_image': '/static/img/thumbsup.gif',
                 'success_class': 'alert alert-success',
                 
             }
            return JsonResponse(context)
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = FeedbackForm()
    return render(request, 'feedback/form.html', {'form': form})


# def save_feedback(request):
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             form.save()
#             context = {
#                 'success': True,
#                 'success_message': 'Feedback saved successfully!',
#                 'success_image': '/static/img/thumbsup.gif',
#             }
#         else:
#             context = {
#                 'form': form,
#             }
#     else:
#         context = {
#             'form': FeedbackForm(),
#         }

#     return render(request, 'feedback/form.html', context)

def feedback_results(request):
    feedback_counts = Feedback.objects.count()
    feedback_ratings = Feedback.objects.values('rating')
    return render(request, 'feedback/form.html', {'feedback_counts': feedback_counts, 'feedback_ratings': feedback_ratings, 'form_submitted':True})
