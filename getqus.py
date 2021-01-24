import execjs
#导入execjs模块以便运行其他js文件 
import time
import random
#导入延时模块&随机数模块=>为发送请求随机延时

#得到参数（调用其他几个js文件）
def get_js():
  f = open("./sign.js",'r',encoding='UTF-8')
  line = f.readline()  
  jsstr = ''  
  while line:  
    jsstr = jsstr + line  
    line = f.readline()  
  return jsstr

jsresult = get_js()
ctx = execjs.compile(jsresult)
allpar = ctx.call('createSign')
sign = allpar["sign"]
businessId = allpar["businessId"]
ts = allpar["ts"]

#导入请求访问的库进行POST提交
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://wenda.zuoyebang.com/commitui/firstcheck/getchecklist'
headers={
'Host':'wenda.zuoyebang.com',
'Connection':'keep-alive',
'Content-Length':'142',
'Accept':'application/json, text/plain, */*',
'Origin':'https://wenda.zuoyebang.com',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
'Content-Type':'application/x-www-form-urlencoded',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'en-us,en'
}

body={
  "businessId":businessId,
  "ts":ts,
  "sign":sign,
  "token":"486c41b5da3f1505a51652a58aa8d7985de2d717"
}
result=''
while(result!='success'):
  if(result == "操作过快,请稍后重试"):
      time.sleep(45)
  else:
    time.sleep(random.random()*10*random.random())
  r = requests.post(url,data=body,headers=headers,verify=False)
  result = r.json()['errStr']
  print(result)
 
  