# Generated by Django 3.0.3 on 2020-02-23 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(blank=True, help_text='Enter your Facebook URL')),
                ('twitter', models.URLField(blank=True, help_text='Enter your Twitter URL')),
                ('youtube', models.URLField(blank=True, help_text='Enter your Youtube URL')),
                ('instagram', models.URLField(blank=True, help_text='Enter your Instagram URL')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
