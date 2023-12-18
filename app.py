import streamlit as st
import json
import os


st.title("Pass or Fail")
Name=st.text_input("enter your name" ,placeholder="enter the Name")
mark=st.number_input("enter the mark",placeholder="enter the number", value=None )
mark2=st.number_input("enter the second marks",placeholder="enter the number",value=None)
mark3=st.number_input("enter the third marks",placeholder="enter the number",value=None)
tot=None
Avg=None

st.button("submit", type="primary")
if st.button('submit'):
    if (mark and mark2 and mark3)!=0:
        tot=mark+mark2+mark3
        avg=tot/3
    if avg>45:
        st.write("your are Pass the exam")
    else:
        st.write("your are,fail the exam")

    st.write("Hello",Name)
    st.write("your mark1 is",mark)
    st.write("your mark2 is", mark2)
    st.write("your third marks is",mark3)
    st.write("your total is",tot)
    st.write("your avgrage is ",avg)
else:
    st.write('Goodbye')






