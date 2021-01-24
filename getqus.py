import execjs
#导入execjs模块以便运行其他js文件 
import time
import random
#导入延时模块&随机数模块=>为发送请求随机延时

#得到参数（调用sign.js文件）
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
#由于关闭了证书查询所以会出现报错加上这个就不会报错

url = 'https://wenda.zuoyebang.com/commitui/firstcheck/getchecklist'
#请求地址

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
  "token":""         
  #由于还没找到获得token的接口，目前token只能通过获取request来获取，获取到过后输入到这里即可
}

result=''
while(result!='success'):
  if(result == "操作过快,请稍后重试"):  
      #如果出现操作过快，请稍后重试的提示此时需要等待一定时间，至少30秒
      time.sleep(45)
  else:
    time.sleep(random.random()*10*random.random())
    #随机延时
  r = requests.post(url,data=body,headers=headers,verify=False)
  #POST发送请求
  result = r.json()['errStr']
  #将获取内容以json格式存储，并获取状态
  print(result)
  #显示当前抢题的状态目前有三种["success","一审领取失败","操作过快，请稍后重试"]
  #若resul==success 那么即为抢题成功！