# Generated by Django 3.0.5 on 2020-04-21 23:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('creatures', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Encounters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('creatures', models.ManyToManyField(to='creatures.Creature')),
            ],
        ),
    ]
