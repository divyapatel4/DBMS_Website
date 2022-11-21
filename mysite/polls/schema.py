schema = {
    'wildlife_sanctuary': ['name', 'sanctuary_id', 'state', 'district', 'budget', 'type', 'weather', 'temperature', 'humidity', 'percipitation', 'wind_direction'],
    'species_data': ['name','population','trend', 'male_female_ration', '"Birth_rate"', 'life_expectancy', "Remarks"],
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