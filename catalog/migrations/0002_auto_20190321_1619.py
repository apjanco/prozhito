# Generated by Django 2.1.7 on 2019-03-21 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableofContents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(blank=True, default=None, null=True)),
                ('journal', models.CharField(blank=True, max_length=200)),
                ('year', models.IntegerField(blank=True, default=None, null=True)),
                ('issue', models.IntegerField(blank=True, default=None, null=True)),
                ('category', models.CharField(blank=True, max_length=200, null=True)),
                ('author', models.CharField(blank=True, max_length=200, null=True)),
                ('link', models.CharField(blank=True, max_length=200, null=True)),
                ('title', models.TextField(blank=True, help_text='Text of the publication', null=True)),
                ('genre', models.TextField(blank=True, help_text='Text of the publication', null=True)),
                ('text', models.TextField(blank=True, help_text='Text of the publication', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='publication',
            name='issue',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='edition',
            name='journal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='journal', to='catalog.Journal'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='author',
            field=models.ForeignKey(max_length=200, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Author'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='journal',
            field=models.ForeignKey(max_length=200, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Journal'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='text',
            field=models.TextField(blank=True, help_text='Text of the publication'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='title',
            field=models.TextField(blank=True, help_text='Text of the publication'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='url',
            field=models.TextField(blank=True, help_text='Text of the publication'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='year',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
