import streamlit as st
import pandas as pd

st.set_page_config(page_title="자동차 보험 추천 시스템", layout="wide")

if "data" not in st.session_state: # 세션에 data가 없으면
    st.session_state.data = pd.DataFrame(columns=["나이","경력","사고","차종","주행거리","보험료","위험점수"]) # 빈 데이터 프레임 생성


st.title("자동차 보험료 분석 시스템")
st.write("보험료 계산 + 데이터 분석 + 추천 기능")

col1, col2 = st.columns(2)

with col1:
    st.subheader("사용자 입력")
    age = st.slider("나이", 18, 80, 30)
    exp = st.slider("운전 경력", 0 , 40, 5)
    accident = st.selectbox("사고 이력", ['없음',"1회","2회 이상"])
    car = st.selectbox("차종", ["경차", "세단", "SUV", "수입차"])
    mileage = st.selectbox("주행거리" , ["적음","보통","많음"])


def calc():
    price = 500000
    risk = 0

    if age < 26:
        price *= 1.3; risk += 2
    if exp < 2:
        price *= 1.2; risk += 2
    
    if accident == "1회":
        price *= 1.2; risk += 2
    elif accident == "2회 이상":
        price *= 1.5; risk += 4
    
    if car == "SUV":
        price *= 1.1; risk += 1
    elif car == "수입차":
        price *= 1.4; risk += 3

    if mileage == "많음":
        price *= 1.1; risk += 1
    elif mileage == "적음":
        price *= 0.9
    
    return int(price), risk

with col2:
    st.subheader("결과")

    if st.button("계산 저장"):
        price, risk = calc()

        st.success(f"보험료 : {price: ,}원")
        st.write(f'위험 점수 : {risk}')

        new_data = pd.DataFrame([{
            "나이" : age,
            "경력" : exp,
            "사고" : accident,
            "차종" : car,
            "주행 거리" : mileage,
            "보험료" : price,
            "위험점수" : risk
        }])

        st.session_state.data = pd.concat([st.session_state.data, new_data], ignore_index=True) # 기존 데이터프레임에 새로운 데이터를 아래로 추가(행 추가) # 0 부터 다시 번호 매기

st.markdown("---")
st.subheader("보험 데이터 분석")

df = st.session_state.data

if not df.empty:
    st.dataframe(df)

    col3, col4, col5 = st.columns(3)

    with col3:
        st.metric("평균 보험료", f"{int(df['보험료'].mean())}")
    with col4:
        st.metric("최고 보험료", f"{int(df['보험료'].max())}")
    with col5:
        st.metric("평균 위험 점수", round(df['위험점수'].mean(),1))
else:
    print("데이터 없음")
