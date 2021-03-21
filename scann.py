#conding:utf-8
import requests
import time
with open('big.txt', 'r',encoding='UTF-8') as readfile:
  for dirs in readfile.readlines():
    url = 'http://www.moonlab.com/'+dirs.strip('\n')
    resp = requests.get(url)
    strlen = len(resp.text)
    print(url+'--'+str(resp.status_code)+'---len--'+str(strlen))
    time.sleep(0.5)
    if resp.status_code == 200 or resp.status_code == 403 or resp.status_code == 301 or resp.status_code == 500:
    with open('write.txt', 'a', encoding='UTF-8') as writefile:
      writefile.write(url+'--'+str(resp.status_code)+'---len--'+str(strlen)+'\n')
      writefile.close()
