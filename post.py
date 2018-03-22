# -*- coding: UTF-8 -*-
import sys
import requests,re,json,io
reload(sys)   
sys.setdefaultencoding('utf-8')   

def getview(url):
    con = requests.get(url)

    regular = {
        'viewstate': re.compile(r'id="__VIEWSTATE" value="(.+)" />'),
        'eventvalidation': re.compile(r'id="__EVENTVALIDATION" value="(.+)" />'),
        'viewstategenrator': re.compile(r'id="__VIEWSTATEGENERATOR" value="(.+)" />')
    }
    VIEWSTATE = regular['viewstate'].findall(con.content)[0]
    EVENTVALIDATION = regular['eventvalidation'].findall(con.content)[0]
    VIEWSTATEGENERATOR = regular['viewstategenrator'].findall(con.content)[0]
    return [VIEWSTATE, VIEWSTATEGENERATOR, EVENTVALIDATION]


f = io.open("info.json", encoding='utf-8')
info = json.load(f)
i=0
while(info['class'][i]):
	date = info['class'][i]['date']

	sjd = info['class'][i]['sjd']
	
	roomid = info['class'][i]['roomid']
	
	url = "http://jxzygl.zju.edu.cn/jsjy/jsjysqb.aspx?xn=2017-2018&xq=2&xxq=春&xqj=7&sjd="+sjd+"&kssj="+date+"&jssj="+date+"&jsbh="+roomid+"&jsdl=1&ytmc=组织培训&ytvalue=4"
	print url
	VIEWSTATE, VIEWSTATEGENERATOR, EVENTVALIDATION = getview(url)
	
	studentid = info['class'][i]['studentid']
	passwd = info['class'][i]['passwd']
	phone = info['class'][i]['phone']
	email = info['class'][i]['email']
	ddlShbm = info['class'][i]['ddlShbm']
	txtJyly = info['class'][i]['txtJyly']
	txtSydx = info['class'][i]['txtSydx']
	payload = {'__VIEWSTATE':VIEWSTATE,
	           '__VIEWSTATEGENERATOR':VIEWSTATEGENERATOR,
	           '__EVENTTARGET':'',
	           '__EVENTARGUMENT':'',
	           '__EVENTVALIDATION':EVENTVALIDATION,
		           'txtYhm':studentid,
        	   'txtMM':passwd,
        	   'Txtdh':phone,
        	   'tbDzyx':email,
        	   'ddlShbm':ddlShbm,
        	   'txtJyly':txtJyly,
        	   'txtSydx':txtSydx,
        	    'ddlSfsyxcp': '否',
        	    'txtSfsyxcp':'',
        	    'ddlSfkzylhd': '否',
        	   'txtSfkzylhd':'',
        	    'ddlSfxwrycj': '否',
        	   'txtSfxwrycj':'',
        	   'txtYYLY':'',
        	    'btnSave': '提+交'
        	   }
	
	my_headers = {
    	'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0',
    	'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    	'Accept-Encoding' : 'gzip',
    	'Accept-Language' : 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
    	'Referer':url,
    	'Cookie':'ASP.NET_SessionId=bcjnkiyowt3coliersetgzb2',
    	'Content-Type': 'application/x-www-form-urlencoded',
    	'Origin': 'http://jxzygl.zju.edu.cn',
    	'Connection': 'keep-alive',
    	'Host': 'jxzygl.zju.edu.cn',
    	'Upgrade-Insecure-Requests': '1'
	}	
	r = requests.post(url,data = payload,headers = my_headers)
	print r.content
	print date+";"
	print studentid+";"
	print passwd+";"
	i = i+1
