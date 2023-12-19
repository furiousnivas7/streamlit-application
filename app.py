import streamlit as st
import pandas as pd
import json
import os

st.title("Pass or Fail")

# Function to load and save data
json_file_path = 'data.json'

def load_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    else:
        return []

def save_data(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Load existing data
data = load_data(json_file_path)

# Input fields
Name = st.text_input("Enter your name", placeholder="Enter the Name")
mark = st.number_input("Enter the mark", min_value=0, max_value=100, value=0, format="%d")
mark2 = st.number_input("Enter the second mark", min_value=0, max_value=100, value=0, format="%d")
mark3 = st.number_input("Enter the third mark", min_value=0, max_value=100, value=0, format="%d")

# Submit button
if st.button('Submit'):
    if mark != 0 and mark2 != 0 and mark3 != 0:
        tot = mark + mark2 + mark3
        avg = tot / 3
        result = "Pass" if avg >= 45 else "Fail"
        
        # Add data to the list and save to JSON
        new_entry = {
            "Name": Name,
            "Mark1": mark,
            "Mark2": mark2,
            "Mark3": mark3,
            "Total": tot,
            "Average": avg,
            "Result": result
        }
        data.append(new_entry)
        save_data(json_file_path, data)

        # Display the result
        st.success(f"Hello {Name}, you have {result}ed the exam.")
        st.write(f"Your marks are: {mark}, {mark2}, {mark3}. Total: {tot}, Average: {avg}")
    else:
        st.error("Please enter valid marks for all subjects.")

# Display table with data
if data:
    df = pd.DataFrame(data)
    st.table(df)

#if st.button('Download JSON Data'):
    with open(json_file_path, "r") as file:
        st.download_button(
            label="Download Data as JSON",
            data=file,
            file_name='student_data.json',
            mime='application/json'
        )