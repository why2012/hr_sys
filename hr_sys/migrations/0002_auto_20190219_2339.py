# Generated by Django 2.1.7 on 2019-02-19 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr_sys', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('parent_id', models.IntegerField(default=-1)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[(0, 'male'), (1, 'female')], max_length=50)),
                ('email', models.CharField(max_length=255, null=True)),
                ('phone', models.CharField(max_length=50, null=True)),
                ('manager_id', models.IntegerField()),
                ('province_name', models.CharField(max_length=50)),
                ('city_name', models.CharField(max_length=50)),
                ('salary', models.PositiveIntegerField()),
                ('status', models.SmallIntegerField(choices=[(0, 'normal'), (1, 'desert')])),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hr_sys.Department')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.SmallIntegerField(choices=[(0, 'ontime'), (1, 'late')])),
                ('standard_time', models.SmallIntegerField()),
                ('check_time', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hr_sys.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('order', models.IntegerField()),
                ('next_level_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EmployeePosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EmployPromoteHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.SmallIntegerField(choices=[(0, 'promote'), (1, 'desert'), (2, 'demote')])),
                ('log_time', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hr_sys.Employee')),
                ('from_level', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='from_level_fk', to='hr_sys.EmployeeLevel')),
                ('to_level', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='to_level_fk', to='hr_sys.EmployeeLevel')),
            ],
        ),
        migrations.CreateModel(
            name='KeyValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hr_sys.EmployeeLevel'),
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hr_sys.EmployeePosition'),
        ),
    ]
