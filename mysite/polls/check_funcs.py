# from schema import schema

schema = {
    'wildlife_sanctuary': ['name', 'sanctuary_id', 'state', 'district', 'budget', 'type', 'weather', 'temperature', 'humidity', 'percipitation', 'wind_direction'],
    'species_data': ['name', 'population', 'trend', 'male_female_ration', '"Birth_rate"', 'life_expectancy', "Remarks"],
    'visitor': ['name', 'nation', 'citizen_id', '"Gender"', '"State"', '"District"'],
    'animal': ['animal_name', 'species_name', '"Sanctuary_ID"', '"Health"', '"Age"', '"Gender"'],
    'expenditure': ['"Item"', '"Invoice_ID"', '"Quantity"', 'price', 'sanctuary_id', '"Emp_ID"'],
    '"Price_List"': ['"Item"', '"Rate"'],
    '"Department"': ['"Department_Name"', '"Department_ID"'],
    'patient': ['"Animal_Name"', '"Species_Name"', '"Emp_ID"', '"Disease"', '"History_of_illness"'],
    'staff': ['name', 'emp_id', 'sanctuary_id', 'nation', '"State"', '"District"', '"City"', '"Street"', '"Block"', 'department_id'],
    '"Mobile_Number"': ['"Emp_ID"', '"Mobile_No"'],
    '"Email_ID"': ['"Emp_ID"', '"Email_ID"'],
    'sighted': ['"Date"', '"Time"', '"Nation"', '"Citizen_ID"', '"Animal_Name"'],
    'visited': ['date', 'nation', 'ciizen_id', 'sanctuary_id'],
    'prey_upon': ['pred_species', 'prey_species']
}

def CheckLogin(User_ID, Password):
    if User_ID == 'admin' and Password == 'admin':
        return True
    else:
        return False

def CheckQuery(table, Type_of_Query, Args):
    if len(table) == 0: return False
    if len(Type_of_Query)==1:
        if Type_of_Query[0]=='Insert':
            if len(table)==1:
                return True
            else:
                return False
        elif Type_of_Query[0]=='Delete':
            if len(table)==1:
                return True
            else:
                return False
        else:
            if len(table) == 1:
                return True
            else:
                return False
    else:
        return False
    
# def get_data(Arg_dict):
#     tables = Arg_dict.getlist('table')
    
#     for table in tables:
    
    