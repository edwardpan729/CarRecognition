import base64
import json
import requests
import urllib
import urllib.request
import urllib.parse
import numpy
import cv2
import os
from aip import AipImageClassify
from aip import AipOcr
from aip import AipBodyAnalysis
APP_ID='16630610'
API_KEY='cvLklIe7UhuQU7Uzl2eXKosx'
SECRET_KEY='Ix53uAnzQ2HAUbLKevMc689QedVG7gMl'

#车型识别
def chexing():
    imageClassify = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)
    filepath = "1.png"
    def get_file_content(filepath):
        with open(filepath, 'rb')as fp:
            return fp.read()
    options = {
        'baike_num': '0',
    }
    result = imageClassify.carDetect(get_file_content(filepath), options)
    return result
    """for i in range(len(result['result'])):
        print(result['result'][i]['name'], end='    ')
        print('%.2f' % (result['result'][i]['score'] * 100), end='')
        print('%')"""
#车牌识别
"""def chepai():
    client=AipOcr(APP_ID,API_KEY,SECRET_KEY)
    filepath="1.jpg"
    def get_file_content(filepath):
        with open(filepath,'rb')as fp:
            return fp.read()
    result1=client.licensePlate(get_file_content(filepath))
    print(result1['words_result']['color'],end='    ')
    print(result1['words_result']['number'])"""
#车辆检测
"""request_url="https://aip.baidubce.com/rest/2.0/image-classify/v1/vehicle_detect"
f=open('3.jpg','rb')
img=base64.b64decode(f.read())
params={"image":img}
params=urllib.parse.urlencode(params).encode(encoding='UTF8')
access_token='24.122a460993f618fbc9409ec8011c3b11.2592000.1564111179.282335-16630610'
request_url=request_url+ "?access_token=" + access_token
request = urllib.request.Request(url=request_url, data=params)
request.add_header('Content-Type', 'application/x-www-form-urlencoded')
response = urllib.request.urlopen(request)
content = response.read()
if content:
    print(content)"""
#驾驶行为检测
"""body=AipBodyAnalysis(APP_ID,API_KEY,SECRET_KEY)
filepath="4.jpg"
def get_file_content(filepath):
    with open(filepath,'rb')as fp:
        return fp.read()
result3=body.driverBehavior(get_file_content(filepath))
    for i in range(len(result3['person_info'])):
    print(result3['person_info'][i]['attributes'],end = '    ')
    print(result3['person_info'][i]['score']*100,end='')
    print('%')
print('%.3f'%(result3['person_info'][0]['attributes']['cellphone']['score']*100))
print('%.3f'%(result3['person_info'][0]['attributes']['both_hands_leaving_wheel']['score']*100))
print('%.3f'%(result3['person_info'][0]['attributes']['not_facing_front']['score']*100))
print('%.3f'%(result3['person_info'][0]['attributes']['not_buckling_up']['score']*100))
print('%.3f'%(result3['person_info'][0]['attributes']['smoke']['score']*100))"""


