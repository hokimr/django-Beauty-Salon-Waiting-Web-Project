# Generated by Django 4.1.1 on 2022-09-28 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standby_system', '0002_alter_waiting_surgery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waiting',
            name='designer',
            field=models.CharField(choices=[('제', '제시'), ('가', '가을'), ('소', '소리'), ('은', '은정'), ('다', '다은'), ('미', '미지정')], max_length=1),
        ),
    ]
