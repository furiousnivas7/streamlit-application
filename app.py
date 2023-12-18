import streamlit as st

st.title("Pass or Fail")
Name=st.text_input("enter your name" ,placeholder="enter the Name")
mark=st.number_input("enter the mark",placeholder="enter the number" )
mark2=st.number_input("enter the second marks",placeholder="enter the number")
mark3=st.number_input("enter the third marks",placeholder="enter the number")
tot=mark+mark2+mark3
avg=tot/3

st.write("Hello",Name)
st.write("your mark1 is",mark)
st.write("your mark2 is", mark2)
st.write("your third marks is",mark3)
st.write("your total is",tot)
st.write("your avgrage is ",avg)