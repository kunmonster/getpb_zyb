var result = require("./sign")
var businessId = result.businessId;
var sign = result.sign;
var ts = result.ts;

var url = "https://wenda.zuoyebang.com/commitui/firstcheck/getchecklist";
var res = http.request(url,{
      headers:{
        'Host': 'wenda.zuoyebang.com',
        'Connection':'keep-alive',
        'Content-Length':'142',
        'Accept':'application/json, text/plain, */*',
        'Origin':'https://wenda.zuoyebang.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
        'Content-Type':'application/x-www-form-urlencoded',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'en-us,en'
      },
      body:"businessId="+businessId+"&ts="+ts+"&sign="+sign+"&token="+"d4a41753702a196f9ce162e496cd882c7eb0d09a",
})
var status = res.statusCode;
console.log(status);
