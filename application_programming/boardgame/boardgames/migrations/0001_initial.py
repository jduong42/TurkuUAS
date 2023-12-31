# Generated by Django 4.2.7 on 2023-11-24 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowed_date', models.DateField(auto_now_add=True)),
                ('return_date', models.DateTimeField(blank=True, null=True)),
                ('borrower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boardgames.user')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boardgames.game')),
            ],
        ),
    ]
