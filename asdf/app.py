import streamlit as st
import os

# Set page configuration
st.set_page_config(layout="wide")

# Path to the HTML file inside the 'htmls' folder
html_file_path = os.path.join(os.path.dirname(__file__), 'htmls', 'index.html')

# Check if the HTML file exists
if not os.path.exists(html_file_path):
    st.error("HTML 파일을 찾을 수 없습니다. 'htmls' 폴더 안에 'index.html' 파일이 올바르게 있는지 확인해주세요.")
else:
    # Read the content of the HTML file
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Use a Streamlit component to display the HTML content
    st.components.v1.html(html_content, height=1000, scrolling=True)
