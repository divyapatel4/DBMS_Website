from django.db import models

class Visitor(models.Model):
    name = models.CharField(max_length=200)
    nation = models.CharField(max_length=200)
    citizen_id = models.IntegerField
    Gender = models.CharField(max_length=200)
    State = models.CharField(max_length=200)
    District = models.CharField(max_length=200)
    # Primary key is (nation, citizen_id)
    class Meta:
        unique_together = ('nation', 'citizen_id')
        db_table = 'visitor'


# CREATE TABLE IF NOT EXISTS wildlife_db. animal
# animal_name character varying COLLATE pg_catalog."default" NOT NULL,
# species_name character varying COLLATE pg_catalog. "default" NOT NULL,
# "Sanctuary_ID" bigint NOT NULL,
# "Health" character varying COLLATE pg_catalog."default" NOT NULL,
# "Age" integer NOT NULL,
# "Gender" character varying COLLATE pg_catalog. "default" NOT NULL,
# CONSTRAINT "Animal_pkey" PRIMARY KEY(animal_name),
# CONSTRAINT "Sanct_FK" FOREIGN KEY("Sanctuary_ID")
# REFERENCES wildlife_db.wildlife_sanctuary(sanctuary_id) MATCH SIMPLE
# ON UPDATE NO ACTION
# ON DELETE NO ACTION
# NOT VALID,
# CONSTRAINT "Species_FK" FOREIGN KEY(species_name)
# REFERENCES wildlife_db. species_data(name) MATCH SIMPLE
# ON UPDATE NO ACTION
# ON DELETE NO ACTION
# NOT VALID

# TABLESPACE pg_default
# ALTER TABLE IF EXISTS wildlife_db. animal
# OWNER to postgres

class Animal(models.Model):
    animal_name = models.CharField(max_length=200)
    species_name = models.ForeignKey('Species_data', on_delete=models.DO_NOTHING)
    Sanctuary_ID = models.ForeignKey('Sanctuary', on_delete=models.DO_NOTHING)
    Health = models.CharField(max_length=200)
    Age = models.IntegerField
    Gender = models.CharField(max_length=200)
    # Foreign key is (Sanctuary_ID, species_name)

    class Meta:
        unique_together = ('animal_name')
        db_table = 'animal'


# CREATE TABLE IF NOT EXISTS wildlife_db. species_data
# name character varying COLLATE pg_catalog. "default" NOT NULL,
# population bigint NOT NULL,
# trend real,
# male_female_ration real,
# "Birth_rate" integer NOT NULL,
# life_expectancy integer,
# "Remarks" character varying COLLATE pg_catalog. "default",
# CONSTRAINT "Species_data_pkey" PRIMARY KEY(name)

# TABLESPACE pg_default
# ALTER TABLE IF EXISTS wildlife_db. species_data
# OWNER to postgres

class Species_data(models.Model):
    name = models.CharField(max_length=200)
    population = models.IntegerField
    trend = models.FloatField
    male_female_ration = models.FloatField
    Birth_rate = models.IntegerField
    life_expectancy = models.IntegerField
    Remarks = models.CharField(max_length=200)
    class Meta:
        unique_together = ('name')
        db_table = 'species_data'


# CREATE TABLE IF NOT EXISTS wildlife_db. wildlife_sanctuary
# name character varying COLLATE pg_catalog."default" NOT NULL,
# sanctuary_id bigint NOT NULL,
# state character varying COLLATE pg_catalog."default" NOT NULL,
# district character varying COLLATE pg_catalog. "default" NOT NULL,
# budget bigint NOT NULL,
# type character varying COLLATE pg_catalog."default",
# weather character varying COLLATE pg_catalog."default",
# temparature real,
# humidity real,
# percipitation real,
# wind_direction character varying COLLATE pg_catalog."default",
# CONSTRAINT wildlife_sanctuary_pkey PRIMARY KEY(sanctuary_id)

# TABLESPACE pg_default
# ALTER TABLE IF EXISTS wildlife_db.wildlife_sanctuary
# OWNER to postgres

class wildlife_sanctuary(models.Model):
    name = models.CharField(max_length=200)
    sanctuary_id = models.IntegerField
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
        unique_together = ('sanctuary_id')
        db_table = 'wildlife_sanctuary'
        
        
# CREATE TABLE IF NOT EXISTS wildlife_db. expenditure
# "Item" character varying COLLATE pg_catalog."default" NOT NULL,
# "Invoice_ID" character varying COLLATE pg_catalog. "default" NOT NULL,
# "Quantity" bigint NOT NULL,
# price real NOT NULL,
# sanctuary_id bigint NOT NULL,
# "Emp_ID" character varying COLLATE pg_catalog. "default" NOT NULL,
# CONSTRAINT "Expenditure_pkey" PRIMARY KEY("Invoice_ID"),
# CONSTRAINT "Emp_ID" FOREIGN KEY("Emp_ID")
# REFERENCES wildlife_db. staff(emp_id) MATCH SIMPLE
# ON UPDATE NO ACTION
# ON DELETE NO ACTION
# NOT VALID,
# CONSTRAINT "Item_FK" FOREIGN KEY("Item")
# REFERENCES wildlife_db.price_list("Item") MATCH SIMPLE
# ON UPDATE NO ACTION
# ON DELETE NO ACTION
# NOT VALID,
# CONSTRAINT "Sanct_ID" FOREIGN KEY(sanctuary_id)
# REFERENCES wildlife_db. wildlife_sanctuary(sanctuary_id) MATCH SIMPLE
# ON UPDATE NO ACTION
# ON DELETE NO ACTION
# NOT VALID

# TABLESPACE pg_default

class expenditure(models.Model):
    Item = models.CharField(max_length=200)
    Invoice_ID = models.CharField(max_length=200)
    Quantity = models.IntegerField
    price = models.FloatField
    sanctuary_id = models.ForeignKey('wildlife_sanctuary', on_delete=models.DO_NOTHING)
    Emp_ID = models.ForeignKey('Staff', on_delete=models.DO_NOTHING)
    class Meta:
        unique_together = ('Invoice_ID')
        db_table = 'expenditure'


# CREATE TABLE IF NOT EXISTS public. "Price_List"
# "Item" "char" NOT NULL,
# "Rate" real NOT NULL,
# CONSTRAINT "Price_List_pkey" PRIMARY KEY("Item")

# TABLESPACE pg_default
# ALTER TABLE IF EXISTS public. "Price_List"
# OWNER I to postgres

class Price_List(models.Model):
    Item = models.CharField(max_length=200)
    Rate = models.FloatField
    class Meta:
        unique_together = ('Item')
        db_table = 'Price_List'


# CREATE TABLE IF NOT EXISTS public. "Department"
# "Department_Name" "char" NOT NULL,
# "Department_ID" bigint NOT NULL,
# CONSTRAINT "Department_pkey" PRIMARY KEY("Department_ID")
# TABLESPACE pg_default
# ALTER TABLE IF EXISTS public. "Department"
# OWNER to postgres

class Department(models.Model):
    Department_Name = models.CharField(max_length=200)
    Department_ID = models.IntegerField
    class Meta:
        unique_together = ('Department_ID')
        db_table = 'Department'
        

# CREATE TABLE IF NOT EXISTS wildlife_db.patient
# "Animal Name" character varying COLLATE pg_catalog."default" NOT NULL,
# "Species_Name" character varying COLLATE pg_catalog."default" NOT NULL,
# "Emp_ID" character varying COLLATE pg_catalog. "default" NOT NULL,
# "Disease" character varying COLLATE pg_catalog."default" NOT NULL,
# "History_of_illness" character varying COLLATE pg_catalog."default",
# CONSTRAINT "Patient_pkey" PRIMARY KEY("Animal_Name"),
# CONSTRAINT "Animal_FK" FOREIGN KEY("Animal_Name")
# REFERENCES wildlife_db. animal(animal_name) MATCH SIMPLE
# ON UPDATE NO ACTION
# ON DELETE NO ACTION
# NOT VALID,
# CONSTRAINT "Emp_FK" FOREIGN KEY("Emp_ID")
# REFERENCES wildlife_db.staff(emp_id) MATCH SIMPLE
# ON UPDATE NO ACTION
# ON DELETE NO ACTION
# NOT VALID,
# CONSTRAINT "Species_FK" FOREIGN KEY("Species_Name")
# REFERENCES wildlife_db. species_data(name) MATCH SIMPLE
# ON UPDATE NO ACTION
# ON DELETE NO ACTION
# NOT VALID
# TABLESPACE pg_default

class patient(models.Model):
    Animal_Name = models.CharField(max_length=200)
    Species_Name = models.ForeignKey('species_data', on_delete=models.DO_NOTHING)
    Emp_ID = models.ForeignKey('Staff', on_delete=models.DO_NOTHING)
    Disease = models.CharField(max_length=200)
    History_of_illness = models.CharField(max_length=200)
    class Meta:
        unique_together = ('Animal_Name')
        db_table = 'patient'


# CREATE TABLE IF NOT EXISTS wildlife_db.staff
# name character varying COLLATE pg_catalog. "default" NOT NULL,
# emp_id character varying COLLATE pg_catalog."default" NOT NULL,
# sanctuary_id bigint NOT NULL,
# nation character varying COLLATE pg_catalog. "default" NOT NULL,
# "State" character varying COLLATE pg_catalog."default" NOT NULL,
# "District" character varying COLLATE pg_catalog. "default" NOT NULL,
# "City" character varying COLLATE pg_catalog."default" NOT NULL,
# "Street" character varying COLLATE pg_catalog."default" NOT NULL,
# "Block" integer NOT NULL,
# department_id bigint NOT NULL,
# CONSTRAINT staff_pkey PRIMARY KEY(emp_id),
# CONSTRAINT "Dept_FK" FOREIGN KEY(department_id)
# REFERENCES wildlife_db. department(department_id) MATCH SIMPLE
# ON UPDATE NO ACTION
# ON DELETE NO ACTION
# NOT VALID

# TABLESPACE pg_default
# ALTER TABLE IF EXISTS wildlife_db. staff
# OWNER to postgres

class staff(models.Model):
    name = models.CharField(max_length=200)
    emp_id = models.CharField(max_length=200)
    sanctuary_id = models.ForeignKey('wildlife_sanctuary', on_delete=models.DO_NOTHING,on_update=models.DO_NOTHING)
    nation = models.CharField(max_length=200)
    State = models.CharField(max_length=200)
    District = models.CharField(max_length=200)
    City = models.CharField(max_length=200)
    Street = models.CharField(max_length=200)
    Block = models.IntegerField
    department_id = models.ForeignKey('Department', on_delete=models.DO_NOTHING,on_update=models.DO_NOTHING)
    class Meta:
        unique_together = ('emp_id')
        db_table = 'staff'
        

# CREATE TABLE IF NOT EXISTS public. "Mobile_Number"
# "Emp_ID" "char" NOT NULL,
# "Mobile_ No" bigint NOT NULL,
# CONSTRAINT "Mobile_Number_pkey" PRIMARY KEY("Mobile_No"),
# CONSTRAINT "Staff_FK" FOREIGN KEY("Emp_ID")
# REFERENCES public. "Staff" (Emp_id") MATCH SIMPLE
# ON UPDATE NO ACTION
# ON DELETE NO ACTION
# NOT VALID

# TABLESPACE pg_default
# ALTER TABLE IF EXISTS public. "Mobile_Number"
# OWNER to postgres


class Mobile_Number(models.Model):
    Emp_ID = models.ForeignKey('Staff', on_delete=models.DO_NOTHING)
    Mobile_No = models.IntegerField
    class Meta:
        unique_together = ('Mobile_No')
        db_table = 'Mobile_Number'
        

# CREATE TABLE IF NOT EXISTS public. "Email_ID"
# "Email_ID" "char" NOT NULL,
# "Emp_ID" "char" NOT NULL,
# CONSTRAINT "Email_ID_pkey" PRIMARY KEY("Email_ID"),
# CONSTRAINT "Staff_FK" FOREIGN KEY("Emp_ID")
# REFERENCES public. "Staff" ("Emp_id") MATCH SIMPLE
# ON UPDATE NO ACTION
# ON DELETE NO ACTION
# NOT VALID

# TABLESPACE pg_default
# ALTER TABLE IF EXISTS public. "Email_ID"
# OWNER to postgres

class Email_ID(models.Model):
    Email_ID = models.CharField(max_length=200)
    Emp_ID = models.ForeignKey('Staff', on_delete=models.DO_NOTHING)
    class Meta:
        unique_together = ('Email_ID')
        db_table = 'Email_ID'


class sighted(models.Model):
    Date = models.DateField
    Time = models.TimeField
    # Citizen ID and Nation are the primary key of the visitor table and foreign key of the sighted table
    Nation = models.ForeignKey('visitor', on_delete=models.DO_NOTHING)
    Citizen_ID = models.ForeignKey('visitor', on_delete=models.DO_NOTHING)
    Animal_Name = models.ForeignKey('animal', on_delete=models.DO_NOTHING)
    class Meta:
        unique_together = ('Nation', 'Citizen_ID', 'Animal_Name')
        db_table = 'sighted'
        

# CREATE TABLE IF NOT EXISTS wildlife db. visited
# date date NOT NULL,
# nation character varying COLLATE pg_catalog."default" NOT NULL,
# citizen_id bigint NOT NULL,
# sanctuary_id bigint NOT NULL,
# CONSTRAINT "Visited_pkey" PRIMARY KEY(citizen_id, nation, sanctuary_id),
# CONSTRAINT "Sanct_FK" FOREIGN KEY(sanctuary_id)
# REFERENCES wildlife_db. wildlife_sanctuary(sanctuary_id) MATCH SIMPLE
# ON UPDATE NO ACTION
# ON DELETE NO ACTION
# NOT VALID,
# CONSTRAINT "Visitor_FK" FOREIGN KEY(citizen_id, nation)
# REFERENCES wildlife_db. visitor(citizen_id, nation) MATCH SIMPLE
# ON UPDATE NO ACTION
# ON DELETE NO ACTION
# NOT VALID

# TABLESPACE pg_default
# ALTER TABLE IF EXISTS wildlife_ db. visited
# OWNER to postgres

class visited(models.Model):
    Date = models.DateField
    nation = models.ForeignKey('visitor', on_delete=models.DO_NOTHING)
    citizen_id = models.ForeignKey('visitor', on_delete=models.DO_NOTHING)
    sanctuary_id = models.ForeignKey('wildlife_sanctuary', on_delete=models.DO_NOTHING)
    class Meta:
        unique_together = ('Citizen_ID', 'Nation', 'Sanctuary_ID')
        db_table = 'visited'
        

# CREATE TABLE IF NOT EXISTS wildlife_db.preys_upon
# pred_species character varying COLLATE pg_catalog. "default" NOT NULL,
# prey_species character varying COLLATE pg_catalog."default" NOT NULL,
# CONSTRAINT "Preys_upon_pkey" PRIMARY KEY(pred_species, prey_species),
# CONSTRAINT "Species_FK1" FOREIGN KEY(pred_species)
# REFERENCES wildlife_db.species_data(name) MATCH SIMPLE
# ON UPDATE NO ACTION
# ON DELETE NO ACTION
# NOT VALID,
# CONSTRAINT "Species_FK2" FOREIGN KEY(prey_species)
# REFERENCES wildlife_db. species_data(name) MATCH SIMPLE
# ON UPDATE NO ACTION
# ON DELETE NO ACTION
# NOT VALID

# TABLESPACE pg_default
# ALTER TABLE IF EXISTS wildlife_db.preys_upon
# OWNER to postgres

class preys_upon(models.Model):
    pred_species = models.ForeignKey('species_data', on_delete=models.DO_NOTHING)
    prey_species = models.ForeignKey('species_data', on_delete=models.DO_NOTHING)
    class Meta:
        unique_together = ('pred_species', 'prey_species')
        db_table = 'preys_upon'
        
