
import streamlit as st
import pandas as pd
import json #json 사용
import os

st.set_page_config( #페이지 설정
    page_title="레이아웃 디자인", # 웹 페이지 위에 title 설정
    layout="wide"  # 화면을 넓게 사용 (기본값은 "centered")
)

st.title("레이아웃 디자인 (JSON 연동)") # 처음 제목 

# ============================================
# JSON 파일에서 데이터 로드하는 함수
# ============================================
def load_students_from_json(file_path="students_data.json"): #students_data.json 파일 불러오기 
    """
    JSON 파일에서 학생 데이터를 읽어옵니다.
    파일이 없으면 기본 데이터를 생성합니다.
    """
    try:
        # JSON 파일이 존재하는지 확인
        if os.path.exists(file_path): # 파이썬에서 지정된 경로를 확인하는 함수
            with open(file_path, 'r', encoding='utf-8') as f: # 파일을 읽기 모드로 가져온다.
                data = json.load(f) # data 변수 안에 로드된 파일을 저장
                st.sidebar.success(f" JSON 파일 로드 완료: {file_path}") # 완료되면 sideber에 완료 메시지 
                # JSON의 'students' 키에서 데이터 추출
                return pd.DataFrame(data['students']) #json 안에 있는 data['students']를 보내준다.
        else:
            # 파일이 없으면 기본 데이터 생성 후 저장
            st.sidebar.warning(" JSON 파일이 없어서 기본 데이터를 생성합니다.") #파일이 없으면 경고 메시지
            default_data = {
                "students": [
                    {"이름": "김철수", "나이": 25, "학년": "3학년", "수학": 85, "영어": 90, "과학": 88},
                    {"이름": "이영희", "나이": 23, "학년": "2학년", "수학": 92, "영어": 88, "과학": 90},
                    {"이름": "박민수", "나이": 26, "학년": "4학년", "수학": 78, "영어": 85, "과학": 92},
                    {"이름": "정지은", "나이": 24, "학년": "3학년", "수학": 95, "영어": 92, "과학": 89},
                    {"이름": "최동욱", "나이": 27, "학년": "4학년", "수학": 88, "영어": 86, "과학": 91},
                    {"이름": "강서연", "나이": 22, "학년": "1학년", "수학": 70, "영어": 75, "과학": 80},
                    {"이름": "윤태희", "나이": 25, "학년": "3학년", "수학": 91, "영어": 89, "과학": 85},
                    {"이름": "장민지", "나이": 23, "학년": "2학년", "수학": 87, "영어": 90, "과학": 88}
                ]
            } # 데이터 직접 입력
            save_students_to_json(default_data, file_path) #json 파일에 데이터를 저장하는 함수
            return pd.DataFrame(default_data['students']) # json 안에 있는 dafault_data['students']를 보내준다.
    except Exception as e: # 이외의 오류 발생 시
        st.sidebar.error(f" 오류 발생: {str(e)}") # sidebar 에 에러 메시지 
        # 오류 발생 시 빈 데이터프레임 반환
        return pd.DataFrame()

# ============================================
# JSON 파일에 데이터 저장하는 함수
# ============================================
def save_students_to_json(data, file_path="students_data.json"): # json 파일에 데이터를 저장하는 함수를 만든다.
    """
    데이터를 JSON 파일로 저장합니다.
    data는 딕셔너리 또는 DataFrame 형태
    """
    try:
        # DataFrame인 경우 딕셔너리로 변환
        if isinstance(data, pd.DataFrame): # 클래스인지 인스턴스인지 확인 
            data_dict = {"students": data.to_dict('records')} # 맞으면 데이터프레임 각 행을 딕셔너리로 만들고, 이를 리스트로 묶는다.
        else:
            data_dict = data # 만약 데이터프레임이 아니면 data_dict에 할당됨
        
        # JSON 파일로 저장 (한글이 깨지지 않도록 ensure_ascii=False)
        with open(file_path, 'w', encoding='utf-8') as f: # students_data.json 파일을 write 형태로 불러온다.
            json.dump(data_dict, f, ensure_ascii=False, indent=2) # 딕셔너리 형태로 저장 한다.
        
        return True  # 참을 보냄
    except Exception as e: # 이외의 오류가 있으면
        st.error(f" 저장 오류: {str(e)}") # 오류 메시지
        return False # 거짓을 보냄

# ============================================
# 데이터 로드
# ============================================
df = load_students_from_json() #위에 json 파일을 불러온 함수를 사용한다.

# 데이터가 비어있으면 에러 메시지 표시
if df.empty: 
    st.error(" 데이터를 불러올 수 없습니다. students_data.json 파일을 확인하세요.")
    st.stop()  # 여기서 앱 실행 중단

# ============================================
# 1. 사이드바 (Sidebar) 사용하기
# ============================================
st.sidebar.title(" 설정 메뉴") # 사이드 바에 제목 
st.sidebar.write("사이드바에 필터링 옵션을 모아둘 수 있습니다.") # 사이드 바에 글을 적는다.

# 사이드바에 필터 옵션 배치
st.sidebar.header(" 데이터 필터")

# 사이드바 - 학년 선택
sidebar_grade = st.sidebar.selectbox(
    "학년 선택",
    options=["전체"] + sorted(df['학년'].unique().tolist()) #리스트로 반환하는 내장 함수이다. 중복안되고 리스트로 변환해서 반환한다.
)

# 사이드바 - 최소 나이 설정하는 것이다.
sidebar_min_age = st.sidebar.slider(
    "최소 나이",
    min_value=int(df['나이'].min()), # int 형태로 df['나이']의 최소나이를 min_value에 저장한다.
    max_value=int(df['나이'].max()), # int 형태로 df['나이']의 최소나이를 max_value에 저장한다.
    value=int(df['나이'].min()) # 처음 설정을 최소나이로 설정한다.
)

# 사이드바 - 과목 선택 
sidebar_subjects = st.sidebar.multiselect( 
    "표시할 과목",
    options=["수학", "영어", "과학"], # 과목을 수학 영어 과학으로 설정한다.
    default=["수학", "영어", "과학"] # 기본 값을 수학 영어 과학으로 설정한다.
)

# 사이드바 구분선
st.sidebar.divider()

# 사이드바 - 추가 옵션
st.sidebar.header(" 추가 옵션")
show_stats = st.sidebar.checkbox("통계 표시", value=True) # value = True는 체크박스 체크 유무를 확인한다. True면 체크 False 면 체크 안됨
show_chart = st.sidebar.checkbox("차트 표시", value=True) # value = True는 체크박스 체크 유무를 확인한다. True면 체크 False 면 체크 안됨

# 필터링 적용
filtered_df = df.copy() #필터링 적용하기 위해 df에 있는 데이터를 filltered_df에 할당한다.

if sidebar_grade != "전체": # siderbar_grade 값이 '전체'가 아닐때 실행 된다.
    filtered_df = filtered_df[filtered_df['학년'] == sidebar_grade] # filltered_df에서 '학년' 컬럼 값이 sider_grade와 같은 행들만 남기고 다시 filtered_df에 저장됨
    # 해당 학년만 남기고 저장한다.

filtered_df = filtered_df[filtered_df['나이'] >= sidebar_min_age] # filltered_df에서 '나이' 칼럼 값이 sider_min_age 이상인 행들만 filltered_df에 저장됨

st.sidebar.success(f" {len(filtered_df)}명의 학생이 검색되었습니다.") # 완료되면 확인메시지

# ============================================
# 2. 컬럼(Columns)으로 화면 나누기
# ============================================
st.header("1. 컬럼으로 화면 나누기") # 메인화면 헤더에 글
st.write("화면을 여러 개의 열로 나눠서 정보를 정리할 수 있습니다.") # 헤더 아랫글

# 3개의 컬럼 생성 (동일한 너비)
col1, col2, col3 = st.columns(3) # 칼럼을 비슷하게 3등분으로 나누어서 화면 배치한다.

# 각 컬럼에 메트릭 카드 배치
with col1: # 첫번째 화면 배치
    st.metric(
        label=" 총 학생 수", # 화면에 보이는 총 학생 수 표시
        value=len(filtered_df), # 화면마다 클릭했을 때 달라지는 학생수 표시
        delta=f"{len(filtered_df) - len(df)} (필터 적용)" # 총 학생 수 아래 몇명 줄었는지 늘었는지 보여주는 메시지
    )

with col2: # 두 번째에 화면 배치
    if sidebar_subjects: # sidebar_subjects 값이 True이면 
        avg_score = filtered_df[sidebar_subjects].mean().mean() # filtered_df[siderbar_subjects] 선택된 과목에 평균을 내고 그 평균을 낸 값을 다시 평균을 내서 avg_score 할당
        st.metric(
            label=" 평균 점수", # 평균점수를 표시한다.
            value=f"{avg_score:.1f}점", # 위에 할당된 avg_score를 한 자리수 점수로 표시한다.
            delta="2.3점" if avg_score > 85 else "-1.2점" # 만약 avg_score가 85 보다 크면 2.3점을 표시하고 아니면 -1.2점을 표시한다.
        )
    else: # sidebar_subjects 값이 False 이면 (과목이 선택되지 않으면)
        st.metric(label=" 평균 점수", value="N/A") # 평균 점수칸에 N/A를 표시한다.

with col3: # 세 번째 화면 배치
    if sidebar_subjects: # siderbar_subjects 값이 True 이면
        max_score = filtered_df[sidebar_subjects].max().max() # 선택된 과목의 가장 큰 값을 내고 다른 과목 점수와 비교하면 가장 큰 값을 max_score에 저장한다.
        st.metric( 
            label=" 최고 점수", # 최고 점수를 나타내는 칸
            value=f"{max_score}점" # max_score를 표시한다.
        )
    else: # siderbar_subjects 값이 False 이면 (과목이 선택되지 않으면)
        st.metric(label=" 최고 점수", value="N/A") # 최고점수 칸에 N/A를 표시한다

st.divider() # 선

# 2:1 비율로 컬럼 나누기
st.header("2. 비율을 조정한 컬럼 레이아웃")

col_left, col_right = st.columns([2, 1])  # 2:1 비율로 칸을 나눈다.

with col_left: # 첫번째 비율의 칸
    st.subheader("📋 필터링된 학생 데이터") # subheader에 부제목을 표시한다.
    if sidebar_subjects: #siderbar_subjects가 True 이면 (과목 선택이 되면)
        columns_to_show = ["이름", "나이", "학년"] + sidebar_subjects # 각 학생들 이름 나이 학년 과 선택 된 과목 성적을 columns_to_show에 할당한다.
        st.dataframe(filtered_df[columns_to_show], use_container_width=True, height=300) # 데이터 프레임으로 표처럼 columns_to_show를 나타낸다. 
    else: # 만약 선택된 과목이 없으면
        st.dataframe(filtered_df[["이름", "나이", "학년"]], use_container_width=True, height=300) # 이름 나이 학년만 표에 나타낸다.

with col_right: # 두 번째 비율의 칸
    st.subheader(" 요약 정보") # 부제목을 표시한다.
    if show_stats and sidebar_subjects: # 통계가 켜져있고 과목이 선택되어 있을 때 둘다 참일때 실행된다.
        st.write("과목별 평균")  # 제목을 출력
        for subject in sidebar_subjects: # 선택된 과목들을 하나씩 반복한다.
            avg = filtered_df[subject].mean() #해당 과목의 평균값을 계산한다.
            st.write(f" {subject}: {avg:.1f}점") # 결과 출력 소수점 한자리 수까지 출력한다.
    else: # 조건이 안맞을 때 둘다 참이 아닐때
        st.info("사이드바에서 '통계 표시'를 선택하세요.") # 안내 메시지 출력

st.divider()

# ============================================
# 3. 탭(Tabs)으로 콘텐츠 구분하기
# ============================================
st.header("3. 탭으로 콘텐츠 구분하기") # 제목 표시
st.write("탭을 사용하면 많은 정보를 깔끔하게 정리할 수 있습니다.") # 밑에 설명 표시

# 탭 생성
tab1, tab2, tab3, tab4 = st.tabs([" 데이터", " 차트", " 랭킹", " 정보"]) # 탭을 생성한다 탭은 선택했을때 화면이 바뀌는 것이다.

# 탭 1: 데이터 테이블
with tab1:
    st.subheader("전체 데이터 테이블") # 부제목을 설정
    st.dataframe(filtered_df, use_container_width=True) # filtered_df안에 데이터를 프레임으로 가져온다.
    
    # 탭 안에서도 컬럼 사용 가능
    col_a, col_b = st.columns(2) # 탭 안에서 또 다른 탭 설정
    with col_a:
        st.write("데이터 요약") # 첫번째 탭 데이터 요약
        st.write(f" 학생 수: {len(filtered_df)}명") # 총학생 수가 몇명인지 구한다.
        st.write(f" 평균 나이: {filtered_df['나이'].mean():.1f}세") # mean을 이용하여 filtered_df['나이'] 안에 저장되어있는 평균 나이를 구한다.
    with col_b: 
        st.write("학년 분포") # 두 번째 탭 학년 분포
        grade_counts = filtered_df['학년'].value_counts() # 학년 칼럼 선택해서 각 값이 몇 번 나왔는지 계산한다.
        st.dataframe(grade_counts.to_frame(name="인원"), use_container_width=True) # 칼럼의 이름을 인원으로 설정해서 화면 너비에 맞게 출력한다.

# 탭 2: 차트
with tab2:
    st.subheader("성적 시각화")
    
    if show_chart and sidebar_subjects:
        # 과목별 평균 점수 차트
        st.write("과목별 평균 점수")
        avg_by_subject = filtered_df[sidebar_subjects].mean()
        st.bar_chart(avg_by_subject)
        
        # 학생별 점수 추이 (첫 5명만)
        st.write("학생별 성적 비교 (상위 5명)")
        chart_df = filtered_df[["이름"] + sidebar_subjects].head(5).set_index("이름")
        st.line_chart(chart_df)
    else:
        st.info("사이드바에서 '차트 표시'를 선택하고 과목을 선택하세요.")

# 탭 3: 랭킹
with tab3:
    st.subheader("성적 순위")
    
    if sidebar_subjects:
        rank_df = filtered_df.copy()
        rank_df['평균'] = rank_df[sidebar_subjects].mean(axis=1)
        rank_df['총점'] = rank_df[sidebar_subjects].sum(axis=1)
        rank_df = rank_df.sort_values('평균', ascending=False)
        
        # 순위 추가
        rank_df['순위'] = range(1, len(rank_df) + 1)
        
        st.dataframe(
            rank_df[['순위', '이름', '학년'] + sidebar_subjects + ['평균', '총점']],
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
    
    1. **사이드바 (Sidebar)**
       - `st.sidebar.title()`, `st.sidebar.selectbox()` 등
       - 필터나 설정을 별도 공간에 배치
    
    2. **컬럼 (Columns)**
       - `st.columns(3)` - 동일한 너비로 3개 분할
       - `st.columns([2, 1])` - 2:1 비율로 분할
       - `with col1:` 구문으로 각 컬럼에 콘텐츠 추가
    
    3. **탭 (Tabs)**
       - `st.tabs(["탭1", "탭2"])` - 여러 탭 생성
       - `with tab1:` 구문으로 각 탭에 콘텐츠 추가
    
    4. **페이지 설정**
       - `layout="wide"` - 화면을 넓게 사용
       - `layout="centered"` - 중앙 정렬 (기본값)
    """)

st.divider()

# ============================================
# 4. JSON 데이터 관리 기능
# ============================================
st.header("4. JSON 파일 데이터 관리")

col1, col2 = st.columns(2)

with col1:
    st.subheader(" 새 학생 추가하기")
    
    with st.form("add_student_form"):
        new_name = st.text_input("이름", placeholder="예: 홍길동")
        new_age = st.number_input("나이", min_value=18, max_value=40, value=22)
        new_grade = st.selectbox("학년", ["1학년", "2학년", "3학년", "4학년"])
        
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            new_math = st.number_input("수학", min_value=0, max_value=100, value=80)
        with col_b:
            new_english = st.number_input("영어", min_value=0, max_value=100, value=80)
        with col_c:
            new_science = st.number_input("과학", min_value=0, max_value=100, value=80)
        
        submitted = st.form_submit_button(" 학생 추가", use_container_width=True)
        
        if submitted:
            if new_name.strip():
                # 새 학생 데이터 추가
                new_student = {
                    "이름": new_name,
                    "나이": new_age,
                    "학년": new_grade,
                    "수학": new_math,
                    "영어": new_english,
                    "과학": new_science
                }
                
                # 기존 데이터에 추가
                df_updated = pd.concat([df, pd.DataFrame([new_student])], ignore_index=True)
                
                # JSON 파일에 저장
                if save_students_to_json(df_updated):
                    st.success(f" '{new_name}' 학생이 추가되었습니다!")
                    st.balloons()
                    # 페이지 새로고침하여 데이터 반영
                    st.rerun() #새로고침
                else:
                    st.error(" 저장에 실패했습니다.")
            else:
                st.warning(" 이름을 입력해주세요.")

with col2:
    st.subheader(" 데이터 관리")
    
    st.write(f"현재 총 학생 수: {len(df)}명")
    
    # 학생 삭제 기능
    if len(df) > 0:
        delete_name = st.selectbox(
            "삭제할 학생 선택",
            df['이름'].tolist(),
            key="delete_student"
        )
        
        if st.button(" 선택한 학생 삭제", use_container_width=True):
            # 선택한 학생 제외하고 저장
            df_updated = df[df['이름'] != delete_name]
            
            if save_students_to_json(df_updated):
                st.success(f" '{delete_name}' 학생이 삭제되었습니다.")
                st.rerun()
            else:
                st.error(" 삭제에 실패했습니다.")
    
    st.divider()
    # 학생 수정 기능
    if len(df) > 0:
        update_name = st.selectbox(
        "수정할 학생 선택",
        df['이름'].tolist(),
        key="update_student"
    )

    update_student = df[df['이름'] == update_name].iloc[0] # 행이나 칼럼의 순서를 나타내는 정수
    
    with st.form("update_student_form"):
        update_new_name = st.text_input('이름', value=update_student['이름'])
        update_new_age = st.number_input('나이', value=update_student['나이'])
        update_new_grade = st.selectbox(
            "학년",
            ["1학년","2학년","3학년","4학년"],
            index=["1학년","2학년","3학년","4학년"].index(update_student['학년'])
        )
        
        col_a , col_b, col_c = st.columns(3)
        with col_a:
            update_math = st.number_input("수학",min_value=0, max_value=100, value=update_student['수학'])
        with col_b:
            update_eng = st.number_input("영어",min_value=0, max_value=100, value=update_student['영어'])
        with col_c:
            update_sc = st.number_input("과학",min_value=0, max_value= 100, value=update_student['과학'])
        
        submit_update = st.form_submit_button("수정 완료",use_container_width=True)

        if submit_update:
            df_updated = df.copy()

            df_updated.loc[df_updated['이름'] == update_new_name, ['이름','나이','학년','수학','영어','과학']] = [
                update_new_name,update_new_age,update_new_grade,
                update_math, update_eng, update_sc
            ]
            if save_students_to_json(df_updated):
                st.success(f"'{update_name}'학생 정보가 수정 완료")
                st.rerun()
            else:
                st.error("수정실패")

    st.divider()
    # JSON 파일 다시 로드
    if st.button(" 데이터 새로고침", use_container_width=True):
        st.rerun()
    
    # 원본 JSON 파일 보기
    with st.expander(" JSON 파일 내용 보기"):
        try:
            with open("students_data.json", 'r', encoding='utf-8') as f:
                json_content = f.read()
                st.code(json_content, language="json")
        except FileNotFoundError:
            st.warning("students_data.json 파일이 없습니다.")

st.divider()

st.info(" Tip: JSON 파일을 사용하면 데이터를 영구적으로 저장하고 외부 프로그램과 쉽게 데이터를 주고받을 수 있습니다!")
