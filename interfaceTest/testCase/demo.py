#20200922
import requests
import json
##获取token
def get_token(self):
    get_param = {
        "grant_type": "client_credential",
        "appid": "wx55614004f367f8ca",
        "secret": "65515b46dd758dfdb09420bb7db2c67f"
    }
    url = 'https://api.weixin.qq.com/cgi-bin/token'
    response = requests.get(url=url, params=get_param)
    r = response.json().get('access_token')
    print(self.r)
    return (self.r)


###添加标签
def add_tag(self):
    url_param_dict = {
        "access_token": str(self.r)
    }
    post_param_data = {"tag": {"name": "今天是20200922"}}

    response = requests.post(url='https://api.weixin.qq.com/cgi-bin/tags/create',
                             params=url_param_dict,
                             data=json.dumps(post_param_data)
                             )
    print(response.content.decode('utf-8'))
get_token()
add_tag()

###查询标签



