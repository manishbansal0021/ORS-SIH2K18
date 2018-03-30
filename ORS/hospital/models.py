from django.db import models
from patient.models import Patient

# Create your models here.

class Avaliable(models.Model):
    date = models.DateField()
    seats = models.IntegerField()


    def __str__(self):
        return str(self.seats)

class Appointment(models.Model):

    # app_id = models.AutoField()
    patient = models.ForeignKey(Patient , on_delete=models.CASCADE  ,null=True , blank=True)

    booking_id = models.IntegerField(primary_key=True)

    state = models.CharField(max_length=50 , null=False  )
    hospital = models.CharField(max_length=50,null=False )
    department = models.CharField(max_length=50,null=True)
    # hospital = models.ForeignKey(Hospital , on_delete=models.CASCADE ,null=True)
    # dep = models.ForeignKey (Department , on_delete=models.CASCADE , null=True)
    appointment_date = models.DateField(null=True)

    booking_date=models.DateTimeField( auto_now_add=True)

    queue = models.IntegerField(null=True , blank=True)

    def __str__(self):
        return str(self.booking_id)


class Department(models.Model):
    # hospital_name
    seats_available = models.ForeignKey(Avaliable , on_delete=models.CASCADE , null=True)
    dep_name = models.CharField(max_length=50 , null=False , blank=False)
    # available = models.IntegerField(null=True)

    def __str__(self):
        return self.dep_name


class Hospital(models.Model):


    hospitalName            = models.CharField(max_length=100 ,blank=False)
    hospital_type           = models.CharField(max_length=100,blank=False)
    under_govt              = models.CharField(max_length=100,blank=False)
    hospital_address        = models.CharField(max_length=200,blank=False)
    hospital_state          = models.CharField(max_length=100,blank=False)

    hospital_district       = models.CharField(max_length=100,blank=False)
    hospital_website        = models.URLField(max_length=255,blank=True)
    hmis                    = models.CharField(max_length=10,blank=False)

    hospital_doctor_num     = models.IntegerField(blank=False)

    nodal_officer_name      = models.CharField(max_length=100,blank=False)
    nodal_officer_email     = models.CharField(max_length=100,blank=False)
    nodal_officer_password  = models.CharField(max_length=100,blank=False)

    hmis_name               = models.CharField(max_length=100,blank=True)
    hmis_deploy_org_name    = models.CharField(max_length=100,blank=True)
    department              = models.ManyToManyField(Department)




    # department = models.ForeignKey(Department , on_delete=models.CASCADE , null=True)
    def __str__(self):
        return self.name
