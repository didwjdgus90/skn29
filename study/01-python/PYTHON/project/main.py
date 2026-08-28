import streamlit as st
import pandas as pd
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os
import matplotlib.pyplot as plt
import folium
from streamlit_folium import st_folium
import html
import re
from pathlib import Path
from faq import load_samsung, load_hyundai, load_db, render_company_faq
import altair as alt

load_dotenv()

# ----------------------------
# DB 연결 설정
# ----------------------------
CAR_DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', ''),
    'database': os.getenv('DB_NAME', 'car_db'),
    'port': int(os.getenv('DB_PORT', 3306))
}

INSURANCE_DB_CONFIG = {
    'host': os.getenv('INS_DB_HOST', os.getenv('DB_HOST', 'localhost')),
    'user': os.getenv('INS_DB_USER', os.getenv('DB_USER', 'root')),
    'password': os.getenv('INS_DB_PASSWORD', os.getenv('DB_PASSWORD', '')),
    'database': os.getenv('INS_DB_NAME', 'car_insurance_final'),
    'port': int(os.getenv('INS_DB_PORT', os.getenv('DB_PORT', 3306)))
}

# ----------------------------
# DB 조회 함수
# ----------------------------
def get_vehicle_data():
    try:
        conn = mysql.connector.connect(**CAR_DB_CONFIG)
        cursor = conn.cursor(dictionary=True)

        query = """
        SELECT 
            r.region_name AS 지역,
            t.type_name AS 차종,
            u.usage_name AS 용도,
            v.vehicle_count AS 등록대수
        FROM vehicle_stat v
        JOIN region r ON v.region_id = r.region_id
        JOIN vehicle_type t ON v.type_id = t.type_id
        JOIN usage_type u ON v.usage_id = u.usage_id
        WHERE v.stat_year_month = '202602'
        """

        cursor.execute(query)
        data = cursor.fetchall()
        df = pd.DataFrame(data)

        cursor.close()
        conn.close()

        return df

    except Error as e:
        st.error(f"DB 오류: {e}")
        return pd.DataFrame()


# ----------------------------
# 성/연령/지역별 DB 조회
# ----------------------------
def get_insurance_gender_age_data():
    try:
        conn = mysql.connector.connect(**CAR_DB_CONFIG)
        cursor = conn.cursor(dictionary=True)

        query = """
        SELECT 
            gender AS 성별,
            age_group AS 연령대,
            region AS 지역,
            SUM(vehicle_count) AS 등록대수
        FROM vehicle_insurance_stat
        WHERE stat_year_month = '202602'
        GROUP BY gender, age_group, region
        ORDER BY age_group, gender, region
        """

        cursor.execute(query)
        data = cursor.fetchall()
        df = pd.DataFrame(data)

        cursor.close()
        conn.close()

        return df

    except Error as e:
        st.error(f"DB 오류: {e}")
        return pd.DataFrame()


# ----------------------------
# 보험 통계 더미 데이터 보완
# ----------------------------
def get_insurance_type_data():
    try:
        conn = mysql.connector.connect(**CAR_DB_CONFIG)
        cursor = conn.cursor(dictionary=True)

        query = """
        SELECT 
            car_type AS 차종,
            가입건수,
            평균보험료
        FROM insurance_type_stat
        ORDER BY 가입건수 DESC
        """
        cursor.execute(query)
        data = cursor.fetchall()
        df = pd.DataFrame(data)

        cursor.close()
        conn.close()
        return df

    except:
        return pd.DataFrame({
            "차종": ["소형", "중형", "대형", "다인승"],
            "평균보험료": [780000, 920000, 1150000, 1300000]
        })


def get_insurance_age_data():
    try:
        conn = mysql.connector.connect(**CAR_DB_CONFIG)
        cursor = conn.cursor(dictionary=True)

        query = """
        SELECT 
            age_group AS 구분,
            가입건수,
            평균보험료
        FROM insurance_age_stat
        ORDER BY 가입건수 DESC
        """
        cursor.execute(query)
        data = cursor.fetchall()
        df = pd.DataFrame(data)

        cursor.close()
        conn.close()
        return df

    except:
        return pd.DataFrame({
            "구분": ["20대", "30대", "40대", "50대 이상"],
            "평균보험료": [1100000, 850000, 780000, 720000]
        })




# ----------------------------
# 보험료 조회용 보조 함수
# ----------------------------
def map_age_to_age_group(age: int) -> str:
    if age <= 29:
        return "20대 이하"
    elif age <= 39:
        return "30대"
    elif age <= 49:
        return "40대"
    elif age <= 59:
        return "50대"
    elif age <= 69:
        return "60대"
    return "70대 이상"


def get_origin_options():
    try:
        conn = mysql.connector.connect(**INSURANCE_DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT origin_type FROM car_master ORDER BY FIELD(origin_type, '국산', '외산')")
        rows = [r[0] for r in cursor.fetchall()]
        cursor.close()
        conn.close()
        return rows or ["국산", "외산"]
    except Error:
        return ["국산", "외산"]


def get_maker_options(origin_type: str):
    try:
        conn = mysql.connector.connect(**INSURANCE_DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT maker_name
            FROM car_master
            WHERE origin_type = %s
            ORDER BY maker_name
        """, (origin_type,))
        rows = [r[0] for r in cursor.fetchall()]
        cursor.close()
        conn.close()
        return rows
    except Error:
        return []


def get_model_options(origin_type: str, maker_name: str):
    try:
        conn = mysql.connector.connect(**INSURANCE_DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT model_name
            FROM car_master
            WHERE origin_type = %s AND maker_name = %s
            ORDER BY model_name
        """, (origin_type, maker_name))
        rows = [r[0] for r in cursor.fetchall()]
        cursor.close()
        conn.close()
        return rows
    except Error:
        return []


def calculate_expected_premium(gender_label, age, model_year, origin_type, maker_name, model_name):
    gender_code = 'M' if gender_label == '남성' else 'F'
    age_group = map_age_to_age_group(age)

    conn = mysql.connector.connect(**INSURANCE_DB_CONFIG)
    cursor = conn.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT maker_name, model_name, origin_type, body_type, vehicle_class, base_price
            FROM car_master
            WHERE origin_type = %s AND maker_name = %s AND model_name = %s
            LIMIT 1
        """, (origin_type, maker_name, model_name))
        car = cursor.fetchone()
        if not car:
            raise ValueError("선택한 차량 정보를 car_master에서 찾을 수 없습니다.")

        body_type = car['body_type']
        vehicle_class = car['vehicle_class']
        base_price = float(car['base_price'])

        cursor.execute("""
            SELECT SUM(earned_premium_amount) / NULLIF(SUM(join_count), 0) AS overall_avg_premium
            FROM insurance_contract_stat
        """)
        overall_avg_premium = float((cursor.fetchone() or {}).get('overall_avg_premium') or 0)
        if overall_avg_premium <= 0:
            raise ValueError("insurance_contract_stat에 유효한 보험료 통계가 없습니다.")

        cursor.execute("""
            SELECT SUM(earned_premium_amount) / NULLIF(SUM(join_count), 0) AS group_avg_premium
            FROM insurance_contract_stat
            WHERE gender_code = %s
              AND age_group = %s
              AND origin_type = %s
              AND vehicle_class = %s
        """, (gender_code, age_group, origin_type, vehicle_class))
        group_avg_premium = float((cursor.fetchone() or {}).get('group_avg_premium') or overall_avg_premium)
        enrollment_risk_factor = group_avg_premium / overall_avg_premium

        cursor.execute("""
            SELECT SUM(l.loss_amount) / NULLIF(SUM(c.earned_premium_amount), 0) AS overall_loss_ratio
            FROM insurance_loss_stat l
            JOIN insurance_contract_stat c
              ON l.stat_year_month = c.stat_year_month
             AND l.insurance_product_id = c.insurance_product_id
             AND l.coverage_id = c.coverage_id
             AND l.vehicle_class = c.vehicle_class
        """)
        overall_loss_ratio = float((cursor.fetchone() or {}).get('overall_loss_ratio') or 1)

        cursor.execute("""
            SELECT SUM(l.loss_amount) / NULLIF(SUM(c.earned_premium_amount), 0) AS class_loss_ratio
            FROM insurance_loss_stat l
            JOIN insurance_contract_stat c
              ON l.stat_year_month = c.stat_year_month
             AND l.insurance_product_id = c.insurance_product_id
             AND l.coverage_id = c.coverage_id
             AND l.vehicle_class = c.vehicle_class
            WHERE c.vehicle_class = %s
        """, (vehicle_class,))
        class_loss_ratio = float((cursor.fetchone() or {}).get('class_loss_ratio') or overall_loss_ratio)
        loss_risk_factor = class_loss_ratio / overall_loss_ratio if overall_loss_ratio else 1.0

        cursor.execute("""
            SELECT residual_value_rate
            FROM car_value_factor
            WHERE origin_type = %s
              AND body_type = %s
              AND model_year = %s
        """, (origin_type, body_type, model_year))
        row = cursor.fetchone()
        residual_value_rate = float(row['residual_value_rate']) if row and row.get('residual_value_rate') is not None else 0.70
        vehicle_value_factor = 0.8 + 0.4 * residual_value_rate

        cursor.execute("""
            SELECT AVG(base_price) AS avg_base_price
            FROM car_master
            WHERE origin_type = %s
              AND vehicle_class = %s
        """, (origin_type, vehicle_class))
        comparable_avg_base_price = float((cursor.fetchone() or {}).get('avg_base_price') or base_price)
        model_price_factor = base_price / comparable_avg_base_price if comparable_avg_base_price else 1.0
        model_price_factor = max(0.85, min(model_price_factor, 1.15))

        expected_premium = (
            overall_avg_premium
            * enrollment_risk_factor
            * loss_risk_factor
            * vehicle_value_factor
            * model_price_factor
        )

        return {
            'premium': round(expected_premium)*10,
            'age_group': age_group,
            'vehicle_class': vehicle_class,
            'body_type': body_type,
            'overall_avg_premium': round(overall_avg_premium),
            'group_avg_premium': round(group_avg_premium),
            'residual_value_rate': residual_value_rate,
            'enrollment_risk_factor': enrollment_risk_factor,
            'loss_risk_factor': loss_risk_factor,
            'vehicle_value_factor': vehicle_value_factor,
            'model_price_factor': model_price_factor,
        }
    finally:
        cursor.close()
        conn.close()

# ----------------------------
# 페이지 설정
# ----------------------------
st.set_page_config(
    page_title="Drive Insight",
    page_icon="🚘",
    layout="wide"
)

# ----------------------------
# 지역 좌표 데이터
# ----------------------------
region_coords = {
    "서울": [37.5665, 126.9780],
    "경기": [37.4138, 127.5183],
    "부산": [35.1796, 129.0756],
    "인천": [37.4563, 126.7052],
    "경남": [35.227, 128.681]
}


# ----------------------------
# 상위 5개 지역만 지도 표시
# ----------------------------
def build_top5_map(region_summary):
    top5 = region_summary.nlargest(5, "등록대수")

    m = folium.Map(
        location=[36.35, 127.8],
        zoom_start=7,
        tiles="CartoDB positron"
    )

    max_value = top5["등록대수"].max()

    for _, row in top5.iterrows():
        region = row["지역"]
        value = row["등록대수"]

        if region in region_coords:
            lat, lon = region_coords[region]
            ratio = value / max_value if max_value else 0

            if ratio >= 0.8:
                color = "#1d4ed8"
            elif ratio >= 0.55:
                color = "#3b82f6"
            elif ratio >= 0.3:
                color = "#60a5fa"
            else:
                color = "#93c5fd"

            radius = 12 + (value / max_value) * 18

            folium.CircleMarker(
                location=[lat, lon],
                radius=radius,
                popup=folium.Popup(
                    f"<b>{region}</b><br>등록대수: {int(value):,}대",
                    max_width=220
                ),
                tooltip=f"{region}: {int(value):,}대",
                color=color,
                fill=True,
                fill_color=color,
                fill_opacity=0.78,
                weight=2
            ).add_to(m)

    return m


# ----------------------------
# CSS 적용
# ----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

#MainMenu {visibility: hidden;} 
footer {visibility: hidden; }
header {visibility: hidden;}
            
/* 전체 */
html, body, [class*="css"], .stApp {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at top right, rgba(37, 99, 235, 0.08), transparent 24%),
        linear-gradient(180deg, #eef4fb 0%, #e9f0f8 100%);
    color: #16202a;
}

.block-container {
    padding-top: 1.7rem;
    padding-left: 2.2rem;
    padding-right: 2.2rem;
    padding-bottom: 2.2rem;
    max-width: 1500px;
}

/* 사이드바 */
section[data-testid="stSidebar"] {
    background:
        radial-gradient(circle at top, rgba(59,130,246,0.16), transparent 22%),
        linear-gradient(180deg, #091327 0%, #0f1c34 45%, #14223b 100%);
    border-right: 1px solid rgba(255,255,255,0.05);
    width: 320px !important;
}

section[data-testid="stSidebar"] .block-container {
    padding-top: 1.25rem;
    padding-left: 1rem;
    padding-right: 1rem;
    padding-bottom: 1rem;
}

/* 사이드바 상단 브랜드 박스 */
.sidebar-brand-box {
    background: linear-gradient(135deg, rgba(255,255,255,0.07) 0%, rgba(59,130,246,0.10) 100%);
    border: 1px solid rgba(148, 163, 184, 0.18);
    border-radius: 24px;
    padding: 18px 16px 16px 16px;
    margin-bottom: 16px;
    box-shadow: 0 18px 30px rgba(0,0,0,0.18);
}

.sidebar-badge {
    display: inline-block;
    padding: 6px 10px;
    border-radius: 999px;
    background: rgba(59,130,246,0.18);
    color: #93c5fd;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 0.12em;
    margin-bottom: 12px;
}

.sidebar-main-title {
    font-size: 31px;
    font-weight: 900;
    color: #f8fafc;
    letter-spacing: -0.03em;
    margin-bottom: 0.35rem;
}

.sidebar-subtitle {
    font-size: 13px;
    color: #aab9d2;
    line-height: 1.55;
    margin-bottom: 0.2rem;
}

.sidebar-menu-title {
    font-size: 12px;
    font-weight: 900;
    letter-spacing: 0.18em;
    color: #60a5fa;
    margin-top: 16px;
    margin-bottom: 12px;
}

/* 사이드바 공통 버튼 */
section[data-testid="stSidebar"] div.stButton > button {
    width: 100%;
    min-height: 56px;
    border-radius: 16px;
    border: 1px solid rgba(148, 163, 184, 0.18);
    background: linear-gradient(135deg, rgba(255,255,255,0.05) 0%, rgba(255,255,255,0.03) 100%);
    color: #edf4ff;
    font-size: 15px;
    font-weight: 800;
    text-align: left;
    padding: 0 16px;
    box-shadow: 0 10px 18px rgba(0,0,0,0.12);
    transition: all 0.2s ease;
}

section[data-testid="stSidebar"] div.stButton > button:hover {
    background: linear-gradient(135deg, rgba(59,130,246,0.18) 0%, rgba(37,99,235,0.14) 100%);
    border: 1px solid rgba(96, 165, 250, 0.48);
    color: #ffffff;
    transform: translateY(-1px);
}

/* 보험/FAQ 메뉴 그룹 */
.insurance-group {
    margin-top: 6px;
    margin-bottom: 12px;
}

.submenu-box {
    margin-left: 18px;
    margin-top: 8px;
    margin-bottom: 12px;
    padding: 10px 10px 8px 12px;
    border-left: 3px solid #3b82f6;
    border-radius: 0 16px 16px 0;
    background: linear-gradient(135deg, rgba(30,41,59,0.80) 0%, rgba(15,23,42,0.48) 100%);
    box-shadow: inset 0 0 0 1px rgba(148,163,184,0.06);
}

.submenu-label {
    display: inline-block;
    padding: 5px 9px;
    border-radius: 999px;
    background: rgba(37,99,235,0.18);
    color: #93c5fd;
    font-size: 10px;
    font-weight: 900;
    letter-spacing: 0.13em;
    margin-bottom: 8px;
}

/* 하위 메뉴 버튼 */
.submenu-box div.stButton > button {
    min-height: 45px !important;
    border-radius: 13px !important;
    font-size: 13px !important;
    font-weight: 700 !important;
    padding-left: 14px !important;
    margin-bottom: 7px !important;
    background: rgba(255,255,255,0.04) !important;
    border: 1px solid rgba(96,165,250,0.12) !important;
    color: #d9e8ff !important;
}

.submenu-box div.stButton > button:hover {
    background: rgba(59,130,246,0.16) !important;
    border: 1px solid rgba(96,165,250,0.30) !important;
    color: #ffffff !important;
}

/* 메인 헤더 */
.hero-box {
    background:
        radial-gradient(circle at top right, rgba(255,255,255,0.12), transparent 26%),
        linear-gradient(135deg, #0b1730 0%, #173fbe 58%, #2954d2 100%);
    border-radius: 28px;
    padding: 32px 34px;
    color: white;
    margin-bottom: 22px;
    box-shadow: 0 24px 44px rgba(15, 23, 42, 0.18);
    border: 1px solid rgba(255,255,255,0.08);
}

.hero-kicker {
    font-size: 12px;
    font-weight: 900;
    letter-spacing: 0.15em;
    color: rgba(255,255,255,0.74);
    margin-bottom: 12px;
}

.main-title {
    font-size: 50px;
    font-weight: 900;
    color: white;
    margin-bottom: 10px;
    letter-spacing: -0.03em;
}

.main-desc {
    font-size: 18px;
    color: rgba(255,255,255,0.86);
    line-height: 1.6;
    margin-bottom: 0;
}

/* 카드 */
.metric-card {
    background: linear-gradient(135deg, #ffffff 0%, #f1f5ff 100%);
    padding: 24px 22px;
    border-radius: 22px;
    border: 1px solid rgba(37, 99, 235, 0.15);
    min-height: 160px;
    box-shadow: 0 18px 32px rgba(15, 23, 42, 0.06);
    position: relative;
    overflow: hidden;
}

.metric-card::after {
    content: "";
    position: absolute;
    top: -10px;
    right: -10px;
    width: 110px;
    height: 110px;
    background: radial-gradient(circle, rgba(59,130,246,0.20), transparent 70%);
}

.metric-title {
    font-size: 14px;
    color: #64748b;
    margin-bottom: 12px;
    font-weight: 800;
    letter-spacing: 0.01em;
}

.metric-value {
    font-size: 34px;
    font-weight: 900;
    color: #0f172a;
    margin-bottom: 8px;
    letter-spacing: -0.02em;
}

.metric-badge {
    display: inline-block;
    margin-top: 10px;
    padding: 8px 12px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 800;
    background: #e0ecff;
    color: #1d4ed8;
}

/* 카드 공통 */
.table-card {
    background: linear-gradient(135deg, #ffffff 0%, #f1f5ff 100%);
    backdrop-filter: blur(8px);
    border: 1px solid rgba(37, 99, 235, 0.15);
    border-radius: 24px;
    padding: 20px;
    margin-top: 16px;
    box-shadow: 0 18px 34px rgba(15, 23, 42, 0.06);
}

.card-header {
    font-size: 20px;
    font-weight: 900;
    color: #0f172a;
    margin-bottom: 6px;
    letter-spacing: -0.02em;
    border-left: 4px solid #3b82f6;
    padding-left: 12px;
}

.card-subtext {
    font-size: 14px;
    color: #64748b;
    margin-bottom: 16px;
    line-height: 1.55;
}

/* 보험 계산 */
.form-card {
    background: linear-gradient(135deg, #ffffff 0%, #f1f5ff 100%);
    border: 1px solid rgba(37, 99, 235, 0.15);
    border-radius: 24px;
    padding: 28px 24px 22px 24px;
    box-shadow: 0 16px 32px rgba(15, 23, 42, 0.06);
    margin-top: 10px;
}

.form-card-title {
    font-size: 20px;
    font-weight: 900;
    color: #0f172a;
    margin-bottom: 6px;
}

.form-card-desc {
    font-size: 14px;
    color: #64748b;
    margin-bottom: 18px;
}

div.stFormSubmitButton > button,
div.stButton > button {
    border-radius: 16px;
    font-weight: 800;
}

div.stFormSubmitButton > button {
    width: auto !important;
    min-width: 140px;
    min-height: 54px;
    border: none !important;
    background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%) !important;
    color: white !important;
    font-size: 16px;
    text-align: center !important;
    padding: 0 24px !important;
    box-shadow: 0 10px 24px rgba(37, 99, 235, 0.28) !important;
}

div.stFormSubmitButton > button:hover {
    background: linear-gradient(135deg, #1d4ed8 0%, #1e40af 100%) !important;
    color: white !important;
}

.result-card {
    margin-top: 18px;
    background: linear-gradient(135deg, #0f172a 0%, #1d4ed8 100%);
    border-radius: 22px;
    padding: 24px 26px;
    color: white;
    box-shadow: 0 18px 36px rgba(29, 78, 216, 0.18);
}

.result-label {
    font-size: 13px;
    font-weight: 800;
    letter-spacing: 0.08em;
    color: rgba(255,255,255,0.72);
    margin-bottom: 10px;
}

.result-price {
    font-size: 38px;
    font-weight: 900;
    margin-bottom: 8px;
    letter-spacing: -0.02em;
}

.result-desc {
    font-size: 15px;
    color: rgba(255,255,255,0.82);
    line-height: 1.6;
}

/* 배지 */
.top-chip-row {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    margin-bottom: 14px;
}

.top-chip {
    display: inline-block;
    padding: 8px 12px;
    border-radius: 999px;
    background: #eaf2ff;
    color: #1d4ed8;
    font-size: 13px;
    font-weight: 800;
}

/* 탭 */
button[data-baseweb="tab"] {
    border-radius: 12px !important;
    padding: 11px 18px !important;
    font-weight: 800 !important;
    color: #475569 !important;
    background: transparent !important;
}

button[data-baseweb="tab"][aria-selected="true"] {
    background: #dbeafe !important;
    color: #1d4ed8 !important;
}

/* 입력 */
div[data-baseweb="select"] > div,
div[data-baseweb="input"] > div,
[data-testid="stNumberInput"] input {
    border-radius: 14px !important;
}

label p {
    font-weight: 800 !important;
    color: #334155 !important;
}

/* expander */
.streamlit-expanderHeader {
    font-weight: 800;
    color: #0f172a;
}

/* 데이터프레임 */
[data-testid="stDataFrame"] {
    border-radius: 14px;
    overflow: hidden;
    border: 1px solid #e2e8f0;
}

/* 작은 안내 텍스트 */
.info-chip {
    display: inline-block;
    padding: 8px 12px;
    border-radius: 999px;
    background: #eff6ff;
    color: #1d4ed8;
    font-size: 13px;
    font-weight: 800;
    margin-bottom: 14px;
}

.map-caption {
    background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
    border: 1px solid #93c5fd;
    color: #1e3a8a;
    padding: 13px 14px;
    border-radius: 16px;
    margin-bottom: 14px;
    font-size: 14px;
    line-height: 1.55;
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# 세션 상태 초기화
# ----------------------------
if "menu" not in st.session_state:
    st.session_state.menu = "차량 등록 현황 데이터"

if "insurance_open" not in st.session_state:
    st.session_state.insurance_open = False

if "faq_open" not in st.session_state:
    st.session_state.faq_open = False

# ----------------------------
# DB 데이터 로드
# ----------------------------
vehicle_df = get_vehicle_data()
region_summary = vehicle_df.groupby("지역")["등록대수"].sum().reset_index() if not vehicle_df.empty else pd.DataFrame(columns=["지역", "등록대수"])
type_summary = vehicle_df.groupby("차종")["등록대수"].sum().reset_index() if not vehicle_df.empty else pd.DataFrame(columns=["차종", "등록대수"])
insurance_type_df = get_insurance_type_data()
insurance_age_df = get_insurance_age_data()

# ----------------------------
# 사이드바
# ----------------------------
with st.sidebar:
    st.markdown("""
    <div class="sidebar-brand-box">
        <div class="sidebar-badge">MOBILITY · INSURANCE · ANALYTICS</div>
        <div class="sidebar-main-title">Drive Insight</div>
        <div class="sidebar-subtitle">
            자동차 등록 데이터와 보험 정보를 위한 모빌리티 데이터 대시보드
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sidebar-menu-title">MENU</div>', unsafe_allow_html=True)

    if st.button("차량 등록 현황 데이터", use_container_width=True):
        st.session_state.menu = "차량 등록 현황 데이터"

    st.markdown('<div class="insurance-group">', unsafe_allow_html=True)
    insurance_label = "자동차 보험 정보  ▼" if st.session_state.insurance_open else "자동차 보험 정보  ▸"
    if st.button(insurance_label, use_container_width=True):
        st.session_state.insurance_open = not st.session_state.insurance_open

    if st.session_state.insurance_open:
        st.markdown("""
        <div class="submenu-box">
            <div class="submenu-label">INSURANCE MENU</div>
        """, unsafe_allow_html=True)

        if st.button("ㆍ 보험 통계 현황", use_container_width=True):
            st.session_state.menu = "보험 통계 현황"

        if st.button("ㆍ 보험료 조회", use_container_width=True):
            st.session_state.menu = "보험료 조회"

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("FAQ", use_container_width=True):
        st.session_state.menu = "FAQ"

menu = st.session_state.menu

# ----------------------------
# 차량 등록 현황
# ----------------------------
if menu == "차량 등록 현황 데이터":
    st.markdown("""
    <div class="hero-box">
        <div class="hero-kicker">VEHICLE REGISTRATION DASHBOARD</div>
        <div class="main-title">자동차 등록 현황</div>
        <div class="main-desc">주요 지역 및 차종별 등록 데이터를 기반으로 핵심 인사이트를 확인할 수 있습니다.</div>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs(["연도별", "지역별", "성/연령별", "차종 검색"])

    with tab1:
        st.markdown('<div class="info-chip">연도별 자동차 등록 현황</div>', unsafe_allow_html=True)

        def get_vehicle_registration_df():
            try:
                conn = mysql.connector.connect(**CAR_DB_CONFIG)
                cursor = conn.cursor(dictionary=True)
                query = "SELECT * FROM vehicle_registration ORDER BY year, type"
                cursor.execute(query)
                data = cursor.fetchall()
                df = pd.DataFrame(data)
                cursor.close()
                conn.close()
                return df
            except Error as e:
                st.error(f"DB 오류: {e}")
                return pd.DataFrame()

        vehicle_year_df = get_vehicle_registration_df()

        if vehicle_year_df.empty:
            st.info("데이터가 없습니다.")
        else:
            vehicle_year_df.rename(columns={
                "type": "차종",
                "total": "전체",
                "government": "관용",
                "private": "자가용",
                "commercial": "영업용",
                "year": "연도"
            }, inplace=True)

            years = sorted(vehicle_year_df["연도"].unique())
            year_tabs = st.tabs([str(y) for y in years])

            for i, year in enumerate(years):
                with year_tabs[i]:
                    st.markdown(f"""
                    <div class="card-header">{year}년 차량 등록 현황</div>
                    <div class="card-subtext">연도별 차종 구분과 용도별 등록 흐름을 확인할 수 있습니다.</div>
                    """, unsafe_allow_html=True)

                    year_df = vehicle_year_df[vehicle_year_df["연도"] == year].copy()
                    year_df_display = year_df.set_index("차종")[["전체", "관용", "자가용", "영업용"]]

                    st.markdown("### 등록대수 표")
                    st.dataframe(year_df_display.style.format("{:,}대"), use_container_width=True)

                    st.markdown("### 등록대수 그래프")
                    chart_df = year_df_display.reset_index().melt(
                        id_vars="차종",
                        value_vars=["전체", "관용", "자가용", "영업용"],
                        var_name="구분",
                        value_name="등록대수"
                    )

                    chart = alt.Chart(chart_df).mark_bar().encode(
                        x=alt.X("차종:N", axis=alt.Axis(labelAngle=0)),  # 🔥 가로로!
                        y="등록대수:Q",
                        color="구분:N"
                    )

                    st.altair_chart(chart, use_container_width=True)
    with tab2:
        if region_summary.empty:
            st.info("데이터가 없습니다.")
        else:
            col1, col2 = st.columns(2)

            max_region = region_summary.loc[region_summary["등록대수"].idxmax()]
            with col1:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-title">등록대수 최고 지역</div>
                    <div class="metric-value">{max_region['지역']}</div>
                    <div class="metric-badge">등록대수 {max_region['등록대수']:,}대</div>
                </div>
                """, unsafe_allow_html=True)

            total_region_count = region_summary["등록대수"].sum()
            with col2:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-title">전체 등록대수</div>
                    <div class="metric-value">{total_region_count:,}대</div>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("""
            <div class="card-header">지역별 등록 현황</div>
            <div class="card-subtext">지역 단위 등록대수 현황과 분포를 함께 확인할 수 있습니다.</div>
            """, unsafe_allow_html=True)
            st.dataframe(region_summary, use_container_width=True)

            chart = alt.Chart(region_summary).mark_bar().encode(
                x=alt.X("지역:N", axis=alt.Axis(labelAngle=0)),  # 🔥 가로로!
                y=alt.Y("등록대수:Q")
            )

            st.altair_chart(chart, use_container_width=True)

            st.markdown("""
            <div class="card-header">상위 5개 지역 차량 분포 지도</div>
            <div class="card-subtext">등록대수 상위 지역을 지도 위에서 직관적으로 확인할 수 있습니다.</div>
            """, unsafe_allow_html=True)

            with st.spinner("지도를 불러오는 중..."):
                top5_map = build_top5_map(region_summary)
                st_folium(top5_map, use_container_width=True, height=520, returned_objects=[])

    with tab3:
        st.markdown('<div class="info-chip">성별·연령별 등록 현황</div>', unsafe_allow_html=True)

        gender_age_df = get_insurance_gender_age_data()

        if gender_age_df.empty:
            st.info("데이터가 없습니다.")
        else:
            gender_age_df['등록대수'] = pd.to_numeric(gender_age_df['등록대수'], errors='coerce').fillna(0)

            if gender_age_df['등록대수'].sum() == 0:
                st.info("등록대수 데이터가 없습니다.")
            else:
                import matplotlib
                import platform

                if platform.system() == 'Windows':
                    matplotlib.rc('font', family='Malgun Gothic')
                elif platform.system() == 'Darwin':
                    matplotlib.rc('font', family='AppleGothic')
                else:
                    matplotlib.rc('font', family='NanumGothic')

                gender_summary = gender_age_df.groupby("성별")["등록대수"].sum()
                age_summary = gender_age_df.groupby("연령대")["등록대수"].sum()

                st.markdown("""
                <div class="card-header">성별·연령별 상세 데이터</div>
                <div class="card-subtext">성별, 연령대, 지역 기준 등록 데이터를 상세하게 확인할 수 있습니다.</div>
                """, unsafe_allow_html=True)
                st.dataframe(gender_age_df, use_container_width=True)

                col_table, col_graph = st.columns(2)

                with col_table:
                    st.markdown("""
                    <div class="card-header">성별 등록 비율</div>
                    <div class="card-subtext">성별 기준 차량 등록 비중을 한눈에 보여줍니다.</div>
                    """, unsafe_allow_html=True)

                    fig, ax = plt.subplots(figsize=(2.5, 2.5))
                    gender_summary.plot(
                        kind="pie",
                        autopct="%1.1f%%",
                        colors=["green", "blue", "#f43f5e"],
                        startangle=90,
                        ax=ax
                    )
                    ax.set_ylabel("")
                    ax.axis("equal")
                    st.pyplot(fig, use_container_width=True)

                with col_graph:
                    st.markdown("""
                    <div class="card-header">연령대 등록대수 추이</div>
                    <div class="card-subtext">연령대별 등록 규모를 선형 흐름으로 비교합니다.</div>
                    """, unsafe_allow_html=True)

                    fig, ax = plt.subplots(figsize=(3, 2.45))
                    age_summary.plot(
                        kind="line",
                        marker='o',
                        ax=ax
                    )
                    ax.set_ylabel("등록대수")
                    ax.set_xlabel("연령대")
                    ax.grid(True, linestyle='--', alpha=0.5)
                    st.pyplot(fig, use_container_width=True)        
    with tab4:
        st.markdown('<div class="info-chip">전국 자동차 등록 조회</div>', unsafe_allow_html=True)

        if vehicle_df.empty:
            st.info("데이터가 없습니다.")
        else:
            regions = ["전체"] + sorted(vehicle_df["지역"].unique().tolist())
            types = sorted(vehicle_df["차종"].unique().tolist())

            search_region = st.selectbox("지역 선택", regions)
            search_types = st.multiselect("차종 선택 (여러 개 선택 가능)", types, default=types)

            filtered_df = vehicle_df.copy()
            if search_region != "전체":
                filtered_df = filtered_df[filtered_df["지역"] == search_region]
            if search_types:
                filtered_df = filtered_df[filtered_df["차종"].isin(search_types)]

            if filtered_df.empty:
                st.info("검색 결과가 없습니다.")
            else:
                st.markdown("""
                <div class="card-header">조건별 등록 데이터</div>
                <div class="card-subtext">선택한 지역과 차종 기준으로 등록 현황을 조회할 수 있습니다.</div>
                """, unsafe_allow_html=True)

                st.dataframe(filtered_df, use_container_width=True)

                csv_data = filtered_df.to_csv(index=False).encode('utf-8-sig')
                st.download_button(
                    label="CSV 다운로드",
                    data=csv_data,
                    file_name="vehicle_registration.csv",
                    mime="text/csv"
                )
# ----------------------------
# 보험 통계 현황
# ----------------------------
elif menu == "보험 통계 현황":
    st.markdown("""
    <div class="hero-box">
        <div class="hero-kicker">AUTO INSURANCE ANALYTICS</div>
        <div class="main-title">보험 통계 현황</div>
        <div class="main-desc">차종별, 성·연령별 보험 가입 현황과 평균 보험료 흐름을 확인할 수 있습니다.</div>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["차종별", "성/연령별"])

    with tab1:
        st.markdown("""
        <div class="card-header">차종별 평균 보험료 현황</div>
        <div class="card-subtext">소형, 중형, 대형, 다인승 차종의 평균 보험료를 비교합니다.</div>
        """, unsafe_allow_html=True)

        if not insurance_type_df.empty:
            chart_df = insurance_type_df.copy()

            # 컬럼명 통일
            chart_df = chart_df.rename(columns={"평균보험료": "평균 보험료"})

            # 필요한 컬럼만 남기기
            chart_df = chart_df[["차종", "평균 보험료"]]

            # 숫자형 변환
            chart_df["평균 보험료"] = pd.to_numeric(chart_df["평균 보험료"], errors="coerce")

            # 결측 제거
            chart_df = chart_df.dropna(subset=["평균 보험료"])

            # 차종 순서 고정
            car_order = ["소형", "중형", "대형", "다인승"]
            chart_df["차종"] = pd.Categorical(chart_df["차종"], categories=car_order, ordered=True)
            chart_df = chart_df.sort_values("차종")

            # 표
            st.dataframe(
                chart_df.style.format({"평균 보험료": "{:,.0f}"}),
                use_container_width=True,
                hide_index=True
            )

            # 그래프
            chart = alt.Chart(chart_df).mark_bar().encode(
                x=alt.X("차종:N", axis=alt.Axis(labelAngle=0), title="차종"),
                y=alt.Y("평균 보험료:Q", title="평균 보험료"),
                tooltip=[
                    alt.Tooltip("차종:N", title="차종"),
                    alt.Tooltip("평균 보험료:Q", title="평균 보험료", format=",.0f")
                ]
            ).properties(
                height=400
            )

            st.altair_chart(chart, use_container_width=True)

            with tab2:
                st.markdown("""
                <div class="card-header">연령대별 평균 보험료 현황</div>
                <div class="card-subtext">연령대별 평균 보험료를 비교합니다.</div>
                """, unsafe_allow_html=True)

                if not insurance_age_df.empty:
                    chart_df = insurance_age_df.copy()

                    # 컬럼명 통일
                    chart_df = chart_df.rename(columns={"평균보험료": "평균 보험료"})

                    # 필요한 컬럼만 사용
                    chart_df = chart_df[["구분", "평균 보험료"]]

                    # 숫자형 변환
                    chart_df["평균 보험료"] = pd.to_numeric(chart_df["평균 보험료"], errors="coerce")

                    # 결측 제거
                    chart_df = chart_df.dropna(subset=["평균 보험료"])

                    # 연령대 순서 고정
                    age_order = ["20대", "30대", "40대", "50대 이상"]
                    chart_df["구분"] = pd.Categorical(chart_df["구분"], categories=age_order, ordered=True)
                    chart_df = chart_df.sort_values("구분")

                    # 표
                    st.dataframe(
                        chart_df.style.format({"평균 보험료": "{:,.0f}"}),
                        use_container_width=True,
                        hide_index=True
                    )

                    # 그래프
                    chart = alt.Chart(chart_df).mark_bar().encode(
                        x=alt.X("구분:N", axis=alt.Axis(labelAngle=0), title="연령대"),
                        y=alt.Y("평균 보험료:Q", title="평균 보험료"),
                        tooltip=[
                            alt.Tooltip("구분:N", title="연령대"),
                            alt.Tooltip("평균보험료:Q", title="평균 보험료", format=",.0f")
                        ]
                    ).properties(
                        height=400
                    )

                    st.altair_chart(chart, use_container_width=True)

# ----------------------------
# 보험료 계산
# ----------------------------
elif menu == "보험료 조회":
    st.markdown("""
    <div class="hero-box">
        <div class="hero-kicker">INSURANCE PRICE ESTIMATOR</div>
        <div class="main-title">보험료 조회</div>
        <div class="main-desc">성별, 나이, 연식, 국산/외산, 제조사, 모델명을 입력하면 DB 기반 예상 보험료를 조회할 수 있습니다.</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card-header">보험료 시뮬레이션 입력</div>
    <div class="card-subtext">사용자 입력값을 바탕으로 연결된 DB에서 차량정보와 보험통계를 조회해 예상 보험료를 계산합니다.</div>
    """, unsafe_allow_html=True)

    origin_options = get_origin_options()
    col1, col2, col3 = st.columns(3)

    with col1:
        gender = st.selectbox("성별", ["남성", "여성"])
        age = st.number_input("나이", min_value=18, max_value=100, value=30, step=1)

    with col2:
        model_year = st.number_input("연식", min_value=1990, max_value=2030, value=2025, step=1)
        origin_type = st.selectbox("국산/외산", origin_options)

    maker_options = get_maker_options(origin_type)
    with col3:
        maker_name = st.selectbox("제조사", maker_options, disabled=not maker_options)
        model_options = get_model_options(origin_type, maker_name) if maker_name else []
        model_name = st.selectbox("모델명", model_options, disabled=not model_options)

    if st.button("보험료 계산"):
        if not maker_options or not model_options:
            st.error("선택 가능한 제조사 또는 모델이 없습니다. car_master 데이터를 확인해주세요.")
        else:
            try:
                result = calculate_expected_premium(
                    gender_label=gender,
                    age=int(age),
                    model_year=int(model_year),
                    origin_type=origin_type,
                    maker_name=maker_name,
                    model_name=model_name,
                )

                st.markdown(f"""
                <div class="result-card">
                    <div class="result-label">ESTIMATED INSURANCE PRICE</div>
                    <div class="result-price">{result['premium']:,} 원</div>
                    <div class="result-desc">입력한 조건과 DB 통계를 반영해 산출한 예상 보험료입니다.</div>
                </div>
                """, unsafe_allow_html=True)

                st.markdown(
                    '<div class="top-chip-row">'
                    f'<div class="top-chip">연령대: {result["age_group"]}</div>'
                    f'<div class="top-chip">차급: {result["vehicle_class"]}</div>'
                    f'<div class="top-chip">차종: {result["body_type"]}</div>'
                    f'<div class="top-chip">잔존가치율: {result["residual_value_rate"]:.2f}</div>'
                    '</div>',
                    unsafe_allow_html=True
                )

                with st.expander("산출 근거 보기"):
                    st.write(f"전체 평균보험료: {result['overall_avg_premium']*10:,} 원")
                    st.write(f"선택 집단 평균보험료: {result['group_avg_premium']*10:,} 원")
                    st.write(f"가입위험계수: {result['enrollment_risk_factor']:.4f}")
                    st.write(f"손해위험계수: {result['loss_risk_factor']:.4f}")
                    st.write(f"차량가치계수: {result['vehicle_value_factor']:.4f}")
                    st.write(f"모델가격계수: {result['model_price_factor']:.4f}")

            except Exception as e:
                st.error(f"보험료 계산 중 오류가 발생했습니다: {e}")

# ----------------------------
# FAQ
# ----------------------------
elif menu == "FAQ":
    st.markdown("""
    <div class="hero-box">
        <div class="hero-kicker">INSURANCE FAQ CENTER</div>
        <div class="main-title">FAQ</div>
        <div class="main-desc">보험사별 자주 묻는 질문을 회사 단위로 조회할 수 있습니다.</div>
    </div>
    """, unsafe_allow_html=True)

    company_options = ["삼성화재", "현대해상", "DB손해보험"]
    selected_company = st.selectbox("회사 선택", company_options)

    if selected_company == "삼성화재":
        df = load_samsung()
    elif selected_company == "현대해상":
        df = load_hyundai()
    elif selected_company == "DB손해보험":
        df = load_db()
    else:
        st.error("회사 선택이 잘못되었습니다.")
        df = pd.DataFrame()

    if not df.empty:
        st.markdown("""
        <div class="card-header">FAQ 목록</div>
        <div class="card-subtext">선택한 보험사의 질문과 답변을 확인할 수 있습니다.</div>
        """, unsafe_allow_html=True)
        render_company_faq(selected_company, df)