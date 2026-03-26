import streamlit as st
import pandas as pd
import pyarrow

data = {
    "이름": ["김철수", "이영희", "박민수", "정지은", "최동욱", "강서연", "윤태희", "장민지"],
    "나이": [25, 23, 26, 24, 27, 22, 25, 23],
    "학년": ["3학년", "2학년", "4학년", "3학년", "4학년", "1학년", "3학년", "2학년"],
    "수학": [85, 92, 78, 95, 88, 70, 91, 87],
    "영어": [90, 88, 85, 92, 86, 75, 89, 90],
    "과학": [88, 90, 92, 89, 91, 80, 85, 88]
}

df = pd.DataFrame(data)
st.dataframe(df,use_container_width=True)
st.divider()

#위젯
# 텍스트 입력
st.subheader("텍스트 입력")
student_name = st.text_input("학생 이름을 입력하세요", placeholder="예) 김철수", help="검색하고 싶은 이름을 입력하세요")

# 입력된 이름으로 데이터를 필터링
if student_name:
    filtered_by_name = df[df['이름'].str.contains(student_name)] #data 이름 안에 포함되어 있나 student_name 비교
    if not filtered_by_name.empty :
        st.success('성공')
        st.dataframe(filtered_by_name,use_container_width=True)
    else:
        st.error('실패')

st.divider()

# 슬라이더
min_age =  st.slider('최소나이를 선택하세요',
          min_value=int(df['나이'].min()),
          max_value=int(df['나이'].max()),
          value=int(df['나이'].mean()),
          step=1
          )

# 나이로 필터링
filtered_by_age =  df[df['나이'] >= min_age]
st.dataframe(filtered_by_age,use_container_width=True)

# 셀럭트 박스
selected_grade =  st.selectbox('학년을 선택하세요',
                               options= ['전체'] + sorted(df['학년'].unique().tolist()))

# 학년으로 필터링
if selected_grade == "전체":
    filtered_by_grade = df
else:
    filtered_by_grade = df[df['학년'] == selected_grade]

st.dataframe(filtered_by_grade,use_container_width=True)

st.divider()

# 멀티 셀렉트
selected_subject = st.multiselect(
    "과목을 선택하세요",
    options=['수학','과학','영어'],
    default=['수학','과학']
)
selected_subject = ['이름','나이','학년'] + selected_subject
flitered_by_subject = df[selected_subject]
st.dataframe(flitered_by_subject)

st.divider()

# 버튼
st.header("3. 버튼 활용하기")

col1, col2, col3 = st.columns(3)

with col1:
    # 일반 버튼
    if st.button(" 전체 통계 보기", use_container_width=True):
        st.success("전체 통계를 표시합니다!")
        st.write(" 과목별 평균 점수")
        avg_scores = df[["수학", "영어", "과학"]].mean()
        st.dataframe(avg_scores.to_frame(name="평균"), use_container_width=True)

with col2:
    # 두 번째 버튼
    if st.button("최우수 학생 찾기", use_container_width=True):
        df['총점'] = df['수학'] + df['영어'] + df['과학']
        top_student = df.loc[df['총점'].idxmax()] # loc 해당 인덱스 행 가져옴 .idxmax() 값이 가장 큰행의 인덱스
        st.success(f"최우수 학생: {top_student['이름']}")
        st.metric("총점", f"{top_student['총점']}점")

with col3:
    # 세 번째 버튼
    if st.button("성적 순위 보기", use_container_width=True):
        df_with_avg = df.copy()
        df_with_avg['평균'] = df[['수학', '영어', '과학']].mean(axis=1) # 각 학생별 평균
        df_sorted = df_with_avg.sort_values('평균', ascending=False) # 평균을 내림차순으로 보여줌
        st.dataframe(df_sorted[['이름', '평균']], use_container_width=True)

st.divider()

# 체크박스
st.header("4. 체크박스로 옵션 켜고 끄기")

show_raw_data = st.checkbox("원본 데이터 보기", value=True)  # value=True로 기본 체크

if show_raw_data:
    st.write("원본 데이터")
    st.dataframe(df, use_container_width=True)

st.info("Tip: 버튼은 클릭할 때마다 페이지가 리렌더링됩니다. 상태를 유지하려면  session_state를 사용하세요!")