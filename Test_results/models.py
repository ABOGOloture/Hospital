from django.db import models

class PersonalInformation(models.Model):
    surname = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    Age = models.IntegerField(blank=True, null=True )
    sex = models.CharField(max_length=20)
    Ward = models.CharField(max_length=200)
    Laboratory_number = models.IntegerField(default=0)
    clinic_Diagnosis = models.CharField(max_length=300)
    specimen = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    consultant = models.CharField(max_length=200)
    date_and_time_of_specimen = models.DateTimeField(auto_now_add=True)
    Remark_on_sample = models.CharField(max_length=300)
    Hospital_number = models.IntegerField(default='08105684597')
    Requesting_Doctor = models.CharField(max_length=200)
    Patients_phone_number = models.IntegerField(default='08105554443')
    Analyte = models.CharField(max_length=100)
    Results = models.CharField(max_length=300)
    Reference_number = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.firstname

    class Meta:
        verbose_name_plural = 'Personal Information'
        #ordering = ['- date_and_time_of_specimen']



class RenalFunctionTests(models.Model):
    Electrolytes = models.CharField(max_length=200)
    Sodium = models.IntegerField(default=0)
    Potassium = models.DecimalField(decimal_places=2, max_digits=4)
    Chloride = models.IntegerField(default=0)
    Bicarbonate = models.IntegerField(default=0)
    Urea = models.DecimalField(decimal_places=2, max_digits=4)
    Creatine = models.IntegerField(default=0)
    Calcium = models.DecimalField(decimal_places=2, max_digits=8)
    Phosphate = models.DecimalField(decimal_places=2, max_digits=4)
    Uric_Acid = models.DecimalField(decimal_places=2, max_digits=4)
    Urinary_Protien = models.DecimalField(decimal_places=2, max_digits=4)
    Creatinine_clearance = models.DecimalField(decimal_places=3, max_digits=4)

    def __str__(self):
        return self.Electrolytes

    class Meta:
        verbose_name_plural = 'Renal Function Tests'


'''class Liver_Function_Test(models.Model):
    SGOT = models.IntegerField(blank=True, null=True)
    SGPT = models.IntegerField(blank=True, null=True)
    ALK_PHOS = models.IntegerField(blank=True, null=True)
    Bilirubin_Total = models.IntegerField(blank=True, null=True)
    Biluribin_Direct = models.IntegerField(blank=True, null=True)
    Total_Protein = models.IntegerField(blank=True, null=True)
    Albumin = models.IntegerField(blank=True, null=True)
    GGT = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.SGOT'''






    
    
