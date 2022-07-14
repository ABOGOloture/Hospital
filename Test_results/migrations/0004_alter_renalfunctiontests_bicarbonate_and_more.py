# Generated by Django 4.0.4 on 2022-07-14 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test_results', '0003_alter_renalfunctiontests_calcium_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='renalfunctiontests',
            name='Bicarbonate',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='renalfunctiontests',
            name='Calcium',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='renalfunctiontests',
            name='Chloride',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='renalfunctiontests',
            name='Creatine',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='renalfunctiontests',
            name='Creatinine_clearance',
            field=models.DecimalField(decimal_places=3, max_digits=4),
        ),
        migrations.AlterField(
            model_name='renalfunctiontests',
            name='Phosphate',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='renalfunctiontests',
            name='Potassium',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='renalfunctiontests',
            name='Sodium',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='renalfunctiontests',
            name='Urea',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='renalfunctiontests',
            name='Uric_Acid',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='renalfunctiontests',
            name='Urinary_Protien',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
