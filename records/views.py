from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Question, Candidate

# Create your views here.
#parameter argument 'request' => HttpRequest object
def index(request):
    qlist = Question.objects.all()
    
    #output = ', '.join([q.question_text for q in qlist])
    context = {'question_list': qlist }
    return render(request, 'records/index.html', context)

    #return HttpResponse("have you ever voted and aked yourself: Who is this person? Or What is there stance on... ?")
    #return HttpResponse(output)

def candInfo(request, candidate_id):
    try:
        candidate = Candidate.objects.get(pk=candidate_id)
        #response = "Viewing the candidate info for %s." % candidate_id
    except Candidate.DoesNotExist:
        raise Http404("Candidate does not exist in our database")

    #return HttpResponse(response)
    return  render(request, 'records/candidate.html', {'candidate': candidate})
def results(request, response_id):
    return HttpResponse("Viewing response %s." % response_id)


