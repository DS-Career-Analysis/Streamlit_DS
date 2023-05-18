import streamlit as st
import pandas as pd
import numpy as np

from time import sleep
from PIL import Image
import threading

def detect_defects():
    # 불량 탐지 코드 작성
    # 결과를 반환하거나, 파일에 저장하는 등의 동작 수행
    defect_thread=threading.Thread(target=detect_defects)

st.set_page_config(
    page_title="DS Career Analysis",
    layout="wide",
)

st.title("DS 커리어 분석💻")
st.image('logo.png', width=1000)

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(['Intro', 'DS', 'DA' , 'DE', '대기업 공고', '나의 역량'])

with tab1:
  st.subheader("DS 커리어 분석")
  st.markdown("Members : 홍재민, 박예린, 윤기창")
  st.write("Our Github Link : <a href='https://github.com/DS-Career-Analysis/' target='_blank'>https://github.com/DS-Career-Analysis/</a>", unsafe_allow_html=True)
  st.subheader("Method")
  st.markdown("원티드, 사람인, 잡플래닛, 인크루트에서 Data Scientist, Data Engineer, Data Analyst 3가지 직무의 공고를 크롤링하고 해당 공고들의 텍스트 분석을 진행하였습니다.")
  st.markdown("또한 수집한 데이터를 활용하여 어떤 지역에 해당 직무의 공고가 집중되어있는지 지도에 표시하였습니다.")

with tab2:
  st.subheader("Data Scientist")

  # 첫 번째 이미지 파일 업로드
  korean_text_ds = Image.open('DS_K.png')

  # 두 번째 이미지 파일 업로드
  english_text_ds = Image.open('DS_E.png')

  if korean_text_ds is not None and english_text_ds is not None:
    # 두 개의 이미지 파일이 모두 업로드된 경우
    col1, col2 = st.columns(2)
    
    # 첫 번째 컬럼에 첫 번째 이미지 배치
    col1.image(korean_text_ds, use_column_width=True)
    
    # 두 번째 컬럼에 두 번째 이미지 배치
    col2.image(english_text_ds, use_column_width=True)
  else:
    # 이미지 파일이 업로드되지 않은 경우
    st.write("Please upload two image files.")



with tab3:
   st.subheader("Data Analyst")
   
   # 첫 번째 이미지 파일 업로드
   korean_text_da = Image.open('DA_K.png')

   # 두 번째 이미지 파일 업로드
   english_text_da = Image.open('DA_E.png')

   if korean_text_da is not None and english_text_da is not None:
      # 두 개의 이미지 파일이 모두 업로드된 경우
      col1, col2 = st.columns(2)
      
      # 첫 번째 컬럼에 첫 번째 이미지 배치
      col1.image(korean_text_da, use_column_width=True)
      
      # 두 번째 컬럼에 두 번째 이미지 배치
      col2.image(english_text_da, use_column_width=True)
   else:
      # 이미지 파일이 업로드되지 않은 경우
      st.write("Please upload two image files.")
   
with tab4:
   st.subheader("Data Engineer")
   
   # 첫 번째 이미지 파일 업로드
   korean_text_de = Image.open('DE_K.png')

   # 두 번째 이미지 파일 업로드
   english_text_de = Image.open('DE_E.png')

   if korean_text_de is not None and english_text_de is not None:
      # 두 개의 이미지 파일이 모두 업로드된 경우
      col1, col2 = st.columns(2)
      
      # 첫 번째 컬럼에 첫 번째 이미지 배치
      col1.image(korean_text_de, use_column_width=True)
      
      # 두 번째 컬럼에 두 번째 이미지 배치
      col2.image(english_text_de, use_column_width=True)
   else:
      # 이미지 파일이 업로드되지 않은 경우
      st.write("Please upload two image files.")

with tab5:
   st.subheader("현재 진행중인 대기업 공고")

with tab6:
   st.subheader("현재 자신의 역량을 선택하여주세요")

   # 체크박스 생성
   python_skill = st.checkbox("Python")
   java_skill = st.checkbox("Java")
   cpp_skill = st.checkbox("C++")
   html_skill = st.checkbox("HTML")
   css_skill = st.checkbox("CSS")
