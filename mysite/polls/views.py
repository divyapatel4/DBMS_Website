from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.contrib import messages
from . import check_funcs
from . import schema
from polls.models import *
# OG View



def comp(inp1, inp2, op):
    if op=='l' and inp1<inp2:
        return True
    elif op =='l' and inp1>=inp2:
        return False
    elif op=='g' and inp1>inp2:
        return True
    elif op=='g' and inp1<=inp2:
        return False
    elif op=='e' and inp1==inp2:
        return True
    elif op=='e' and inp1!=inp2:
        return False
    
    

# DBMS_Website/mysite/polls/models.py

def index(request):
    return render(request, 'polls/index.html', {"foo": "bar"})  


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
                if Type_of_Query[0] == "View":
                    if tables[0] == "visitor":
                        showall = Visitor.objects.all()
                        return render(request, 'polls/Visitor.html', {"data": showall})
                    elif tables[0] == "animal":
                        showall = Animal.objects.all()
                        return render(request, 'polls/animal.html', {"data": showall})
                    elif tables[0] == "species_data":
                        showall = SpeciesData.objects.all()
                        return render(request, 'polls/SpeciesData.html', {"data": showall})
                    elif tables[0] == "wildlife_sanctuary":
                        showall = WildlifeSanctuary.objects.all()
                        return render(request, 'polls/wildlifesanctuary.html', {"data": showall})
                    elif tables[0] == "expenditure":
                        showall = Expenditure.objects.all()
                        return render(request, 'polls/Expenditure.html', {"data": showall})
                    elif tables[0] == '"Price_List"':
                        showall = PriceList.objects.all()
                        return render(request, 'polls/PriceList.html', {"data": showall})
                    elif tables[0] == '"Department"':
                        showall = Department.objects.all()
                        return render(request, 'polls/department.html', {"data": showall})
                    elif tables[0] == 'patient':
                        showall = Patient.objects.all()
                        return render(request, 'polls/patient.html', {"data": showall})
                    elif tables[0] == 'staff':
                        showall = Staff.objects.all()
                        return render(request, 'polls/staff.html', {"data": showall})
                    elif tables[0] == '"Mobile_Number"':
                        showall = MobileNo.objects.all()
                        return render(request, 'polls/mobile_no.html', {"data": showall})
                    elif tables[0] == 'sighted':
                        showall = Sighted.objects.all()
                        return render(request, 'polls/sighted.html', {"data": showall})
                    elif tables[0] == 'visited':
                        showall = Visited.objects.all()
                        return render(request, 'polls/visited.html', {"data": showall})
                    else:
                        #prey_upon
                        showall = PreysUpon.objects.all()
                        return render(request, 'polls/preys_upon.html', {"data": showall})
                else:
                    context = {'schema': schema.schema, 'args': tables}
                    template = loader.get_template('polls/form1.html')
                    return HttpResponse(template.render(context, request))
            else:
                return HttpResponse('Invalid Query')
        else:
            print(request.POST)
            if (request.POST.getlist('tables')[0] == 'animal'):
                InsertAnimal(request)
                return HttpResponse("Inserted")
            elif (request.POST.getlist('tables')[0] == 'visitor'):
                InsertVisitor(request)
                return HttpResponse("Inserted")
            else:
                return HttpResponse("Cannot Insert in this table")  
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


def InsertAnimal(request):
    print("Inside")
    if request.method == 'POST':
        print("Inside")
        # Print value at Animal_name key in form
        print(request.POST.get('animal.animal_name.val'))
        print(request.POST.get('animal.species_name.val'))

        if request.POST.get('animal.animal_name.val') and request.POST.get('animal.species_name.val') and request.POST.get('animal."Sanctuary_ID".val') and request.POST.get('animal."Health".val') and request.POST.get('animal."Age".val') and request.POST.get('animal."Gender".val'):
            print("Inside")
            animal = Animal()
            animal.animal_name = request.POST.get('animal.animal_name.val')
            animal.species_name = SpeciesData.objects.get(name=request.POST.get('animal.species_name.val'))
            animal.sanctuary = WildlifeSanctuary.objects.get(sanctuary_id=request.POST.get('animal."Sanctuary_ID".val'))
            animal.health = request.POST.get('animal."Health".val')
            animal.Age = request.POST.get('animal."Age".val')
            animal.gender = request.POST.get('animal."Gender".val')
            animal.save()
            mess = "Animal Inserted"
            return render(request, 'polls/form.html', {"mess": mess})
        else:
            return HttpResponse("Invalid Insert")


def InsertVisitor(request):
    if request.method == 'POST':
        if request.POST.get('visitor.citizen_id.val') and request.POST.get('visitor.name.val') and request.POST.get('visitor.nation.val') and request.POST.get('visitor."Gender".val') and request.POST.get('visitor."State".val') and request.POST.get('visitor."District".val') :
            visitor = Visitor()
            visitor.citizen_id = request.POST.get('visitor.citizen_id.val')
            visitor.name = request.POST.get('visitor.name.val')
            visitor.nation = request.POST.get('visitor.nation.val')
            visitor.district = request.POST.get('visitor."District".val')
            visitor.gender = request.POST.get('visitor."Gender".val')
            visitor.state = request.POST.get('visitor."State".val')
            visitor.save()
            mess = "Visitor Inserted"
            return render(request, 'polls/form.html', {"mess": mess})
        else:
            return HttpResponse("Invalid Insert")
        