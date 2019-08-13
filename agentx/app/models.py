
from django.db import models
import uuid


CHANGE_STATUS = (
    ('APPENDING', '变更中'), # 变更中
    ('FAILED', '变更失败'),   # 变更失败
    ('SECCUSS', '变更成功'), # 变更成功
    ('ROLLING', '变更回滚'), # 变更回滚
)


# 之所以不用外键， 是因为当用户名没有的时候，仍然可以提供日志时间的记录。
class ChangeAudit(models.Model):
    """
    注意这个里面的变更记录, 是通过Web中间件进行返回。脚本添加和反馈。
    """
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    opreate_username = models.CharField(verbose_name=u"操作员", max_length=33, help_text='默认为操作员')
    remote_addr = models.GenericIPAddressField(verbose_name=u"IP", help_text='操作的IP', default='127.0.0.1')
    change_name = models.CharField(verbose_name="变更名", max_length=155, blank=True, default='')
    change_obj = models.CharField(verbose_name="变更对象", max_length=155, blank=True, default='')
    change_desc = models.CharField(verbose_name="变更描述", max_length=155, blank=True, default='')
    change_stat = models.CharField(verbose_name="变更状态", max_length=10, choices=CHANGE_STATUS, default="SECCUSS")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='审计时间')

    class Meta:
        db_table = "change_audit"
        verbose_name = "平台变更记录"
        ordering = ('-date_created', )

