# Generated by Django 4.1.1 on 2022-09-28 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standby_system', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waiting',
            name='Surgery',
            field=models.CharField(choices=[('C', '커트'), ('P', '펌'), ('M', '매직')], max_length=1),
        ),
    ]
