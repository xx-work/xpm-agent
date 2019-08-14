from django.db import models


class CronLog(models.Model):

    log_id = models.IntegerField('log_id', primary_key=True)
    job_id = models.CharField('job_id', max_length=10)
    status = models.CharField('task_cmd', max_length=10)
    task_cmd = models.CharField('task_cmd', max_length=150)
    task_log = models.TextField('task_log')
    exec_time = models.DateTimeField(auto_now_add=True, verbose_name='执行时间')

    class Meta:
        db_table = "cron_log"
        verbose_name = "Cron执行日志"
        ordering = ('active', '-date_created', )