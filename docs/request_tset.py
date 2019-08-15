from requests.api import request
import uuid

resp = request(method="post",
               url="http://localhost:4033/v1/cron/job/",
               json=dict(cron="*/10 * * * * *", ),
               headers={'Content-Type': 'application/json'},
               verify=False)

print(resp.status_code)
print(resp.content.decode('utf-8'))
