# Generated by Django 2.0.5 on 2019-01-18 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('no', models.AutoField(db_column='s_no', primary_key=True, serialize=False, verbose_name='学科编号')),
                ('name', models.CharField(db_column='s_name', max_length=255, verbose_name='学科名称')),
                ('intro', models.CharField(db_column='s_intro', max_length=512, verbose_name='学科介绍')),
            ],
            options={
                'db_table': 'tb_subject',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('no', models.AutoField(db_column='tno', primary_key=True, serialize=False, verbose_name='编号')),
                ('name', models.CharField(db_column='tname', max_length=20, verbose_name='姓名')),
                ('intro', models.CharField(db_column='tintro', max_length=1023, verbose_name='简介')),
                ('motto', models.CharField(db_column='tmotto', max_length=255, verbose_name='教学理念')),
                ('photo', models.CharField(blank=True, db_column='tphoto', max_length=511, null=True, verbose_name='照片')),
                ('manager', models.BooleanField(db_column='tmanager', default=False, verbose_name='是否主管')),
                ('good_count', models.IntegerField(db_column='tgcount', default=0, verbose_name='好评数')),
                ('bad_count', models.IntegerField(db_column='tbcount', default=0, verbose_name='差评数')),
                ('subject', models.ForeignKey(db_column='sno', on_delete=django.db.models.deletion.PROTECT, related_name='+', to='demo.Subject', verbose_name='所属学科')),
            ],
            options={
                'db_table': 'tb_teacher',
            },
        ),
    ]
