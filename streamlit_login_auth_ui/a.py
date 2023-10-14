import streamlit as st
import base64
from PIL import Image
import requests


def show_pdf(file_path):
    with open(file_path,"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)
topic = st.sidebar.selectbox("Menu:", ["Home", "About"])
if topic=='Home':
    feature_image1 = Image.open(r'C:\Users\marba\OneDrive\Desktop\New folder (2)\streamlit_pdf_display\2022.PNG')
    with st.container():
        image_col, text_col = st.columns((1,3))
        with image_col:
            st.image(feature_image1,caption='Image by Pixabay')
        with text_col:
            st.markdown(""" <style> .font {
            font-size:22px ; font-family: 'Black'; color: #FFFFF;} 
            </style> """, unsafe_allow_html=True)
            st.markdown('<p class="font">Clean a ‘Numeric’ ID Column in Pandas Dataframe</p>', unsafe_allow_html=True)    
            st.markdown("By Sharone Li - As a data scientist, you must have encountered this problem at least once in your data science journey: you import your data into a Pandas dataframe... [Continue to Read on Towards Data Science](https://towardsdatascience.com/clean-a-numeric-id-column-in-pandas-dataframe-fbe03c11e330)")

    col1, col2,col3= st.columns(3)
    with col1:  
        if st.button('Read PDF Tutorial',key='1'):            
            show_pdf('LSE_BARC_2022.pdf')
    with col2:
        st.button('Close PDF Tutorial',key='2')                   
    with col3:
        with open("LSE_BARC_2022.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(label="Download PDF Tutorial", key='3',data=PDFbyte,file_name="pandas-clean-id-column.pdf",mime='application/octet-stream')

    feature_image2 = Image.open(r'C:\Users\marba\OneDrive\Desktop\New folder (2)\streamlit_pdf_display\2021.PNG')
    with st.container():
        image_col, text_col = st.columns((1,3))
        with image_col:
            st.image(feature_image1,caption='Image by Pixabay')
        with text_col:
            st.markdown(""" <style> .font {
            font-size:22px ; font-family: 'Black'; color: #FFFFF;} 
            </style> """, unsafe_allow_html=True)
            st.markdown('<p class="font">Clean a ‘Numeric’ ID Column in Pandas Dataframe</p>', unsafe_allow_html=True)    
            st.markdown("By Sharone Li - As a data scientist, you must have encountered this problem at least once in your data science journey: you import your data into a Pandas dataframe... [Continue to Read on Towards Data Science](https://towardsdatascience.com/clean-a-numeric-id-column-in-pandas-dataframe-fbe03c11e330)")

    col1, col2,col3= st.columns(3)
    with col1:  
        if st.button('Read PDF Tutorial',key='4'):            
            show_pdf('NYSE_HSBC_2021.pdf')
    with col2:
        st.button('Close PDF Tutorial',key='5')                   
    with col3:
        with open("NYSE_HSBC_2021.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(label="Download PDF Tutorial", key='6',data=PDFbyte,file_name="pandas-clean-id-column.pdf",mime='application/octet-stream')
        
        
    feature_image3 = Image.open(r'C:\Users\marba\OneDrive\Desktop\New folder (2)\streamlit_pdf_display\2020.PNG')
    with st.container():
        image_col, text_col = st.columns((1,3))
        with image_col:
            st.image(feature_image1,caption='Image by Pixabay')
        with text_col:
            st.markdown(""" <style> .font {
            font-size:22px ; font-family: 'Black'; color: #FFFFF;} 
            </style> """, unsafe_allow_html=True)
            st.markdown('<p class="font">Clean a ‘Numeric’ ID Column in Pandas Dataframe</p>', unsafe_allow_html=True)    
            st.markdown("By Sharone Li - As a data scientist, you must have encountered this problem at least once in your data science journey: you import your data into a Pandas dataframe... [Continue to Read on Towards Data Science](https://towardsdatascience.com/clean-a-numeric-id-column-in-pandas-dataframe-fbe03c11e330)")

    col1, col2,col3= st.columns(3)
    with col1:  
        if st.button('Read PDF Tutorial',key='7'):            
            show_pdf('Sale Invoice INV-04347-M0X0X4.pdf')
    with col2:
        st.button('Close PDF Tutorial',key='8')                   
    with col3:
        with open("Sale Invoice INV-04347-M0X0X4.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(label="Download PDF Tutorial", key='9',data=PDFbyte,file_name="pandas-clean-id-column.pdf",mime='application/octet-stream')   