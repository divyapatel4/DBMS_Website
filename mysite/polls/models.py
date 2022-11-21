from django.db import models


# class Visitor(models.Model):
#     name = models.CharField(max_length=200)
#     nation = models.CharField(max_length=200)
#     citizen_id = models.IntegerField(primary_key=True)
#     Gender = models.CharField(max_length=200)
#     State = models.CharField(max_length=200)
#     District = models.CharField(max_length=200)

#     class Meta:
#         managed = False
#         unique_together = (('nation', 'citizen_id'),)
#         db_table = 'visitor'


# class animal(models.Model):
#     animal_name = models.CharField(max_length=200, primary_key=True)
#     species_name = models.ForeignKey(
#         'polls.species_data', on_delete=models.DO_NOTHING)
#     Sanctuary_ID = models.ForeignKey(
#         'polls.wildlife_sanctuary', on_delete=models.DO_NOTHING)
#     health = models.CharField(max_length=200)
#     Age = models.IntegerField
#     gender = models.CharField(max_length=200)
#     # Foreign key is (Sanctuary_ID, species_name)

#     class Meta:
#         managed = False
#         db_table = 'animal'



# class Species_data(models.Model):
#     name = models.CharField(max_length=200, primary_key=True)
#     population = models.IntegerField
#     trend = models.FloatField
#     male_female_ration = models.FloatField
#     Birth_rate = models.IntegerField
#     life_expectancy = models.IntegerField
#     Remarks = models.CharField(max_length=200)

#     class Meta:
#         managed = False
#         db_table = 'species_data'


# class wildlife_sanctuary(models.Model):
#     name = models.CharField(max_length=200)
#     sanctuary_id = models.IntegerField(primary_key=True)
#     state = models.CharField(max_length=200)
#     district = models.CharField(max_length=200)
#     budget = models.IntegerField
#     type = models.CharField(max_length=200)
#     weather = models.CharField(max_length=200)
#     temparature = models.FloatField
#     humidity = models.FloatField
#     percipitation = models.FloatField
#     wind_direction = models.CharField(max_length=200)

#     class Meta:
#         managed = False
#         db_table = 'wildlife_sanctuary'



# class expenditure(models.Model):
#     Item = models.CharField(max_length=200)
#     Invoice_ID = models.CharField(max_length=200, primary_key=True)
#     Quantity = models.IntegerField
#     price = models.FloatField
#     sanctuary_id = models.ForeignKey('wildlife_sanctuary', on_delete=models.DO_NOTHING,related_name='sanctuary_id_expenditure')
#     Emp_ID = models.ForeignKey('polls.staff', on_delete=models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'expenditure'



# class price_list(models.Model):
#     Item = models.CharField(max_length=200, primary_key=True)
#     rate = models.FloatField

#     class Meta:
#         managed = False
#         db_table = 'public\".\"price_list'



# class department(models.Model):
#     department_name = models.CharField(max_length=200)
#     department_id = models.IntegerField(primary_key=True)

#     class Meta:
#         managed = False
#         db_table = 'public\".\"department'



# class patient(models.Model):
#     Animal_Name = models.CharField(max_length=200, primary_key=True)
#     Species_Name = models.ForeignKey(
#         'polls.species_data', on_delete=models.DO_NOTHING)
#     Emp_ID = models.ForeignKey('polls.staff', on_delete=models.DO_NOTHING)
#     Disease = models.CharField(max_length=200)
#     History_of_illness = models.CharField(max_length=200)

#     class Meta:
#         managed = False
#         db_table = 'patient'



# class staff(models.Model):
#     name = models.CharField(max_length=200)
#     emp_id = models.CharField(max_length=200, primary_key=True)
#     sanctuary_id = models.ForeignKey(
#         'polls.wildlife_sanctuary', on_delete=models.DO_NOTHING , related_name='sanctuary_id_staff')
#     nation = models.CharField(max_length=200)
#     State = models.CharField(max_length=200)
#     District = models.CharField(max_length=200)
#     City = models.CharField(max_length=200)
#     Street = models.CharField(max_length=200)
#     Block = models.IntegerField
#     department_id = models.ForeignKey(
#         'polls.department', on_delete=models.DO_NOTHING , related_name='department_id_staff')

#     class Meta:
#         managed = False
#         db_table = 'staff'




# class mobile_no(models.Model):
#     emp_id = models.ForeignKey('polls.staff', on_delete=models.DO_NOTHING , related_name='emp_id_mobile_no')
#     mobile_number = models.IntegerField(primary_key=True)

#     class Meta:
#         managed = False
#         db_table = 'mobile_no'


# class email_id(models.Model):
#     email_id = models.CharField(max_length=200, primary_key=True)
#     emp_id = models.ForeignKey('polls.staff', on_delete=models.DO_NOTHING , related_name='emp_id_email_id')

#     class Meta:
#         managed = False
#         db_table = 'email_id'


# class sighted(models.Model):
#     Date = models.DateField
#     Time = models.TimeField
#     # Citizen ID and Nation are the primary key of the visitor table and foreign key of the sighted table
#     Nation = models.ForeignKey('polls.visitor', on_delete=models.DO_NOTHING , related_name='nation_sighted')
#     Citizen_ID = models.ForeignKey(
#         'polls.visitor', on_delete=models.DO_NOTHING)
#     Animal_Name = models.ForeignKey(
#         'polls.animal', on_delete=models.DO_NOTHING)

#     class Meta:
#         managed = False
#         unique_together = (('Nation', 'Citizen_ID', 'Animal_Name'),)
#         db_table = 'sighted'


# class visited(models.Model):
#     date = models.DateField
#     nation = models.ForeignKey('polls.visitor', on_delete=models.DO_NOTHING , related_name='nation_visited')
#     citizen_id = models.ForeignKey(
#         'polls.visitor', on_delete=models.DO_NOTHING)
#     sanctuary_id = models.ForeignKey(
#         'polls.wildlife_sanctuary', on_delete=models.DO_NOTHING , related_name='sanctuary_id_visited')

#     class Meta:
#         managed = False
#         unique_together = (('citizen_id', 'nation', 'sanctuary_id'),)
#         db_table = 'visited'


# class preys_upon(models.Model):
#     pred_species = models.ForeignKey(
#         'polls.species_data', on_delete=models.DO_NOTHING , related_name='pred_species_preys_upon')
#     prey_species = models.ForeignKey(
#         'polls.species_data', on_delete=models.DO_NOTHING , related_name='prey_species_preys_upon')

#     class Meta:
#         managed = False
#         unique_together = (('pred_species', 'prey_species'),)
#         db_table = 'preys_upon'





class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)



class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(
        'DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class PriceList(models.Model):
    # Field name made lowercase.
    item = models.CharField(db_column='Item', primary_key=True, max_length=200)
    rate = models.FloatField()

    class Meta:
        managed = False
        db_table = 'price_list'
        

class WildlifeSanctuary(models.Model):
    name = models.CharField(max_length=200)
    sanctuary_id = models.BigIntegerField(primary_key=True)
    state = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    budget = models.BigIntegerField()
    type = models.CharField(max_length=200, blank=True, null=True)
    weather = models.CharField(max_length=200, blank=True, null=True)
    temparature = models.FloatField(blank=True, null=True)
    humidity = models.FloatField(blank=True, null=True)
    percipitation = models.FloatField(blank=True, null=True)
    wind_direction = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wildlife_sanctuary'


class SpeciesData(models.Model):
    name = models.CharField(primary_key=True, max_length=200)
    population = models.BigIntegerField()
    trend = models.FloatField(blank=True, null=True)
    male_female_ration = models.FloatField(blank=True, null=True)
    # Field name made lowercase.
    birth_rate = models.IntegerField(db_column='Birth_rate')
    life_expectancy = models.IntegerField(blank=True, null=True)
    # Field name made lowercase.
    remarks = models.CharField(
        db_column='Remarks', max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'species_data'


class Department(models.Model):
    department_name = models.CharField(max_length=200)
    department_id = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'department'


class Animal(models.Model):
    animal_name = models.CharField(primary_key=True, max_length=200)
    species_name = models.ForeignKey(
        'SpeciesData', models.DO_NOTHING, db_column='species_name')
    # Field name made lowercase.
    sanctuary = models.ForeignKey(
        'WildlifeSanctuary', models.DO_NOTHING, db_column='Sanctuary_ID')
    health = models.CharField(max_length=200)
    Age = models.IntegerField(db_column='Age')  # Field name made lowercase.
    gender = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'animal'


class Staff(models.Model):
    name = models.CharField(max_length=200)
    emp_id = models.CharField(primary_key=True, max_length=200)
    sanctuary_id = models.BigIntegerField()
    nation = models.CharField(max_length=200)
    # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=200)
    # Field name made lowercase.
    district = models.CharField(db_column='District', max_length=200)
    # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=200)
    # Field name made lowercase.
    street = models.CharField(db_column='Street', max_length=200)
    # Field name made lowercase.
    block = models.IntegerField(db_column='Block')
    department = models.ForeignKey(Department, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'staff'
        
class EmailId(models.Model):
    email = models.CharField(primary_key=True, max_length=200)
    emp = models.ForeignKey('Staff', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'email_id'


class MobileNo(models.Model):
    mobile_number = models.CharField(primary_key=True, max_length=200)
    emp = models.ForeignKey('Staff', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mobile_no'

class Expenditure(models.Model):
    # Field name made lowercase.
    item = models.ForeignKey('PriceList', models.DO_NOTHING, db_column='Item')
    # Field name made lowercase.
    invoice_id = models.CharField(
        db_column='Invoice_ID', primary_key=True, max_length=200)
    # Field name made lowercase.
    quantity = models.BigIntegerField(db_column='Quantity')
    price = models.FloatField()
    sanctuary = models.ForeignKey('WildlifeSanctuary', models.DO_NOTHING)
    # Field name made lowercase.
    emp = models.ForeignKey('Staff', models.DO_NOTHING, db_column='Emp_ID')

    class Meta:
        managed = False
        db_table = 'expenditure'







class Patient(models.Model):
    # Field name made lowercase.
    animal_name = models.OneToOneField(
        Animal, models.DO_NOTHING, db_column='Animal_Name', primary_key=True)
    # Field name made lowercase.
    species_name = models.ForeignKey(
        'SpeciesData', models.DO_NOTHING, db_column='Species_Name')
    # Field name made lowercase.
    emp = models.ForeignKey('Staff', models.DO_NOTHING, db_column='Emp_ID')
    # Field name made lowercase.
    disease = models.CharField(db_column='Disease', max_length=200)
    # Field name made lowercase.
    history_of_illness = models.CharField(
        db_column='History_of_illness', max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient'


class Visitor(models.Model):
    name = models.CharField(max_length=200)
    nation = models.CharField(primary_key=True, max_length=200)
    citizen_id = models.BigIntegerField()
    # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=200)
    # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=200)
    # Field name made lowercase.
    district = models.CharField(db_column='District', max_length=200)

    class Meta:
        managed = False
        db_table = 'visitor'
        unique_together = (('nation', 'citizen_id'),)


class Visited(models.Model):
    date = models.DateField()
    nation = models.ForeignKey(
        'Visitor', models.DO_NOTHING, db_column='nation')
    citizen_id = models.BigIntegerField(primary_key=True)
    sanctuary = models.ForeignKey('WildlifeSanctuary', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'visited'
        unique_together = (('citizen_id', 'nation', 'sanctuary'),)

class PreysUpon(models.Model):
    pred_species = models.OneToOneField(
        'SpeciesData', models.DO_NOTHING, db_column='pred_species', primary_key=True, related_name='predator_species')
    prey_species = models.ForeignKey(
        'SpeciesData', models.DO_NOTHING, db_column='prey_species', related_name='prey_species')

    class Meta:
        managed = False
        db_table = 'preys_upon'
        unique_together = (('pred_species', 'prey_species'),)



class Sighted(models.Model):
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    time = models.TimeField(db_column='Time')  # Field name made lowercase.
    # Field name made lowercase.
    nation = models.OneToOneField(
        'Visitor', models.DO_NOTHING, db_column='Nation', primary_key=True)
    # Field name made lowercase.
    citizen_id = models.BigIntegerField(db_column='Citizen_ID')
    # Field name made lowercase.
    animal_name = models.ForeignKey(
        Animal, models.DO_NOTHING, db_column='Animal_Name')

    class Meta:
        managed = False
        db_table = 'sighted'
        unique_together = (('nation', 'citizen_id', 'animal_name'),)

