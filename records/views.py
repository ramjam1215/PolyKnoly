from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect , Http404


from .models import Question, Candidate

# Create your views here.
#parameter argument 'request' => HttpRequest object
# https://docs.djangoproject.com/en/3.0/topics/forms/
def index(request):
    qlist = Question.objects.all()
    
    #output = ', '.join([q.question_text for q in qlist])

    #The context is a dictionary mapping template variable names to Python objects.
    context = {'question_list': qlist }
    return render(request, 'records/index.html', context)

    #return HttpResponse("have you ever voted and aked yourself: Who is this person? Or What is there stance on... ?")
    #return HttpResponse(output)

def candInfo(request, candidate_id):
    try:
        # calls model Manager to access the db
        candidate = Candidate.objects.get(pk=candidate_id)
        #response = "Viewing the candidate info for %s." % candidate_id
    except Candidate.DoesNotExist:
        raise Http404("Candidate does not exist in our database")

    #return HttpResponse(response)
    return  render(request, 'records/candidate.html', {'candidate': candidate})

def results(request, response_id):
    return HttpResponse("Viewing response %s." % response_id)

#def details(request):
    #return render(request, 'records/details.html')

def inputCand(request):
    return render(request, 'records/inCand.html')

# here we will add to db via save()
def addData(request):

    #In an HttpRequest object, the GET and POST attributes are instances of django.http.QueryDict,
        # a dictionary-like class customized to deal with multiple values for the same key. 
        # This is necessary because some HTML form elements, notably <select multiple>, pass multiple values for the same key.
        # The QueryDicts at request.POST and request.GET will be immutable when accessed in a normal request/response cycle.
        # To get a mutable version you need to use QueryDict.copy().
    if request.method == 'POST':
        q = request.POST
        print("Posted data....")
        print(q.items)

    return HttpResponse("<p>We got to addData</p>")
