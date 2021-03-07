# Generated by Django 3.1.7 on 2021-03-07 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='building_bonbun',
            field=models.IntegerField(help_text='건물본번'),
        ),
        migrations.AlterField(
            model_name='building',
            name='building_boobun',
            field=models.IntegerField(help_text='건물부번'),
        ),
        migrations.AlterField(
            model_name='jibun',
            name='building_bonbun',
            field=models.IntegerField(help_text='건물본번'),
        ),
        migrations.AlterField(
            model_name='jibun',
            name='building_boobun',
            field=models.IntegerField(help_text='건물부번'),
        ),
        migrations.AlterField(
            model_name='jibun',
            name='jibun_bonbun_bunji',
            field=models.IntegerField(help_text='지번본번(번지)'),
        ),
        migrations.AlterField(
            model_name='jibun',
            name='jibun_boobun_ho',
            field=models.IntegerField(help_text='지번부번(호)'),
        ),
        migrations.AlterField(
            model_name='jibun',
            name='jibun_no',
            field=models.IntegerField(help_text='지번일련번호'),
        ),
    ]
