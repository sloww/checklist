from django.db import models
import uuid
from django.conf import settings
from datetime import datetime

class Company(models.Model):
     
    name = models.CharField(
        verbose_name = '单位名称',
        max_length = 100,
        default = ' ',
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '单位'
        verbose_name_plural = '0.单位'

class Team(models.Model):
     
    name = models.CharField(
        verbose_name = '班组名称',
        max_length = 100,
        default = ' ',
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '班组'
        verbose_name_plural = '1.班组'


class User(models.Model):
    company = models.ForeignKey(
        'Company',
        on_delete = models.CASCADE,
        related_name = 'company_user', 
        verbose_name = '单位',
        )
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '2.用户'

class Template(models.Model):

    company = models.ForeignKey(
        'Company',
        on_delete = models.CASCADE,
        related_name = 'company_template',
        verbose_name = '单位',
        )
 
    name = models.CharField(
        verbose_name = '设备名称',
        max_length = 100,
        default = '',
        )

    title = models.CharField(
        verbose_name = '页面标题',
        max_length = 100,
        default = '',
        )
    


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '设备模版'
        verbose_name_plural = '3.设备模版'


class CheckPoint(models.Model):

    template= models.ForeignKey(
        'Template',
        on_delete = models.CASCADE,
        related_name = 'template_checkpoint',
        verbose_name = '模版',
        )

#    CHECK_CHOICES=(
#        (1,'确认型'),
#        (2,'选择型'),
#        (3,'数字输入型'),
#        (4,'文本输入型'),
#        (5,'图片上传型'),
#        )

    style = models.IntegerField(
        default = 1,
        verbose_name = '检查类型',
        choices = settings.CHECK_CHOICES, 
        )

    title = models.CharField(
        blank = True,
        default = '',
        max_length = 900,
        verbose_name = '检查内容',
        )

    no = models.IntegerField(
        default = 0,
        verbose_name = '展示顺序号'
        )

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = '检查项'
        verbose_name_plural = '4.检查项目'



class Equipment(models.Model):

    template = models.ForeignKey(
        'Template',
        on_delete = models.CASCADE,
        related_name = 'template_equipment',
        verbose_name = '模版',
        )

    team = models.ForeignKey(
        'Team',
        on_delete = models.CASCADE,
        related_name = 'team_equipment',
        verbose_name = '所属班组',
        blank = True,
        )



    uuid = models.CharField(
        max_length = 50,
        default = str(uuid.uuid4()), 
        editable = False,
        verbose_name = 'UUID',
        )

    
    
    no = models.CharField(
        verbose_name = '编号',
        max_length = 100,
        default = '0',
        )
    
    def url(self):
        return '{}{}/'.format(settings.CLURLPRE,self.uuid) 


    def __str__(self):
        return '{}-{}'.format(self.template,self.no,)

    class Meta:
        verbose_name = '设备'
        verbose_name_plural = '5.设备'


class Record(models.Model):

    equipment = models.ForeignKey(
        'Equipment',
        on_delete = models.CASCADE,
        related_name = 'equipment_record',
        verbose_name = '设备',
        )
    
    datetime = models.DateTimeField(
        auto_now_add=True, 
        blank=True,
        )

    remark = models.TextField(
        blank = True,
        verbose_name = '备注',
        )

    userstr = models.CharField(
        max_length=100,
        default='',
        verbose_name = '记录人',
        )

    teamstr = models.CharField(
        max_length=100,
        default='',
        verbose_name = '班组名称'
        )

    def __str__(self):
        return '{}-{}'.format(self.equipment,self.datetime)

    class Meta:
        verbose_name = '检查记录'
        verbose_name_plural = '6.检查记录'



class RecordPoint(models.Model):
    record = models.ForeignKey(
        'Record',
        on_delete = models.CASCADE,
        related_name = 'Record_rp',
        verbose_name = '记录表',
        )
    

    style = models.IntegerField(
        default = 1,
        verbose_name = '检查类型',
        choices = settings.CHECK_CHOICES, 
        )

    title = models.CharField(
        blank = True,
        default = '',
        max_length = 900,
        verbose_name = '检查内容',
        )
 
    value = models.CharField(
        blank = True,
        default = '',
        max_length = 900,
        verbose_name = '检查值',
        ) 

    no = models.IntegerField(
        default = 0,
        verbose_name = '展示顺序号'
        )

    remark = models.TextField(
        blank = True,
        verbose_name = '备注',
        )


    def __str__(self):
        return '{}-{}'.format(self.record,self.value)

    class Meta:
        verbose_name = '检查记录明细'
        verbose_name_plural = '7.检查记录明细'
