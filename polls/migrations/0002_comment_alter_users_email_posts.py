# Generated by Django 4.2.5 on 2023-09-26 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=1000000)),
            ],
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=200, unique=True),
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=1000000)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.comment')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.users')),
            ],
        ),
    ]