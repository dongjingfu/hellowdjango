from django.db import models
from  django.db.models import  PROTECT

# Create your models here.

class Subject(models.Model):
    no = models.AutoField(primary_key=True, db_column="s_no", verbose_name="学科编号")
    name = models.CharField(max_length=255, db_column="s_name", verbose_name="学科名称")
    intro = models.CharField(max_length=512, db_column='s_intro', verbose_name="学科介绍")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "tb_subject"

    verbose_name = "学科"
    verbose_name_plural = "学科"
    pass

class Teacher(models.Model):
    no = models.AutoField(primary_key=True, db_column='tno', verbose_name='编号')
    name = models.CharField(max_length=20, db_column='tname', verbose_name='姓名')
    intro = models.CharField(max_length=1023, db_column='tintro', verbose_name='简介')
    motto = models.CharField(max_length=255, db_column='tmotto', verbose_name='教学理念')
    photo = models.CharField(max_length=511, db_column='tphoto', verbose_name='照片', null=True, blank=True)
    subject = models.ForeignKey(Subject, db_column='sno', on_delete=PROTECT, related_name='+', verbose_name='所属学科')
    manager = models.BooleanField(default=False, db_column='tmanager', verbose_name='是否主管')
    good_count = models.IntegerField(default=0, db_column='tgcount', verbose_name='好评数')
    bad_count = models.IntegerField(default=0, db_column='tbcount', verbose_name='差评数')

    @property
    def gcount(self):
        return f'{self.good_count}' \
            if self.good_count <= 999 else '999+'

    @property
    def bcount(self):
        return f'{self.bad_count}' \
            if self.bad_count <= 999 else '999+'

    class Meta(object):
        db_table = 'tb_teacher'

    verbose_name = '讲师'
    verbose_name_plural = '讲师'
    pass