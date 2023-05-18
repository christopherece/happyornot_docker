from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import FeedbackForm
from .models import Feedback
from speaker.models import Speaker
from trainingtitle.models import Trainingtitle
import json




def feedback_form(request):
    speakers = Speaker.objects.all()
    trainingtitles = Trainingtitle.objects.all()

    context = {
        'speakers': speakers,
        'trainingtitles': trainingtitles
    }
    return render(request, 'feedback/form.html', context)

def speaker_training_dropdown(request):
    speakers = Speaker.objects.all()
    training_titles = Trainingtitle.objects.all()
    context = {'speakers': speakers, 'training_titles': training_titles}
    return render(request, 'speaker_training_dropdown.html', context)

def get_training_titles(request):
    speaker_id = request.GET.get('speaker_id')
    print(speaker_id)
    training_titles = Trainingtitle.objects.filter(speaker_id=speaker_id).order_by('title')
    print(training_titles)
    training_title_list = [{'id': title.id, 'title': title.title} for title in training_titles]
    return JsonResponse(training_title_list, safe=False)

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
