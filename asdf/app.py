import streamlit as st
import streamlit.components.v1 as components
import os

def main():
    """
    Streamlit 애플리케이션의 메인 함수.
    'htmls' 폴더의 HTML 파일을 선택하여 표시합니다.
    """
    st.set_page_config(layout="wide")

    # Path to the 'htmls' folder
    htmls_folder_path = os.path.join(os.path.dirname(__file__), 'htmls')

    # Get a list of HTML files in the 'htmls' folder
    try:
        html_files = [f for f in os.listdir(htmls_folder_path) if f.endswith('.html')]
    except FileNotFoundError:
        st.error("'htmls' 폴더를 찾을 수 없습니다. 'app.py'와 같은 디렉토리에 'htmls' 폴더를 생성해주세요.")
        html_files = []

    if not html_files:
        st.warning("'htmls' 폴더에 HTML 파일이 없습니다.")
    else:
        # Use a selectbox in the sidebar to choose the HTML file
        st.sidebar.title("HTML 파일 선택")
        selected_file = st.sidebar.selectbox("표시할 HTML 파일을 선택하세요:", html_files)

        # Construct the full path to the selected HTML file
        selected_html_path = os.path.join(htmls_folder_path, selected_file)

        # Read and display the content of the selected HTML file
        try:
            with open(selected_html_path, 'r', encoding='utf-8') as f:
                html_content = f.read()

            # Display the HTML content using a Streamlit component
            st.title(f"'{selected_file}' 보기")
            components.html(html_content, height=800, scrolling=True)

        except FileNotFoundError:
            st.error(f"'{selected_file}' 파일을 찾을 수 없습니다.")

if __name__ == '__main__':
    main()
