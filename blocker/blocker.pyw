import time
from datetime import datetime
hosts_temp=r"C:\Users\Thanos\Desktop\blocker\hosts"
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="192.168.1.3"

blockedWebsites=["http://www.newsbomb.gr","http://www.newsit.gr"]

while True:
    if datetime(datetime.now().year,datetime.now().month,datetime.now().day,10)<datetime.now()<datetime(datetime.now().year,datetime.now().month,datetime.now().day,20):
      print(2)
      with open(hosts_path,'r+') as file:
        content=file.read()
        for website in blockedWebsites:
            if website in content:
                pass
            else:
                file.write(redirect+ " "+website+"\n")
    else:
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in blockedWebsites):
                    file.write(line)
            file.truncate()

    time.sleep(5)
