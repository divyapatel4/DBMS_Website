# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Animal(models.Model):
    animal_name = models.CharField(primary_key=True, max_length=-1)
    species_name = models.ForeignKey('SpeciesData', models.DO_NOTHING, db_column='species_name')
    sanctuary = models.ForeignKey('WildlifeSanctuary', models.DO_NOTHING, db_column='Sanctuary_ID')  # Field name made lowercase.
    health = models.CharField(max_length=-1)
    age = models.IntegerField(db_column='Age')  # Field name made lowercase.
    gender = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'animal'


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


class Department(models.Model):
    department_name = models.CharField(max_length=-1)
    department_id = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'department'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
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


class EmailId(models.Model):
    email = models.CharField(primary_key=True, max_length=-1)
    emp = models.ForeignKey('Staff', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'email_id'


class Expenditure(models.Model):
    item = models.ForeignKey('PriceList', models.DO_NOTHING, db_column='Item')  # Field name made lowercase.
    invoice_id = models.CharField(db_column='Invoice_ID', primary_key=True, max_length=-1)  # Field name made lowercase.
    quantity = models.BigIntegerField(db_column='Quantity')  # Field name made lowercase.
    price = models.FloatField()
    sanctuary = models.ForeignKey('WildlifeSanctuary', models.DO_NOTHING)
    emp = models.ForeignKey('Staff', models.DO_NOTHING, db_column='Emp_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'expenditure'


class MobileNo(models.Model):
    mobile_number = models.CharField(primary_key=True, max_length=-1)
    emp = models.ForeignKey('Staff', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mobile_no'


class Patient(models.Model):
    animal_name = models.OneToOneField(Animal, models.DO_NOTHING, db_column='Animal_Name', primary_key=True)  # Field name made lowercase.
    species_name = models.ForeignKey('SpeciesData', models.DO_NOTHING, db_column='Species_Name')  # Field name made lowercase.
    emp = models.ForeignKey('Staff', models.DO_NOTHING, db_column='Emp_ID')  # Field name made lowercase.
    disease = models.CharField(db_column='Disease', max_length=-1)  # Field name made lowercase.
    history_of_illness = models.CharField(db_column='History_of_illness', max_length=-1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'patient'


class PreysUpon(models.Model):
    pred_species = models.OneToOneField('SpeciesData', models.DO_NOTHING, db_column='pred_species', primary_key=True)
    prey_species = models.ForeignKey('SpeciesData', models.DO_NOTHING, db_column='prey_species')

    class Meta:
        managed = False
        db_table = 'preys_upon'
        unique_together = (('pred_species', 'prey_species'),)


class PriceList(models.Model):
    item = models.CharField(db_column='Item', primary_key=True, max_length=-1)  # Field name made lowercase.
    rate = models.FloatField()

    class Meta:
        managed = False
        db_table = 'price_list'


class Sighted(models.Model):
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    time = models.TimeField(db_column='Time')  # Field name made lowercase.
    nation = models.OneToOneField('Visitor', models.DO_NOTHING, db_column='Nation', primary_key=True)  # Field name made lowercase.
    citizen_id = models.BigIntegerField(db_column='Citizen_ID')  # Field name made lowercase.
    animal_name = models.ForeignKey(Animal, models.DO_NOTHING, db_column='Animal_Name')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sighted'
        unique_together = (('nation', 'citizen_id', 'animal_name'),)


class SpeciesData(models.Model):
    name = models.CharField(primary_key=True, max_length=-1)
    population = models.BigIntegerField()
    trend = models.FloatField(blank=True, null=True)
    male_female_ration = models.FloatField(blank=True, null=True)
    birth_rate = models.IntegerField(db_column='Birth_rate')  # Field name made lowercase.
    life_expectancy = models.IntegerField(blank=True, null=True)
    remarks = models.CharField(db_column='Remarks', max_length=-1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'species_data'


class Staff(models.Model):
    name = models.CharField(max_length=-1)
    emp_id = models.CharField(primary_key=True, max_length=-1)
    sanctuary_id = models.BigIntegerField()
    nation = models.CharField(max_length=-1)
    state = models.CharField(db_column='State', max_length=-1)  # Field name made lowercase.
    district = models.CharField(db_column='District', max_length=-1)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=-1)  # Field name made lowercase.
    street = models.CharField(db_column='Street', max_length=-1)  # Field name made lowercase.
    block = models.IntegerField(db_column='Block')  # Field name made lowercase.
    department = models.ForeignKey(Department, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'staff'


class Visited(models.Model):
    date = models.DateField()
    nation = models.ForeignKey('Visitor', models.DO_NOTHING, db_column='nation')
    citizen_id = models.BigIntegerField(primary_key=True)
    sanctuary = models.ForeignKey('WildlifeSanctuary', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'visited'
        unique_together = (('citizen_id', 'nation', 'sanctuary'),)


class Visitor(models.Model):
    name = models.CharField(max_length=-1)
    nation = models.CharField(primary_key=True, max_length=-1)
    citizen_id = models.BigIntegerField()
    gender = models.CharField(db_column='Gender', max_length=-1)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=-1)  # Field name made lowercase.
    district = models.CharField(db_column='District', max_length=-1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'visitor'
        unique_together = (('nation', 'citizen_id'),)


class WildlifeSanctuary(models.Model):
    name = models.CharField(max_length=-1)
    sanctuary_id = models.BigIntegerField(primary_key=True)
    state = models.CharField(max_length=-1)
    district = models.CharField(max_length=-1)
    budget = models.BigIntegerField()
    type = models.CharField(max_length=-1, blank=True, null=True)
    weather = models.CharField(max_length=-1, blank=True, null=True)
    temparature = models.FloatField(blank=True, null=True)
    humidity = models.FloatField(blank=True, null=True)
    percipitation = models.FloatField(blank=True, null=True)
    wind_direction = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wildlife_sanctuary'
