#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
import json
from ..models import CronLog


def exec_shell(cmd):
    """执行shell命令函数"""
    sub = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout, stderr = sub.communicate()
    ret = sub.returncode
    print(stdout)
    if ret == 0:
        return ret, stdout.decode('utf-8').split('\n')
    else:
        return ret, stdout.decode('utf-8').replace('\n', '')


def exec_cmd(cmd, job_id):
    """执行CMD命令,记录日志"""
    recode, stdout = exec_shell(cmd)
    print('cmd', recode, stdout)
    CronLog(job_id=job_id, status='success' if recode == 0 else 'faild', task_cmd=cmd, task_log=str(stdout)).save()
    if recode != 0:
        print('[Error] (%s) failed' % cmd)
        exit(407)
    print('[Success] (%s) success' % cmd)
    return stdout


def exec_task(params, job_id):
    try:
        task_info = json.loads(params)
        # print(task_info)
    except:
        if "{" not in params:
            return exec_cmd(params, job_id)
        raise AttributeError('传入属性错误{"name":"print", "args":""}')
    from agentx import tasks

    if type(task_info) == list:
        task_name, args = tuple(task_info)
    else:
        try:
            task_name = task_info["name"]
        except:
            raise AttributeError("错误的命名传入")
        args = task_info['args'] if 'args' in task_info.keys() else None

    try:
        logtxt = getattr(tasks, task_name)(args)
        run_code = 0
    except Exception as e:
        logtxt = str(e)
        run_code = 1
        return "执行错误！传入的参数不合法"
    finally:
        CronLog(job_id=job_id,
                status='success' if run_code == 0 else 'faild',
                task_cmd=str(task_info),
                task_log=str(logtxt)).save()


# 原来的老版本的执行明明行任务的 cron 管理;
# 如果需要执行命令行任务使用这个脚本执行，需要执行tornado环境任务使用当前
def job_from2(scheduler, **jobargs):
    """
    实际使用中不要scheduler代替handler中的
    :param scheduler:
    :param jobargs:
    :return:
    """
    job_id = jobargs['job_id']
    func = __name__ + ':' + 'exec_cmd'
    args = jobargs['cmd']
    cron = jobargs['cron'].split(' ')
    cron_rel = dict(second=cron[0], minute=cron[1], hour=cron[2], day=cron[3], month=cron[4], day_of_week=cron[5])
    scheduler.add_job(func=func, id=job_id, kwargs={'cmd': args, 'job_id': job_id}, trigger='cron', **cron_rel,
                      replace_existing=True)
    return job_id


if __name__ == '__main__':
    pass
