# -*- coding: utf-8 -*-

####李运辰  2021-01-04
import requests
from stylecloud import gen_stylecloud
import jieba
####视频https://www.bilibili.com/video/BV1nX4y1u7BH?from=search&seid=13601446070722236862
####弹幕https://api.bilibili.com/x/v1/dm/list.so?oid=266851015
headers = {
     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'
}
def jieba_cloud(file_name, icon):
    with open(file_name, 'r', encoding='utf8') as f:
        word_list = jieba.cut(f.read())
        result = " ".join(word_list)  # 分词用 隔开
        # 制作中文云词
        icon_name = ""
        if icon == "1":
            icon_name = ''
        elif icon == "2":
            icon_name = 'fas fa-dragon'
        elif icon == "3":
            icon_name = 'fas fa-dog'
        elif icon == "4":
            icon_name = 'fas fa-cat'
        elif icon == "5":
            icon_name = 'fas fa-dove'
        elif icon == "6":
            icon_name = 'fab fa-qq'
        """
        # icon_name='',#国旗
        # icon_name='fas fa-dragon',#翼龙
        #icon_name='fas fa-dog',#狗
        # icon_name='fas fa-cat',#猫
        # icon_name='fas fa-dove',#鸽子
        # icon_name='fab fa-qq',#qq
        """
        picp = file_name.split('.')[0] + str(icon) + '.png'
        if icon_name is not None and len(icon_name) > 0:
            gen_stylecloud(text=result, icon_name=icon_name, font_path='simsun.ttc', output_name=picp)  # 必须加中文字体，否则格式错误
        else:
            gen_stylecloud(text=result, font_path='simsun.ttc', output_name=picp)  # 必须加中文字体，否则格式错误

    return picp

url="https://api.bilibili.com/x/v1/dm/list.so?oid=266851015"
r = requests.get(url, headers=headers)
r.encoding = 'utf-8'
list_s = r.text.split("<d p=")
list_s = list_s[1:]
with open("commit.txt","a+",encoding='utf-8') as f:
    for i in list_s:
          i = (i.split(">"))[1].replace("</d","")
          #print(i)
          i = i.replace("？","").replace("。","").replace("，","").replace("+","").replace("！","").replace("....","").replace(".......","")
          f.write(str(i)+"\n")

jieba_cloud("t2.txt","1")
jieba_cloud("t2.txt","3")
jieba_cloud("t2.txt","4")
jieba_cloud("t2.txt","5")
jieba_cloud("t2.txt","6")
