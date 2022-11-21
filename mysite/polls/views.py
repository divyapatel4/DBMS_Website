from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.contrib import messages
from . import check_funcs
from . import schema
from polls.models import Animal



# DBMS_Website/mysite/polls/models.py

def index(request):
    showall =Animal.objects.all()
    # print(showall)
    return render(request, 'polls/index.html', {"data": showall})


def login(request):
    if request.method == 'POST':
        User_ID = request.POST['User ID']
        Password = request.POST['Password']
        if check_funcs.CheckLogin(User_ID, Password) == True:
            return HttpResponseRedirect('form')
        else:
            return HttpResponse("Invalid Login Credentials")
    else:
        context = {'foo': 'bar'}
        template = loader.get_template('polls/login.html')
        return HttpResponse(template.render(context, request))


def form(request):
    if request.method == 'POST':
        print(request.POST)
        if request.POST.getlist('submit')[0] == 'Submit':
            tables = request.POST.getlist('table')
            print(tables, len(tables))
            Type_of_Query = request.POST.getlist('Type_of_Query')
            print(Type_of_Query, len(Type_of_Query))
            Args = request.POST.getlist('args')
            print(Args, len(Args))
            if check_funcs.CheckQuery(tables, Type_of_Query, Args) == True:
                context = {'schema': schema.schema, 'args': tables}
                template = loader.get_template('polls/form1.html')
                return HttpResponse(template.render(context, request))
            else:
                return HttpResponse('Invalid Query')
        else:
            print(request.POST)
            return HttpResponse("Hello")
    else:
        context = {'foo': 'bar'}
        template = loader.get_template('polls/form.html')
        return HttpResponse(template.render(context, request))


def get_args(request):
    print("Hello1")
    print("Hello2")
    context = {'foo': 'bar'}
    template = loader.get_template('polls/form1.html')
    return HttpResponse(template.render(context, request))


def results(request):
    context = {'foo': 'bar'}
    template = loader.get_template('polls/table.html')
    return HttpResponse(template.render(context, request))


# def InsertAnimal(request):
#     if request.method == 'POST':
#         if request.POST.get('animal_name') and request.POST.get('species_name') and request.POST.get('Sanctuary_ID') and request.POST.get('Health') and request.POST.get('Age') and request.POST.get('Gender'):
#             animal = Animal()
#             animal.animal_name = request.POST.get('animal_name')
#             animal.species_name = request.POST.get('species_name')
#             animal.Sanctuary_ID = request.POST.get('Sanctuary_ID')
#             animal.Health = request.POST.get('Health')
#             animal.Age = request.POST.get('Age')
#             animal.Gender = request.POST.get('Gender')
#             animal.save()
#             return render(request, 'polls/insert.html')
#         else:
#             return HttpResponse("Invalid Insert")
#     else:
#         return render(request, 'polls/insert.html')
