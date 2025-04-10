# Generated by Django 3.1.12 on 2025-04-09 04:26

from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('duration', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('members', djongo.models.fields.ArrayReferenceField(on_delete=django.db.models.deletion.CASCADE, to='tracker.user')),
            ],
        ),
        migrations.CreateModel(
            name='Leaderboard',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('points', models.IntegerField()),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.team')),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('activity_type', models.CharField(max_length=50)),
                ('duration', models.IntegerField()),
                ('date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.user')),
            ],
        ),
    ]
