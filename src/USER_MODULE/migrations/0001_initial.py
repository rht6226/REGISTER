# Generated by Django 2.1.4 on 2019-01-02 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_id', models.CharField(max_length=15, unique=True)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('first_name', models.CharField(default='', max_length=100)),
                ('last_name', models.CharField(default='', max_length=100)),
                ('type', models.CharField(blank=True, choices=[('s', 'student'), ('f', 'faculty')], default='s', max_length=1)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('middle_name', models.CharField(blank=True, default='', max_length=30)),
                ('gender', models.CharField(choices=[('m', 'male'), ('f', 'female'), ('c', 'cannot disclose')], default='c', max_length=1)),
                ('date_of_birth', models.DateField(blank=True, default='1998-11-01')),
                ('profile_image', models.ImageField(blank=True, upload_to='user/')),
            ],
            options={
                'permissions': (('add_user', 'add user'), ('change_user', 'update user'), ('delete_user', 'delete user'), ('view_user', 'view user')),
                'default_permissions': (),
            },
        ),
    ]
