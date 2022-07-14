# Generated by Django 4.0.4 on 2022-07-14 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personal_information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=200)),
                ('firstname', models.CharField(max_length=200)),
                ('Age', models.IntegerField(blank=True, null=True)),
                ('sex', models.CharField(max_length=20)),
                ('Ward', models.CharField(max_length=200)),
                ('Laboratory_number', models.IntegerField(default=0)),
                ('clinic_Diagnosis', models.CharField(max_length=300)),
                ('specimen', models.CharField(max_length=100)),
                ('occupation', models.CharField(max_length=100)),
                ('consultant', models.CharField(max_length=200)),
                ('date_and_time_of_specimen', models.DateTimeField(auto_now_add=True)),
                ('Remark_on_sample', models.CharField(max_length=300)),
                ('Hospital_number', models.IntegerField(default='08105684597')),
                ('Requesting_Doctor', models.CharField(max_length=200)),
                ('Patients_phone_number', models.IntegerField(default='08105554443')),
                ('Analyte', models.CharField(max_length=100)),
                ('Results', models.CharField(max_length=300)),
                ('Reference_number', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Informations',
            },
        ),
        migrations.CreateModel(
            name='Renal_Function_Tests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sodium', models.IntegerField(blank=True, null=True)),
                ('Potassium', models.IntegerField(blank=True, null=True)),
                ('Chloride', models.IntegerField(blank=True, null=True)),
                ('Bicarbonate', models.IntegerField(blank=True, null=True)),
                ('Urea', models.IntegerField(blank=True, null=True)),
                ('Creatine', models.IntegerField(blank=True, null=True)),
                ('Calcium', models.IntegerField(blank=True, null=True)),
                ('Phosphate', models.IntegerField(blank=True, null=True)),
                ('Uric_Acid', models.IntegerField(blank=True, null=True)),
                ('Urinary_Protien', models.IntegerField(blank=True, null=True)),
                ('Creatinine_clearance', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]