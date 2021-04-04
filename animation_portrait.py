import requests, base64
import uuid


def get_acess_token():
    # client_id 为官网获取的AK， client_secret 为官网获取的SK，去 百度智能管理中心创建获取
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=【官网获取的AK】&client_secret=【官网获取的SK】'
    response = requests.get(host)
    return response.json()['access_token']


def make_picture(path):
    request_url = "https://aip.baidubce.com/rest/2.0/image-process/v1/selfie_anime"
    # 二进制方式打开图片文件
    f = open(path, 'rb')
    img = base64.b64encode(f.read())

    params = {"image": img}
    access_token = get_acess_token()
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)

    res = response.json()

    if res:
        f = open(str(uuid.uuid1()) + '.png', 'wb')
        after_img = res['image']
        after_img = base64.b64decode(after_img)
        f.write(after_img)
        f.close()

    print('------------已完成---------------------')


if __name__ == '__main__':

    path=''
    make_picture(path)
