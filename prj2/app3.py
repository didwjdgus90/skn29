import streamlit as st
import pandas as pd


# 사이드바, 컬럼, 탭을 활용 화면 구성
st.set_page_config(
    page_title="레이아웃 디자인",
    layout='wide'
)
st.title("레이아웃 디자인")

data = {
    "이름": ["김철수", "이영희", "박민수", "정지은", "최동욱", "강서연", "윤태희", "장민지"],
    "나이": [25, 23, 26, 24, 27, 22, 25, 23],
    "학년": ["3학년", "2학년", "4학년", "3학년", "4학년", "1학년", "3학년", "2학년"],
    "수학": [85, 92, 78, 95, 88, 70, 91, 87],
    "영어": [90, 88, 85, 92, 86, 75, 89, 90],
    "과학": [88, 90, 92, 89, 91, 80, 85, 88]
}

df = pd.DataFrame(data)

# 사이드바
st.sidebar.title('설정메뉴')
st.sidebar.write('사이드바에 필터링 옵션을 모아둘수 있습니다.')

# 사이드바 필터 옵션
st.sidebar.header('데이터 필터')
sidebar_grade = st.sidebar.selectbox(
    '학년 선택', 
    options=['전체'] + sorted(df['학년'].unique().tolist())  # tolist 함수를 통해 넘파이에서 리스트로 변환
    )

# 최소나이
sidebar_min_age = st.sidebar.slider( #사이드 바에 최소나이 설정
    "최소 나이",
    min_value= int(df['나이'].min()), 
    max_value= int(df['나이'].max()),
    value= int(df["나이"].min())
)

# 과목
sidebar_subject = st.sidebar.multiselect( #사이드 바에 표시되는 과목 설정
    "표시할 과목",
    options=['수학','영어','과학'],
    default=['수학','영어','과학']
    )

# select_siderbar = ['이름','나이','학년'] + sidebar_subject

st.sidebar.divider()

# 추가 옵션
st.sidebar.header("추가 옵션")
show_stats = st.sidebar.checkbox('통계 표시', value=True) # value 체크가 되었으면 true 아니면 false
show_chart = st.sidebar.checkbox('차트 표시', value=True)

# 필터 적용
filtered_df =  df.copy()  # 원본 파일을 복사해서 저장한다.

if sidebar_grade != '전체':
    filtered_df = filtered_df[filtered_df['학년'] == sidebar_grade] # df키값으로 넘겨주면 -> true에 해당하는 row만 가져온다. 

filtered_df = filtered_df[filtered_df['나이'] >= sidebar_min_age] # df키값으로 넘겨주면 -> true에 해당하는 row만 가져온다.


# filtered_df = filtered_df[select_siderbar]
# 컬럼으로 화면 분할
st.header('컬럼으로 화면 분할하기')
st.write("화면을 여러개의 열로 나눠서 정보를 정리")

col1,col2,col3 = st.columns(3)

with col1:
    st.metric(
        "총 학생수",
        value = len(filtered_df),
        delta = f'{len(filtered_df) - len(df)} 필터 적용' #원본 대비 - 몇개가 적개 보인다.
    )

with col2:
    if sidebar_subject:
        avg_score = filtered_df[sidebar_subject].mean().mean()
        if pd.isna(avg_score): # 시스템이나 데이터가 누락된 값을 탐지하여 boolean 배열 함수로 반환
            st.metric("평균점수", value =  "N/A")
        else:     
            st.metric("평균점수", value =  f'{avg_score:.1f}점')  
    else:
        st.metric('평균점수',value='N/A')         
with col3:
    if sidebar_subject:
        max_score = filtered_df[sidebar_subject].max().max() # 하나만 max() 하면 과목 중 최고점이 나오고 max().nax() 과목을 합쳐서 최고점이 나온다.
        if pd.isna(max_score): # 시스템이나 데이터가 누락된 값을 탐지하여 boolean 배열 함수로 반환
            st.metric("최고점수", value =  "N/A") 
        else:     
            st.metric("최고점수", value =  f'{max_score:.1f}점')  
    else:
        st.metric('최고점수',value='N/A')   # subject이 비어있으면 N/A 출력

# 오른쪽 본문
st.divider()

st.header("2. 비율을 조정한 컬럼 레이아웃")

col_left, col_right = st.columns([2, 1])  # 2:1 비율

with col_left:
    st.subheader(" 필터링된 학생 데이터")
    if sidebar_subject:
        columns_to_show = ["이름", "나이", "학년"] + sidebar_subject # 리스트와 리스트를 합쳐서 하나의 리스트로 만듬 , 컬럼 [] 두개이상 쓰면 데이터 프레임 하나만 쓰면 시리즈가 된다.
        st.dataframe(filtered_df[columns_to_show], use_container_width=True, height=300)
    else:
        st.dataframe(filtered_df[["이름", "나이", "학년"]], use_container_width=True, height=300)

with col_right:
    st.subheader(" 요약 정보")
    if show_stats and sidebar_subject: # 사이드에 선택된 과목들의 평균 출력
        st.write("**과목별 평균**")
        for subject in sidebar_subject: 
            avg = filtered_df[subject].mean() #과목마다 평균을 avg변수안에 넣어준다.
            st.write(f"• {subject}: {avg:.1f}점")
    else:
        st.info("사이드바에서 '통계 표시'를 선택하세요.")

st.divider()

# ============================================
# 3. 탭(Tabs)으로 콘텐츠 구분하기
# ============================================
st.header("3. 탭으로 콘텐츠 구분하기")
st.write("탭을 사용하면 많은 정보를 깔끔하게 정리할 수 있습니다.")

# 탭 생성
tab1, tab2, tab3, tab4 = st.tabs([" 데이터", " 차트", " 랭킹", " 정보"])  

# 탭 1: 데이터 테이블
with tab1:
    st.subheader("전체 데이터 테이블")
    st.dataframe(filtered_df, use_container_width=True)
    
    # 탭 안에서도 컬럼 사용 가능
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("데이터 요약")
        st.write(f" 학생 수: {len(filtered_df)}명")
        st.write(f" 평균 나이: {filtered_df['나이'].mean():.1f}세")
    with col_b:
        st.write("학년 분포")
        grade_counts = filtered_df['학년'].value_counts()
        st.dataframe(grade_counts.to_frame(name="인원"), use_container_width=True)

# 탭 2: 차트
with tab2:
    st.subheader("성적 시각화")
    
    if show_chart and sidebar_subject:
        # 과목별 평균 점수 차트
        st.write("과목별 평균 점수")
        avg_by_subject = filtered_df[sidebar_subject].mean()
        st.bar_chart(avg_by_subject)
        
        # 학생별 점수 추이 (첫 5명만)
        st.write("학생별 성적 비교 (상위 5명)")
        chart_df = filtered_df[["이름"] + sidebar_subject].head(5).set_index("이름")
        st.line_chart(chart_df)
    else:
        st.info("사이드바에서 '차트 표시'를 선택하고 과목을 선택하세요.")

# 탭 3: 랭킹
with tab3:
    st.subheader("성적 순위")
    
    if sidebar_subject:
        rank_df = filtered_df.copy()
        rank_df['평균'] = rank_df[sidebar_subject].mean(axis=1)
        rank_df['총점'] = rank_df[sidebar_subject].sum(axis=1)
        rank_df = rank_df.sort_values('평균', ascending=False)
        
        # 순위 추가
        rank_df['순위'] = range(1, len(rank_df) + 1)
        
        st.dataframe(
            rank_df[['순위', '이름', '학년'] + sidebar_subject + ['평균', '총점']],
            use_container_width=True
        )
        
        # 1등 학생 하이라이트
        if len(rank_df) > 0:
            top_student = rank_df.iloc[0]
            st.success(f" 1등: {top_student['이름']} ({top_student['학년']}) - 평균 {top_student['평균']:.1f}점")
    else:
        st.warning("사이드바에서 최소 하나의 과목을 선택하세요.")

# 탭 4: 정보
with tab4:
    st.subheader(" 레이아웃 가이드")
    
    st.markdown("""
    ### 배운 레이아웃 기능들:
    
    1. 사이드바 (Sidebar)
       - `st.sidebar.title()`, `st.sidebar.selectbox()` 등
       - 필터나 설정을 별도 공간에 배치
    
    2. 컬럼 (Columns)
       - `st.columns(3)` - 동일한 너비로 3개 분할
       - `st.columns([2, 1])` - 2:1 비율로 분할
       - `with col1:` 구문으로 각 컬럼에 콘텐츠 추가
    
    3. 탭 (Tabs)
       - `st.tabs(["탭1", "탭2"])` - 여러 탭 생성
       - `with tab1:` 구문으로 각 탭에 콘텐츠 추가
    
    4. 페이지 설정
       - `layout="wide"` - 화면을 넓게 사용
       - `layout="centered"` - 중앙 정렬 (기본값)
    """)


st.info("Tip: 실제 대시보드를 만들 때는 사이드바에 필터를, 메인 영역에는 탭으로 구분된 콘텐츠를 배치하는 것이 일반적입니다!")
st.divider()


