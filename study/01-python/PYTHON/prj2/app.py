import streamlit as st
import pandas as pd

# 페이지 제목을 설정 (브라우저 탭에 표시)
st.set_page_config(page_title = "기초화면구성")

# 타이틀 출력 (가장 큰 제목)
st.title("화면구성")

# 헤더 출력(중간 크기 제목)
st.header("다양한 텍스트 출력 방법")

# 일반 텍스트 출력
st.write('st.write는 가장 기본적인 출력')
st.write('숫자 문자열 데이터프레임 등 거의 모든 것을 출력')

# 서브헤더(작은 제목)
st.subheader("2. 마크다운 활용하기")

# 마크 다운 문법으로 다양한 스타일 적용
st.markdown('''
### 마크 다운으로 할수 있는 것들:
            - ** 굵은글씨**
            - *기울림 글씨*
            - `코드 표시`
            - [링크 만들기](http://streamlit.io)

            > 이것은 인용구 입니다.
            ''')
st.markdown("**굵은 글씨**")
st.markdown("*기울림 글씨*")
st.markdown("""
            ``` python
            import streamlit as pd
            pd.DataFraame(array)
            ```
            """)
st.markdown("[링크만들기](http://streamlit.io)")

# 취소선
st.divider()

# 데이터 프레임 생성 및 출력
st.header("3. pandas 데이터프레임 출력")

# 가상의 데이터
data = {
    "이름": ["김철수", "이영희", "박민수", "정지은", "최동욱"],
    "나이": [25, 23, 26, 24, 27],
    "수학": [85, 92, 78, 95, 88],
    "영어": [90, 88, 85, 92, 86],
    "과학": [88, 90, 92, 89, 91]
}
df = pd.DataFrame(data)

# 데이터프레임 출력 방법 : st.write()사용
st.subheader("방법 1: st.write()로 출력")
st.write(df)

# 데이터프레임 출력 방법 : st.dataframe()사용
st.subheader("방법 2: st.dataframe() 스크롤 정렬 가능")
st.dataframe(df, use_container_width=True )

# 데이터프레임 출력 방법 : st.table()사용
st.subheader("방법 2: st.table() 정적테이블")
st.table(df)

st.divider() # 구분선

# 매트릭 카드( 주요 지표 표시)
st.header('4. 매트릭 카드로 주요 지표 표시')
col1,col2,col3 = st.columns(3)
with col1:
    st.metric(label="총 학생수", value=len(df))
with col2:
    st.metric(label="평균 수학 점수", value=f"{df['수학'].mean():.1f}점")  
with col3:
    st.metric(label="최고 영어 점수", value=f"{df['영어'].max()}점")

# 정보박스
st.info('Tip : st.write()는 만능 출력 함수, 특정 용도에는 전용 함수 st.dataframe st.metric')

