from django.db import models
import uuid


class Cop(models.Model):

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    uniq_flag = models.CharField(max_length=155, verbose_name="系统部件唯一标识", unique=True)
    name = models.CharField(max_length=128, verbose_name=u"系统部件名称")
    ip = models.GenericIPAddressField(verbose_name=_('ip'))

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = "cop_backup_agx"
        verbose_name = "系统部件备份"
