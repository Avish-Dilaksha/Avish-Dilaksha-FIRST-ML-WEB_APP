# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 17:09:16 2022

@author: Avish Dilaksha
"""
import streamlit as st
#import joblib
import pickle
import pandas as pd



def main():
    html_temp = """
    <div style = "background-color:SlateGray;padding:20px">
    <h2 style = "color:black;text-allign:center">
        Health insurance cost prediction using Machine Learning
    </h2>
    </div>
    
    """
    st.markdown(html_temp,unsafe_allow_html= True)
    
    model = pickle.load(open('model_joblib_pk','rb'))
    #model = joblib.load('model_joblib_Gr')
    
    p1 = st.number_input('Enter your Age',0,100)

    
    s1 = st.selectbox('Sex',('Male','Female'))
    
    if(s1 == "Male"):
        p2 = 1
    else:
        p2 = 0
        
    p3 = st.number_input('Enter your BMI value')
    
    p4 = st.number_input('Enter number of children',1,10,value = 1,step = 1)
    
    
    s2 = st.selectbox('Smoker',('Yes','No'))
    
    if(s2 == "Yes"):
        p5 = 1
    else:
        p5 = 0
        
    s3 = st.selectbox('Region',('southwest','northwest','northeast','southeast'))
    
    if(s3 == "southwest"):
        p6 = 1
    elif(s3 == 'northwest'):
        p6 = 3
    elif(s3 == 'northeast'):
        p6 = 4
    else:
        p6 = 2
        
    if st.button('Predict'):
        #pred = model.predict(pd.DataFrame([[p1,p2,p3,p4,p5,p6]],columns= ['age','sex','bmi','children','smoker','region']))
        pred = model.predict([[p1,p2,p3,p4,p5,p6]])
        
        
        st.success('Your insurance cost is :  {}'.format(round(pred[0],2)))
    
    
    
if __name__ == '__main__':
    main()

