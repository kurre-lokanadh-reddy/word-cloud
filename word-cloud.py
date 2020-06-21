# -*- coding: utf-8 -*-
"""
Created on Sat May 30 21:47:09 2020

@author: kurre lokanadh reddy
"""
from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt
import streamlit as st



st.title("Word Cloud Generator")
st.write("you can input either a 'list' of words,a 'text' or go completly unconventional using 'unC'")
input_type=st.selectbox("input type",['text','list of words','Un C mode'])
if input_type=="list of words":
    input_content=st.text_input("enter list here:")
    input_content=str(" ".join(input_content))
elif input_type=="text":
    input_content=st.text_area("enter text here:")
else :
    st.write("In this you are suposed to give a word followed by its percentage(example: If you are clouding for skills set then give 'python:90 cpp:85' )")
    input_content=st.text_area("enter the word1:percent1 ")
    strig=""
    for i in list(input_content.split()):
        word,val=i.split(":")
        strig+=" ".join([word]*int(int(val)/5))
    input_content=strig

st.sidebar.title("Word Cloud Generator")
max_words=st.sidebar.slider("max no of words:",10,50,25)
width=st.sidebar.slider("width of cloud:",100,1000,500)
height=st.sidebar.slider("height of cloud:",100,1000,500)
background=st.sidebar.text_input("background[white]:")
generate=st.sidebar.button("generate cloud")
if generate:
    img=WordCloud(width=width,height=height,repeat=False, max_words=max_words,min_font_size=7,background_color="white",stopwords=set(STOPWORDS)).generate(input_content)
    plt.figure(figsize=(8,8),facecolor=None)
    plt.imshow(img)
    plt.axis("off")
    st.pyplot()
    
