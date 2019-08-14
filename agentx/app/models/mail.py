from django.db import models
import uuid


class MailHost(models.Model):
    id = models.UUIDField(default=uuid.uuid4, verbose_name='ID', primary_key=True)
    mail_host = models.CharField(verbose_name=u"邮件服务端地址", max_length=255, help_text='邮件服务端地址例如smtp.163.com', default='smtp.163.com')
    mail_user = models.CharField(verbose_name=u"邮件用户名", max_length=255, help_text='邮件用户名root')
    mail_pass = models.CharField(verbose_name=u"邮件用户名", max_length=255, help_text='邮件设置的棉麻')
    mail_postfix = models.CharField(verbose_name=u"邮件后缀", max_length=255, help_text='邮件用户名root', default='163.com')
    default_recv = models.CharField(verbose_name=u"默认接收者", max_length=255, default='180573956@qq.com,admin@actanble.com')
    active = models.BooleanField(verbose_name=u"生效", default=True)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='审计时间')

    class Meta:
        db_table = "mail_hosts"
        verbose_name = "邮件服务端列表"
        ordering = ('active', '-date_created', )
