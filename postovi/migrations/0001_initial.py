# Generated by Django 2.1 on 2018-08-19 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=50000)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quest_name', models.CharField(max_length=100)),
                ('quest_text', models.CharField(max_length=50000)),
            ],
        ),
        migrations.AddField(
            model_name='comments',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postovi.Questions'),
        ),
    ]
