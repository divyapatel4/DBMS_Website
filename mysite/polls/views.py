from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.contrib import messages
from . import check_funcs
from . import schema

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def login(request):
    if request.method == 'POST':
        User_ID = request.POST['User ID']
        Password = request.POST['Password']
        if check_funcs.CheckLogin(User_ID, Password)==True:
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
        tables = request.POST.getlist('table')
        print(tables, len(tables))
        Type_of_Query = request.POST.getlist('Type_of_Query')
        print(Type_of_Query, len(Type_of_Query))
        Args = request.POST.getlist('args')
        print(Args, len(Args))
        if check_funcs.CheckQuery(tables, Type_of_Query,Args)==True:    
            context = {'schema': schema.schema, 'args': tables}
            template = loader.get_template('polls/form1.html')   
            return HttpResponse(template.render(context, request))
        else:
            return HttpResponse('Invalid Query')
    else:
        context = {'foo': 'bar'}
        template = loader.get_template('polls/form.html')   
        return HttpResponse(template.render(context, request))

def get_args(request):
    print  ("Hello1")
    print("Hello2")
    context = {'foo': 'bar'}
    template = loader.get_template('polls/form1.html')   
    return HttpResponse(template.render(context, request))


def results(request):
    context = {'foo': 'bar'}
    template = loader.get_template('polls/table.html')
    return HttpResponse(template.render(context, request))