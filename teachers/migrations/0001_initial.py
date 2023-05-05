# Generated by Django 4.1.7 on 2023-03-25 05:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lessonType', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeachersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
                ('info', models.TextField()),
                ('yuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='teachers/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('lesson_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_lesson_type', to='lessonType.lessontype')),
            ],
        ),
    ]