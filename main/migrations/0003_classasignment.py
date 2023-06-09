# Generated by Django 4.1.2 on 2023-04-18 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_classes_class_rename_students_student_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassAsignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.class')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.subject')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.teacher')),
            ],
        ),
    ]
