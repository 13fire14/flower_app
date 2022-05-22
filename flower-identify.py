# -*- coding: utf-8 -*-
"""
Created on Tue May 17 14:51:24 2022

@author: bianca
"""
import streamlit as st 
import sys
import numpy as np
import cv2
import pandas as pd
import matplotlib.pyplot as plt
from streamlit.elements.image import image_to_url
import tensorflow as tf
from PIL import Image
import os

sys.path.append('C:\\Users\\bianca\\AppData\\Roaming\\Python\\Python38\\site-packages')
st.title('花卉识别系统')
#%% 添加背景图
img_url=image_to_url(plt.imread('D:/tiqam_data/week4/green.jpg'),width=-3,clamp=False,channels='RGB',output_format='auto',
                    image_id='',allow_emoji=False)
st.markdown('''
<style>
.css-fg4pbf {background-image:url('''+img_url+''');}</style>
''',unsafe_allow_html=True)

#%% 添加侧边栏
st.sidebar.title('识别结果栏')
# st.sidebar.button('!')

f=st.file_uploader('上传图片')
img=np.array(Image.open(f),dtype=np.uint8)
# st.image(img2)

#%% 加载模型
model=tf.keras.models.load_model('D:/tiqam_data/week4/102flowers/resnet50_membrane.h5')
# with st.sidebar.expander('模型参数查看'):
#     st.write(f'{model.summary()}')
#%%预处理图片
p=128
img2=cv2.resize(img,(p,p))
img3=cv2.resize(img,(360,360))
# st.image(img3)
# 增加两栏
col1,col2=st.columns(2)
col1.image(img3)
prob=model.predict(img2.reshape(-1,p,p,3))
result=np.argmax(prob)
#st.sidebar.write(f'该花识别结果为第{result}类，中文名称为{chinese_name.loc[index,:].iloc[:,1]}')

#%% 导入中文名称
chinese_name=pd.read_csv('D:/tiqam_data/week4/102flowers/imagelabels.csv',encoding='gbk')
index=chinese_name['label']==result
name_list=list(chinese_name['种类'])
st.sidebar.write(f'该花识别结果为第{result}类')
name=list(np.array(name_list)[index])
st.sidebar.write(f'中文名称为：{name}')


    
#侧边栏加入对比图片
st.sidebar.title(f'{list(np.array(name_list)[index])}的对比照片如下：')
routine='D:/tiqam_data/week4/102flowers/train'
list2=os.listdir(f'{routine}/{result}')#获取所有分类
path=(f'{routine}/{result}/{list2[-1]}')
st.sidebar.image(plt.imread(path))


#%% 爬虫爬取种类介绍
import requests
import re
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62'}
url='https://cn.bing.com/search?q='
res=requests.get(f'{url}{name}', headers=headers).text
res2=requests.get(f'{url}{name}花语', headers=headers).text
introduce_source='<span data-translation="">(.*?)</span>'
introduce=re.findall(introduce_source,res,re.S)#%%
flower_imply=re.findall(introduce_source,res2,re.S )
with st.sidebar.expander('花之介绍'):
    st.write(f'{introduce}')
with st.sidebar.expander('花之语'):
    st.write(f'{flower_imply}')


#%% 反馈栏目
col2.title('反馈：')
with col2.form(f'反馈'):
    res=st.radio('准吗',['准','完全不准'])
    if st.form_submit_button('点击提交'):
        if res=='准':
            st.write('感谢您的使用，祝生活愉快')
            st.balloons()
        else:
            st.write('感谢您的反馈，我们会努力提升识别正确率的')
            st.snow()
            
