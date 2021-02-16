import requests
import base64
import time

key = '7bc2dvth9jjngmkvq3kw4zrhcplx68fn'
body = ''

UrlPost = 'http://azcaptcha.com/in.php'
UrlGet  = 'https://azcaptcha.com/res.php'




for i in range(24,640):
    with open("Images"+str(i)+".jpg", "rb") as img_file:
        body = base64.b64encode(img_file.read())
    params = {'key': key, 'method': 'base64', 'body': body}

    resp = requests.post(UrlPost,params=params)
    id = resp.text.replace('OK|', '')
    time.sleep(5)

    paramsGet = {'key': key, 'action': 'get', 'id': id}
    resp2 = requests.get(UrlGet,params=paramsGet)
    CaptchaResult = resp2.text.replace('OK|', '')
    print(CaptchaResult  + " - Row:" + str(i))
    