#20200922
import requests
import json
import re
##获取token
get_param = {
    "grant_type": "client_credential",
    "appid": "wx55614004f367f8ca",
    "secret": "65515b46dd758dfdb09420bb7db2c67f"
}
url = 'https://api.weixin.qq.com/cgi-bin/token'
response = requests.get(url=url, params=get_param)
r = response.json().get('access_token')
print(r)
###添加标签

post_param_data = {   "tag" : {     "id" : 998,     "name" : "张单2"   } }

response = requests.post(url='https://api.weixin.qq.com/cgi-bin/tags/create',
                         params={'access_token':r},
                         data=json.dumps(post_param_data)
                         )
print(response.url)
print(response.content.decode('utf-8'))

###查询标签
response = requests.post(url='https://api.weixin.qq.com/cgi-bin/tags/get',
                         params={'access_token':r}
                         )
print(response.content.decode('utf-8'))

###删除标签
post_param_data2 = {   "tag":{        "id" : 651   } }
response = requests.post(url='https://api.weixin.qq.com/cgi-bin/tags/delete',
                         params={'access_token': r},
                         data=json.dumps(post_param_data2)
                         )
print(response.content.decode('utf-8'))
###re的使用
r=requests.get('https://www.qq.com')
print(r.text)
con = re.findall('name="description" content="(.+?)"',r.text)
print( con )