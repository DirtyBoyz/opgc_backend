# Generated by Django 2.2.17 on 2021-01-17 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achievements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('summary', models.CharField(max_length=200, verbose_name='summary')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GithubUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(max_length=200, unique=True)),
                ('profile_image', models.CharField(max_length=500, null=True)),
                ('total_contribution', models.IntegerField(default=0, verbose_name='contribution')),
                ('rank', models.SmallIntegerField(choices=[(15, 'Gold'), (10, 'Silver'), (5, 'bronze'), (0, 'unrank')], default=0)),
                ('company', models.CharField(blank=True, default='', max_length=100)),
                ('bio', models.CharField(blank=True, default='', max_length=200)),
                ('blog', models.CharField(blank=True, default='', max_length=100)),
                ('public_repos', models.IntegerField(blank=True, default=0)),
                ('followers', models.IntegerField(blank=True, default=0)),
                ('following', models.IntegerField(blank=True, default=0)),
                ('status', models.SmallIntegerField(choices=[(0, 'none'), (5, 'completed'), (10, 'waiting'), (15, 'updating'), (20, 'fail')], default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(max_length=100, unique=True, verbose_name='language_type')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('description', models.CharField(max_length=500, verbose_name='description')),
                ('logo', models.CharField(max_length=500, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserOrganization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('github_user', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='githubs.GithubUser')),
                ('organization', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='githubs.Organization')),
            ],
            options={
                'verbose_name': 'user organization',
                'db_table': 'githubs_user_organization',
            },
        ),
        migrations.CreateModel(
            name='UserLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('number', models.IntegerField(default=0)),
                ('github_user', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='githubs.GithubUser')),
                ('language', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='githubs.Language')),
            ],
            options={
                'verbose_name': 'user language',
                'db_table': 'githubs_user_language',
            },
        ),
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('contribution', models.IntegerField(default=0, verbose_name='contribution')),
                ('name', models.CharField(max_length=100)),
                ('full_name', models.CharField(max_length=100)),
                ('owner', models.CharField(max_length=100)),
                ('organization', models.CharField(max_length=100)),
                ('language', models.CharField(default='', max_length=100)),
                ('github_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='repository', to='githubs.GithubUser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='organization',
            name='github_users',
            field=models.ManyToManyField(blank=True, related_name='organization', through='githubs.UserOrganization', to='githubs.GithubUser'),
        ),
        migrations.AddField(
            model_name='language',
            name='github_users',
            field=models.ManyToManyField(blank=True, related_name='language', through='githubs.UserLanguage', to='githubs.GithubUser'),
        ),
    ]
