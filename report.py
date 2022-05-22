# -*- coding: utf-8 -*-
"""
Created on Mon May  9 11:11:24 2022

@author: bianca

小红书app调差问卷
"""

#%% 
import streamlit as st
import numpy as np
import pandas as pd
st.set_page_config(page_title='小红书调查问卷',    page_icon=':heart:')
with st.form('report'):
    st.title('小红书APP对大学生及上班族旅游消费行为的影响调查问卷')
    st.write('使用小红书app的用户大家好！小红书作为一款当红app大家可以在在小红书社区通过文字、图片、视频笔记的分享，来记录这个时代年轻人的正能量和美好生活，而旅游作为一种享受生活的方式在小红书上的占比也是日益增加，下面我将对小红书app对大家的旅游前后的行为以及消费影响进行调查，希望大家能抽出宝贵的几分钟完成下面的问卷，谢谢大家！')
    st.write('______________________')
    
    #第1题
    #st.write('1.性别')
    #st.selectbox('1.性别', ['男','女'])
    res1=st.radio('1.性别', ['男','女'])
    #第2题
    res2=st.number_input('2.您的年龄',min_value=18,max_value=50)
    
    #第3题
    res3=st.radio('3. 你每个月生活费（工资）是多少？ （单位为元）',
             ['2000以下',
    '2000-3000（不包括3000）',
    '3000-4000（不包括4000）',
    '4000-5000（不包括5000）',
    '5000及以上'])
    #第4题
    res4=st.radio('4. 你每次的旅游花费是多少？（单位为元）',['1000以下',
    '1000-2000（不包括2000）',
    '2000-3000（不包括3000）',
    '3000-4000（不包括4000）',
    '4000及以上'
        ])
    #第5题
    res5=st.radio('5. 你在出游前会不会使用小红书攻略参考？',
             ['一定使用（只要有出游想法就一定会用小红书）',
    '经常使用（大多数出游前都会参考小红书）',
    '偶尔使用（只有极小部分出游前参考）',
    '从不使用']
             )
    #第6题
    res6=st.radio('6. 参考小红书来进行旅游，你更看重的是？',
             ['查看小红书上的攻略后更省钱,省时',
    '能发现一些小众宝藏地',
    '自己没什么想法，需要依赖出行路线规划',
    '想打卡小红书上的博主去过的地方',
    '其他'])
    
    #第7题
    choices7=['网红马路、打卡拍照（外滩、武康路等）',
    '美食探店',
    '博物馆、艺术馆、展览',
    '公园等自然风光',
    '主题乐园（迪士尼等）',
    '古镇、特色小镇',
    '体验馆（蜡像馆、星空馆等）',
    '其他文化场所（名人故居、历史建筑遗迹等）']
    #res=st.multiselect('7. 你会根据小红书的推荐与分享去哪里玩？', choices)
    
    st.write('7. 你会根据小红书的推荐与分享去哪里玩？')
    res7=[]
    for c in choices7:
        res7.append(st.checkbox(c))
        
    # st.write(res)
    # st.write(res2)
    
    #第8题
    res8=st.slider('8. 你最终的旅游行为有多大程度参考了小红书APP上的旅游信息？（参考程度从高到低）',min_value=1,max_value=5)
    
    #第9题
    choices9=['景点图片精美',
    '推荐人是好看的小哥哥小姐姐',
    '文字信息务实有用',
    '笔记是标题党设有悬念',
    '图文排版设计感强',
    '短视频形式更加直观、吸引力强',
    '其他']
    st.write('9. 小红书上旅游相关的笔记有哪些闪光点吸引你呢？')
    res9=[]
    for i in choices9:
        res9.append(st.checkbox(i))
        
        
    #第10题
    res10=st.radio('10. 你会不会去小红书中推荐的网红店消费？',
             ['从不消费',
    '偶尔消费',
    '经常消费'])
    #第11题
    res11=st.slider('11. 你觉得小红书推荐的网红店消费体验感如何（信息真实度、性价比等等）',min_value=1,max_value=5)
    #第12题
    res12=st.radio('12. 在使用小红书后，你是否觉得自己的旅游消费增加了？',
             ['使不使用小红书，旅游消费支出都差不多',
    '使用小红书后的旅游消费支出增多了',
    '使用小红书红的旅游消费支出减少了'])
    #第13题
    res13=st.slider('13. 目的地及相关消费的实际情况与小红书描述的符合程度如何？（有没有被照骗）',min_value=1,max_value=5)
    #第14题
    res14=st.slider('14. 小红书旅游相关笔记对你出游的有用程度是多少呢？（即你收到了多少干货）',min_value=1,max_value=5)
    #第15题
    res15=st.slider('15. 你使用小红书进行旅游消费的满意度是多少分？',min_value=1,max_value=5)
    #第16题
    res16=st.radio('16. 游玩后你是否会上传分享笔记或防雷吐槽至小红书呢？',
             ['会','不会'])
    #第17题
    choices17=['编辑较为麻烦',
                '防止泄露个人隐私',
                '对某一景点体验一般、感触不深',
                '广告与用户推荐鱼龙混杂，不愿参与',
                '不愿发表个人意见，以免产生分歧',
                '其他情况']
    #st.multiselect('17.你不会上传分享推荐笔记或防雷吐槽的原因是？', choices17)
    st.write('17.你不会上传分享推荐笔记或防雷吐槽的原因是？')
    res17=[]
    for k in choices17:
        res17.append(st.checkbox(k))
    
    #第18题
    choices18=['p图过度，网红滤镜照骗',
                '广告泛滥',
                '信息复杂有用程度低',
                '不喜欢页面设计等',
                '其他原因']
    st.write('18. 你最想吐槽小红书在旅游推荐上的什么雷点？')
    
    res18=[]
    for j in choices18:
        res18.append(st.checkbox(j))
        
    #第19题
    choices19=['景点图片美化过于严重，p图过度',
                '广告泛滥，多数与旅游内容无关',
                '信息价值不大（发布内容已经知道）',
                '网红博主存在虚假宣传，打广告等嫌疑',
                '对小红书不了解，对其他APP信任度更高',
                '其他考虑']
    
    st.write('19. 你抛弃小红书APP的原因是什么呢？')
    res19=[]
    for c in choices19:
        res19.append(st.checkbox(c))
    
    #第20题
    res20=st.text_input('20. 你对于小红书还有什么想要提出的建议或踩雷经历分享？')
    #第21题
    res21=st.text_input(('21. 相较于小红书，请列举一下你所使用的其他同类旅游社区APP及其优势功能'))
    
    res=[[res1,res2,res3,res4,res5,res6,res7,res8,res9,res10,res11,res12,res13,res14,res15,res16,res17,res18,res19,res20,res21]]
    
   #st.button('点击提交')
    if st.form_submit_button('点击提交'):
        data=pd.DataFrame(res)
        #st.write(data)
        data.to_csv("D:/image/report_result.csv",mode="a")#mode='a'追加  
        st.write('thanks')
        st.balloons()
        
        with st.expander('是否查看数据'):
            st.dataframe(data)
            
        # st.download_button('下载数据', data,file_name='')