# Generated migration for DoctorProfile country field

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_doctor_kyc'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorprofile',
            name='country',
            field=models.CharField(default='Unknown', max_length=100),
        ),
    ]
