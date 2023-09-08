import easyocr as ocr  #OCR
import streamlit as st  #Web App
from PIL import Image #Image Processing
import numpy as np #Image Processing 
st. set_page_config(layout="wide")
import re
import pymysql
import io
import mysql.connector

# Getting Secrets from Streamlit Secret File
#

# Connect to AWS-RDS-MYSQL
connect = mysql.connector.connect(
            host="localhost",
            user="root",
            password="aditya1234",
            database='dbase'
        )
cursor = connect.cursor()

#title
def format_title(title: str):
    """
    Formats the given title with a colored box and padding
    """
    formatted_title = f"<div style='padding:10px;background-color:rgb(230, 0, 172, 0.3);border-radius:10px'><h1 style='color:rgb(204, 0, 153);text-align:center;'>{title}</h1></div>"
    return formatted_title

# Use the function to format your title
st.markdown(format_title("UNLOCKING DATA FROM BUSINESS CARDS USING OCR"), unsafe_allow_html=True)

st.write(" ")
st.write(" ")
st.write(" ")
st.write("### UPLOAD ANY BUSINESS CARD IMAGE TO EXTRACT INFORMATION ")
CD,col1, col2,col3= st.columns([0.5,4,1,4])
with col1:
    #image uploader
    st.write("#### SELECT IMAGE")
    image = st.file_uploader(label = "",type=['png','jpg','jpeg'])

@ st.cache_data
def load_model(): 
    reader = ocr.Reader(['en'])
    return reader 

reader = load_model() #load model
if image is not None:
    input_image = Image.open(image) #read image
    with col1:
        st.image(input_image) #display image  
        st.write(" ")

    result = reader.readtext(np.array(input_image))
    result_text = [] #empty list for results
