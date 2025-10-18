import streamlit as st
import streamlit.components.v1 as components
import os

def main():
    """
    Streamlit 애플리케이션의 메인 함수.
    'htmls' 폴더의 HTML 파일을 선택하여 표시합니다.
    """
    st.set_page_config(layout="wide")

    # 'htmls' 폴더 경로 설정
    # Path to the 'htmls' folder
    htmls_folder_path = os.path.join(os.path.dirname(__file__), 'htmls')

    # 'htmls' 폴더에서 HTML 파일 목록 가져오기
    # Get a list of HTML files in the 'htmls' folder
    try:
        # .html, .htm 으로 끝나거나 확장자가 없는 파일을 포함하도록 수정
        html_files = [
            f for f in os.listdir(htmls_folder_path) 
            if f.endswith(('.html', '.htm')) or '.' not in f
        ]
    except FileNotFoundError:
        st.error("'htmls' 폴더를 찾을 수 없습니다. 'app.py'와 같은 디렉토리에 'htmls' 폴더를 생성해주세요.")
        html_files = []

    if not html_files:
        st.warning("'htmls' 폴더에 HTML 파일이 없습니다.")
    else:
        # 사이드바에서 HTML 파일을 선택하는 selectbox 사용
        # Use a selectbox in the sidebar to choose the HTML file
        st.sidebar.title("HTML 파일 선택")
        selected_file = st.sidebar.selectbox("표시할 HTML 파일을 선택하세요:", html_files)

        # 선택된 HTML 파일의 전체 경로 구성
        # Construct the full path to the selected HTML file
        selected_html_path = os.path.join(htmls_folder_path, selected_file)

        # 선택된 HTML 파일의 내용을 읽고 표시
        # Read and display the content of the selected HTML file
        try:
            with open(selected_html_path, 'r', encoding='utf-8') as f:
                html_content = f.read()

            # Streamlit 컴포넌트를 사용하여 HTML 내용 표시
            # Display the HTML content using a Streamlit component
            st.title(f"'{selected_file}' 보기")
            components.html(html_content, height=800, scrolling=True)

        except FileNotFoundError:
            st.error(f"'{selected_file}' 파일을 찾을 수 없습니다.")

if __name__ == '__main__':
    main()

