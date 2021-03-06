# Generated by Django 2.0.3 on 2018-03-30 04:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('booking_id', models.IntegerField(primary_key=True, serialize=False)),
                ('state', models.CharField(max_length=50)),
                ('hospital', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50, null=True)),
                ('appointment_date', models.DateField(null=True)),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
                ('queue', models.IntegerField(blank=True, null=True)),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Avaliable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('seats', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_name', models.CharField(max_length=50)),
                ('seats_available', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.Avaliable')),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospitalName', models.CharField(max_length=100)),
                ('hospital_type', models.CharField(max_length=100)),
                ('under_govt', models.CharField(max_length=100)),
                ('hospital_address', models.CharField(max_length=200)),
                ('hospital_state', models.CharField(max_length=100)),
                ('hospital_district', models.CharField(max_length=100)),
                ('hospital_website', models.URLField(blank=True, max_length=255)),
                ('hmis', models.CharField(max_length=10)),
                ('hospital_doctor_num', models.IntegerField()),
                ('nodal_officer_name', models.CharField(max_length=100)),
                ('nodal_officer_email', models.CharField(max_length=100)),
                ('nodal_officer_password', models.CharField(max_length=100)),
                ('hmis_name', models.CharField(blank=True, max_length=100)),
                ('hmis_deploy_org_name', models.CharField(blank=True, max_length=100)),
                ('department', models.ManyToManyField(to='hospital.Department')),
            ],
        ),
    ]
