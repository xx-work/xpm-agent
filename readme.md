## Tornado 项目

- 部件监控和处置监督的自己的客户端监控工具


## 2019-8-8
- 开始准备开发。
- 参考
  - [webspider](https://github.com/CallMeHoney/webspider)

## 2019-8-10
- 1, 通信加密模块的所有工具，在这个中进行。
- 2, 通信管理的所有内容在这个中进行。
- 3, 监控异常在这个中进行。
> 使用 scheachemy 代替掉原来的 ORM

## 2019-8-12
- 1, 修改数据库背景为
- 2, 修改数据库背景

## 2019-8-13
- 开始使用ORM环境在Tornado项目中。
- 目的是使用django-orm替代sqlachemy
- [策略基准](https://docs.microsoft.com/zh-cn/azure/active-directory/conditional-access/concept-baseline-protection)


## 客户端进行监控 信息采集等都使用 ORM 同样部件注册也使用ORM
- 1, 在请求外包裹 tornado.gen.task 
- 2,  \


## 2019-8-14 
- apschedueler 监控。
- 今日成果
  - 1, 完成了 sqlachemy+apscheduler对接的管理
  - 2, 修改 codo-cron 为自己的Django-ORM格式的；
  
## 2019-8-15
- 开源运维管理系统CMDB
  - [Codo-Open-DevOps](https://github.com/opendevops-cn/opendevops) 采用 py3 + tornado5
  - [Opserver](https://github.com/opserver/Opserver) 监控系统
  - [OpsManage](https://github.com/welliamcao/OpsManage) 采用 py3 + django
  - [bk_cmdb](https://github.com/Tencent/bk-cmdb) 采用Go开发
  - [adminset](https://github.com/guohongze/adminset) 采用 py2 + django

## 2019-8-16
- 今天老表科目二。
- 今天内容： 
  - 1，准备SNMP普遍信息收集
  - 2，准备相关的接口开发和编辑。
  - 3，准备通用型的部件API管理; 
  - 4, 监控完善，审计完善，任务投放流程完善。

## 2019-8-16-2
- 1, SNMP处理流程
  - 通过远程部件接口获取到部件的信息。
    - 进行本地存储和备份，如果发生修改进行告警。
    - 如果发生变更进行告警。
    - 为了不污染Django的环境，在这里我们进行告警通信。信息收集，监控等相关的内容。
    - 简单的任务也在这里进行，如果需要调用celery的任务，就用远程 requests 封装接口后调用。