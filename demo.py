import streamlit as st

st.title('DS Career Analysis')
st.subheader(':violet[Dais OpenLab]')
st.caption('😎 박예린 윤기창 홍재민 😎')

# 깃허브 링크
st.caption('👉 [Github](https://github.com/DS-Career-Analysis)')

tab1, tab2, tab3, tab4 = st.tabs(['🖊️ 소개', '🗂️ DS ▪️ DA ▪️ DE', '🔍 나의 역량', '🏙️ 대기업 모음'])

with tab1:
    # 프로젝트 설명
    st.write('''
    Data Scientist의 역량을 알아보기 위해 wanted, saramin, Jobplanet, Incruit의 채용공고를      \n**데이터 사이언티스트, 데이터 애널리스트, 데이터 엔지니어**로 각각 수집하였다.
    ''')

    st.write('''
    이 프로젝트의 최종 목표는
    1. 원하는 직무의 역량을 제공해줄 수 있다.
    2. 자신의 역량에 맞는 채용공고를 추천해줄 수 있다.
    3. 특정 대기업의 채용공고만 추천해줄 수 있다.
    ''')

    st.markdown('---')


    # 크롤링 진행 과정 
    # video로 보여주기 (아님 사이트 사진, 코드 사진으로?)
    def file_upload(f):
        file_open = open(f'{f}', 'rb')
        file_read = file_open.read()
        return file_read

    st.subheader('채용공고 수집')

    st.markdown('#### 👇 wanted')
    f = 'C:\\Users\\LG\\Videos\\Captures\\wanted.mp4'
    st.video(file_upload(f))

    st.markdown('#### 👇 saramin')
    f = 'C:\\Users\\LG\\Videos\\Captures\\wanted.mp4'
    st.video(file_upload(f))

    st.write('#### 👇 Jobplanet')
    f = 'C:\\Users\\LG\\Videos\\Captures\\wanted.mp4'
    st.video(file_upload(f))

    st.write('#### 👇 Incruit')
    f = 'C:\\Users\\LG\\Videos\\Captures\\wanted.mp4'
    st.video(file_upload(f))

    st.markdown('---')


    # 텍스트 분석 진행 과정
    # 코드 보여주고, 시각화한거 보여주기??
    st.subheader('텍스트 분석')
    f = 'C:\\Users\\LG\\Videos\\Captures\\TA_EDA.png'
    st.image(file_upload(f))