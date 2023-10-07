# Generated by Django 4.2.5 on 2023-10-07 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Took Responsibility', models.BooleanField(default=False, verbose_name='Terms')),
                ('message', models.TextField(verbose_name='Message')),
                ('person', models.CharField(choices=[('Candidate', 'Candidate'), ('Employee', 'Employee')], max_length=50, verbose_name='Person')),
                ('option', models.CharField(choices=[('I lost my account', 'I lost my account'), ('Update resume', 'Update resume'), ('Others', 'Others'), ('My password does not work', 'My password does not work')], max_length=50, verbose_name='Option')),
                ('email', models.CharField(max_length=50, verbose_name='Email')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('Situation', models.CharField(blank=True, choices=[('Done', 'Done'), ('Pending', 'Pending')], default='Pending', max_length=50, null=True, verbose_name='Situation')),
            ],
        ),
    ]