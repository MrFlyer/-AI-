# -*- coding: utf-8 -*
import random
import wenxin_api  # 可以通过"pip install wenxin-api"命令安装
from wenxin_api.tasks.text_to_image import TextToImage
import requests
import os

temp = []
url = []
style = ["油画", "水彩画", "浮世绘", "蒸汽波艺术", "概念艺术", "未来主义", "赛博朋克", "写实风格", "巴洛克风格", "超现实主义"]
os.makedirs('./image/', exist_ok=True)
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/85.0.4183.102 Safari/537.36 '
}


def getWord(_str):
    file_path = "歌词.txt"  # 文件路径
    for line in open(file_path, encoding='UTF-8'):
        data = line.replace("\n", "")
        _str.append(data)

    # print(_str)


def getPic(words):
    wenxin_api.ak = "kqldgDh5F5CyM8qLcrOmcmtLp9GKrV0S"
    wenxin_api.sk = "oYcEbPIXtA2Q6whlTPEFXnxCpHxsPyXr"
    rd_style = random.randint(0, len(style) - 1)
    input_dict = {
        "text": words,
        "style": style[rd_style],

    }
    print(style[rd_style])
    rst = TextToImage.create(**input_dict)
    # rst = json.loads(rst)
    rst = rst['imgUrls']
    geturl = rst[random.randint(0, 5)]
    print(geturl)
    url.append(geturl)


def saveUrl(get_url):
    file = open("url.txt", "a", encoding="utf8")  # 指定文件名和保存路径、文件操作类型、编码
    file.write(get_url)  # 写入内容
    file.write('\r\n')
    file.close()  # 关闭操作对象


def downloadPic(pic_url):
    # 发送get请求图片url
    r = requests.get(pic_url, headers=headers)
    # wb 以二进制打开文件并写入，文件名不存在会创建
    with open('./image/1.png', 'wb') as f:
        f.write(r.content)  # 写入二进制内容


getWord(temp)
print(temp)
getPic(temp[14])
saveUrl(url[0])
downloadPic(url[0])
