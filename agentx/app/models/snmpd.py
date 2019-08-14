from django.db import models
import uuid


class SnmpV2AgentCfgInfo(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    snmp_host = models.GenericIPAddressField(verbose_name='IP')
    snmp_port = models.IntegerField(verbose_name="Snmp端口", default=161)
    snmp_community = models.CharField(max_length=32, verbose_name="Snmp组织密码")
    host_uniq = models.CharField(verbose_name='主机唯一ID', max_length=122, unique=True)
    collected = models.BooleanField(verbose_name="是否收集", default=True)

    class Meta:
        db_table = "snmpv2_agent_cfg_info"
        verbose_name = "SnmpV2配置信息"


class SnmpHostData(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    ip = models.GenericIPAddressField(verbose_name='IP')
    send_flow = models.FloatField( verbose_name="发送的字节数", default=0.0)
    recv_flow = models.FloatField( verbose_name="接受字节数", default=0.0)
    cpu_percent = models.FloatField( verbose_name="CPU占用", default=0.0)
    mem_percent = models.FloatField( verbose_name="内存占用", default=0.0)
    disk_percent = models.FloatField( verbose_name="硬盘占用", default=0.0)
    up_time = models.IntegerField(verbose_name="开启时间", blank=True, default=0)

    date_created = models.DateTimeField(auto_now_add=True, verbose_name="监控时间")

    class Meta:
        db_table = "snmp_agent_datas"
        verbose_name = "SNMP部件监控数据"
        ordering = ('-date_created', )
