import streamlit as st

st.title("Pass or Fail")
Name=st.text_input("enter your name" ,placeholder="enter the Name")
st.write("Hello",Name)
mark=st.number_input("enter the mark",placeholder="enter the number" )
st.write("your mark1 is",mark)
mark2=st.number_input("enter the second marks",placeholder="enter the number")
st.write("your mark2 is", mark2)
mark3=st.number_input("enter the third marks",placeholder="enter the number")
st.write("your third marks is",mark3)
