from requests.api import request
import uuid

resp = request(method="post",
               url="http://localhost:4011/v1/cron/job/",
               data={"cron": "*/12 * * * * *", "params": "dir", "job_id": '1234'},
               verify=False)

print(resp.status_code)
print(resp.text)
