import streamlit as st

st.title('DS Career Analysis')
st.subheader(':violet[Dais OpenLab]')
st.caption('😎 박예린 윤기창 홍재민 😎')

# 깃허브 링크
st.caption('👉 [Github](https://github.com/DS-Career-Analysis)')

tab1, tab2, tab3, tab4 = st.tabs(['🖊️ 소개', '🗂️ DS ▪️ DA ▪️ DE', '🔍 나의 역량', '🏙️ 대기업 모음'])

with tab1:
    # 프로젝트 설명
    st.markdown('Data Scientist의 역량을 알아보기 위해 wanted, saramin, Jobplanet, Incruit의 채용공고를')
    st.markdown('**데이터 사이언티스트, 데이터 애널리스트, 데이터 엔지니어**로 각각 수집하였습니다.')

    st.write('''
    이 앱은 3가지를 제공합니다.
    1. 원하는 직무의 역량을 제공한다.
    2. 자신의 역량에 맞는 채용공고를 추천한다.
    3. 특정 대기업의 채용공고만 추천한다.
    ''')

    st.markdown('---')


    # 크롤링 진행 과정 
    def file_upload(f):
        file_open = open(f'{f}', 'rb')
        file_read = file_open.read()
        return file_read

    st.subheader('채용공고 수집')
    st.markdown('코드 보여주고, 돌아가는 모습을 보여줄 예정입니다.')

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
    st.subheader('텍스트 분석')
    st.markdown('채용공고 수집과 마찬가지로, 코드를 보여주고 영상 밑에 워드클라우드를 보여줄 예정입니다.')
    f = 'C:\\Users\\LG\\Videos\\Captures\\wanted.mp4'
    st.video(file_upload(f))
    f = 'C:\\Users\\LG\\Videos\\Captures\\TA_EDA.png'
    st.image(file_upload(f))

with tab2:
    genre = st.radio(
    "관심있는 키워드를 선택해주세요.",
    ('데이터 사이언티스트', '데이터 애널리스트', '데이터 엔지니어'))

    if genre == '데이터 사이언티스트':
        st.write('''
            개발 언어: Python, ...
            \n역량: 영어 및 한글
            \n데이터 사이언티스트에 맞는 채용공고를 추천해드릴게요!
            \n[채용공고 (제목, 링크, 회사 위치)]
        ''')

    elif genre == '데이터 애널리스트':
        st.write('''
            개발 언어: Python, ...
            \n역량: 영어 및 한글
            \n데이터 애널리스트에 맞는 채용공고를 추천해드릴게요!
            \n[채용공고 (제목, 링크, 회사 위치)]
        ''')

    else:
        st.write('''
            개발 언어: Python, ...
            \n역량: 영어 및 한글
            \n데이터 엔지니어에 맞는 채용공고를 추천해드릴게요!
            \n[채용공고 (제목, 링크, 회사 위치)]
        ''')

with tab3:
    options = st.multiselect(
        '자신의 역량을 선택해주세요! (중복 선택 가능)',
        ['정형데이터 분석', '이미지 분석', '텍스트 분석', '웹 제작', '의사소통']
        )

    st.write('나의 역량은 👇 ', options)

with tab4:
    st.markdown('오늘의 대기업 채용공고 입니다!')