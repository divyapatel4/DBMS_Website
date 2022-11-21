from django.db import models


class Visitor(models.Model):
    name = models.CharField(max_length=200)
    nation = models.CharField(max_length=200)
    citizen_id = models.IntegerField(primary_key=True)
    Gender = models.CharField(max_length=200)
    State = models.CharField(max_length=200)
    District = models.CharField(max_length=200)

    class Meta:
        managed = False
        unique_together = (('nation', 'citizen_id'),)
        db_table = 'wildlife_db\".\"visitor'


class animal(models.Model):
    animal_name = models.CharField(max_length=200, primary_key=True)
    species_name = models.ForeignKey(
        'polls.species_data', on_delete=models.DO_NOTHING)
    Sanctuary_ID = models.ForeignKey(
        'polls.wildlife_sanctuary', on_delete=models.DO_NOTHING)
    health = models.CharField(max_length=200)
    Age = models.IntegerField
    gender = models.CharField(max_length=200)
    # Foreign key is (Sanctuary_ID, species_name)

    class Meta:
        managed = False
        db_table = 'wildlife_db\".\"animal'



class Species_data(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    population = models.IntegerField
    trend = models.FloatField
    male_female_ration = models.FloatField
    Birth_rate = models.IntegerField
    life_expectancy = models.IntegerField
    Remarks = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'wildlife_db\".\"species_data'


class wildlife_sanctuary(models.Model):
    name = models.CharField(max_length=200)
    sanctuary_id = models.IntegerField(primary_key=True)
    state = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    budget = models.IntegerField
    type = models.CharField(max_length=200)
    weather = models.CharField(max_length=200)
    temparature = models.FloatField
    humidity = models.FloatField
    percipitation = models.FloatField
    wind_direction = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'wildlife_db\".\"wildlife_sanctuary'



class expenditure(models.Model):
    Item = models.CharField(max_length=200)
    Invoice_ID = models.CharField(max_length=200, primary_key=True)
    Quantity = models.IntegerField
    price = models.FloatField
    sanctuary_id = models.ForeignKey('wildlife_sanctuary', on_delete=models.DO_NOTHING,related_name='sanctuary_id_expenditure')
    Emp_ID = models.ForeignKey('polls.staff', on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wildlife_db\".\"expenditure'



class price_list(models.Model):
    Item = models.CharField(max_length=200, primary_key=True)
    rate = models.FloatField

    class Meta:
        managed = False
        db_table = 'public\".\"price_list'



class department(models.Model):
    department_name = models.CharField(max_length=200)
    department_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'public\".\"department'



class patient(models.Model):
    Animal_Name = models.CharField(max_length=200, primary_key=True)
    Species_Name = models.ForeignKey(
        'polls.species_data', on_delete=models.DO_NOTHING)
    Emp_ID = models.ForeignKey('polls.staff', on_delete=models.DO_NOTHING)
    Disease = models.CharField(max_length=200)
    History_of_illness = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'wildlife_db\".\"patient'



class staff(models.Model):
    name = models.CharField(max_length=200)
    emp_id = models.CharField(max_length=200, primary_key=True)
    sanctuary_id = models.ForeignKey(
        'polls.wildlife_sanctuary', on_delete=models.DO_NOTHING , related_name='sanctuary_id_staff')
    nation = models.CharField(max_length=200)
    State = models.CharField(max_length=200)
    District = models.CharField(max_length=200)
    City = models.CharField(max_length=200)
    Street = models.CharField(max_length=200)
    Block = models.IntegerField
    department_id = models.ForeignKey(
        'polls.department', on_delete=models.DO_NOTHING , related_name='department_id_staff')

    class Meta:
        managed = False
        db_table = 'wildlife_db\".\"staff'




class mobile_no(models.Model):
    emp_id = models.ForeignKey('polls.staff', on_delete=models.DO_NOTHING , related_name='emp_id_mobile_no')
    mobile_number = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'wildlife_db\".\"mobile_no'


class email_id(models.Model):
    email_id = models.CharField(max_length=200, primary_key=True)
    emp_id = models.ForeignKey('polls.staff', on_delete=models.DO_NOTHING , related_name='emp_id_email_id')

    class Meta:
        managed = False
        db_table = 'wildlife_db\".\"email_id'


class sighted(models.Model):
    Date = models.DateField
    Time = models.TimeField
    # Citizen ID and Nation are the primary key of the visitor table and foreign key of the sighted table
    Nation = models.ForeignKey('polls.visitor', on_delete=models.DO_NOTHING , related_name='nation_sighted')
    Citizen_ID = models.ForeignKey(
        'polls.visitor', on_delete=models.DO_NOTHING)
    Animal_Name = models.ForeignKey(
        'polls.animal', on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        unique_together = (('Nation', 'Citizen_ID', 'Animal_Name'),)
        db_table = 'wildlife_db\".\"sighted'


class visited(models.Model):
    date = models.DateField
    nation = models.ForeignKey('polls.visitor', on_delete=models.DO_NOTHING , related_name='nation_visited')
    citizen_id = models.ForeignKey(
        'polls.visitor', on_delete=models.DO_NOTHING)
    sanctuary_id = models.ForeignKey(
        'polls.wildlife_sanctuary', on_delete=models.DO_NOTHING , related_name='sanctuary_id_visited')

    class Meta:
        managed = False
        unique_together = (('citizen_id', 'nation', 'sanctuary_id'),)
        db_table = 'wildlife_db\".\"visited'


class preys_upon(models.Model):
    pred_species = models.ForeignKey(
        'polls.species_data', on_delete=models.DO_NOTHING , related_name='pred_species_preys_upon')
    prey_species = models.ForeignKey(
        'polls.species_data', on_delete=models.DO_NOTHING , related_name='prey_species_preys_upon')

    class Meta:
        managed = False
        unique_together = (('pred_species', 'prey_species'),)
        db_table = 'wildlife_db\".\"preys_upon'
