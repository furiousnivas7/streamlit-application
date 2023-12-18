import streamlit as st

st.title("pass or fail")
Name=st.text_input("enter your name" )
st.write("Hello",Name)
mark=st.number_input("enter the mark" )
st.write("your mark1 is",mark)
mark2=st.number_input("enter the second marks")
st.write("your mark2 is", mark2)
mark3=st.number_input("enter the third marks")
st.write.("your third marks is",mark3)
