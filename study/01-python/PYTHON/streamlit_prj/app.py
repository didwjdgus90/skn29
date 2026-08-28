"""
Streamlit 버전: 쇼핑몰 데이터베이스 대시보드 (MySQL)
데이터베이스의 통계 및 시각화를 보여주는 인터랙티브 대시보드

실행 방법:
streamlit run shop_db_streamlit_mysql.py
"""

# 필요한 라이브러리
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
from shop_db_manger import ShopDB, create_tables, insert_sample_data
import os
from dotenv import load_dotenv

load_dotenv() # 환경 변수 설정


DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', ''),
    'database': os.getenv('DB_NAME', 'shop_db'),
    'port': int(os.getenv('DB_PORT', 3306))
}

# ===== 페이지 설정 =====
st.set_page_config(
    page_title="쇼핑몰 데이터 대시보드 (MySQL)",
    page_icon="",
    layout="wide"
)


# ===== 데이터베이스 연결 =====
@st.cache_resource
def get_database_connection():
    """데이터베이스 연결 (캐싱)"""
    db = ShopDB(**DB_CONFIG)
    db.connect()
    return db


def init_database():
    """데이터베이스 초기화"""
    db = get_database_connection()
    create_tables(db)
    insert_sample_data(db)
    st.success("데이터베이스가 초기화되었습니다!")
    st.rerun()


def execute_query(query):
    """쿼리 실행 및 결과 반환"""
    db = get_database_connection()
    try:
        db.execute(query)
        
        # SELECT 쿼리인 경우 결과 반환
        if query.strip().upper().startswith('SELECT'):
            results = db.fetchall()
            columns = [desc[0] for desc in db.cursor.description]
            return pd.DataFrame(results, columns=columns)
        else:
            db.commit()
            return None
    except Exception as e:
        st.error(f"쿼리 실행 오류: {e}")
        return None


# ===== 대시보드 통계 함수 =====
def get_dashboard_stats():
    """대시보드 메인 통계 조회"""
    stats = {}
    
    # 총 고객 수
    df = execute_query("SELECT COUNT(*) as count FROM customers")
    stats['total_customers'] = df['count'].iloc[0] if not df.empty else 0
    
    # 총 주문 수
    df = execute_query("SELECT COUNT(*) as count FROM orders")
    stats['total_orders'] = df['count'].iloc[0] if not df.empty else 0
    
    # 총 매출
    df = execute_query("SELECT SUM(total_amount) as total FROM orders WHERE status = 'Completed'")
    stats['total_revenue'] = df['total'].iloc[0] if not df.empty and pd.notna(df['total'].iloc[0]) else 0
    
    # 평균 주문 금액
    df = execute_query("SELECT AVG(total_amount) as avg FROM orders WHERE status = 'Completed'")
    stats['avg_order_value'] = df['avg'].iloc[0] if not df.empty and pd.notna(df['avg'].iloc[0]) else 0
    
    return stats


# ===== 메인 UI =====
def main():
    """메인 애플리케이션"""
    
    # 타이틀
    st.title("쇼핑몰 데이터 대시보드 (MySQL)")
    st.markdown("---")
    
    # 사이드바 메뉴
    with st.sidebar:
        st.header("메뉴")
        
        # 데이터베이스 초기화 버튼
        st.markdown("### 데이터베이스 관리")
        if st.button("데이터베이스 초기화", type="primary"):
            with st.spinner("데이터베이스를 초기화하는 중..."):
                init_database()
        st.markdown("---")
        
        # 메뉴 선택
        menu = st.radio(
            "뷰 선택",
            [
                "메인 대시보드",
                "고객 분석",
                "상품 분석",
                "주문 분석",
                "매출 분석",
                "원본 데이터",
                "커스텀 쿼리"
            ]
        )
    
    # 선택된 메뉴에 따라 뷰 표시
    if menu == "메인 대시보드":
        show_main_dashboard()
    elif menu == "고객 분석":
        show_customer_analysis()
    elif menu == "상품 분석":
        show_product_analysis()
    elif menu == "주문 분석":
        show_order_analysis()
    elif menu == "매출 분석":
        show_revenue_analysis()
    elif menu == "원본 데이터":
        show_raw_data()
    elif menu == "커스텀 쿼리":
        show_custom_query()


# ===== 대시보드 뷰 함수들 =====

def show_main_dashboard():
    """메인 대시보드 뷰"""
    st.header("메인 대시보드")
    
    # 주요 지표 표시
    stats = get_dashboard_stats()
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="총 고객 수",
            value=f"{stats['total_customers']:,}명"
        )
    
    with col2:
        st.metric(
            label="총 주문 수",
            value=f"{stats['total_orders']:,}건"
        )
    
    with col3:
        st.metric(
            label="총 매출",
            value=f"₩{stats['total_revenue']:,.0f}"
        )
    
    with col4:
        st.metric(
            label="평균 주문액",
            value=f"₩{stats['avg_order_value']:,.0f}"
        )
    
    st.markdown("---")
    
    # 그래프 영역
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("등급별 고객 분포")
        df = execute_query("""
            SELECT grade, COUNT(*) as count
            FROM customers
            GROUP BY grade
            ORDER BY count DESC
        """)
        
        if not df.empty:
            fig = px.pie(df, values='count', names='grade', 
                        title='고객 등급 분포',
                        color_discrete_sequence=px.colors.sequential.RdBu)
            st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("카테고리별 상품 수")
        df = execute_query("""
            SELECT category, COUNT(*) as count
            FROM products
            GROUP BY category
            ORDER BY count DESC
        """)
        
        if not df.empty:
            fig = px.bar(df, x='category', y='count',
                        title='카테고리별 상품 수',
                        color='count',
                        color_continuous_scale='Blues')
            st.plotly_chart(fig, use_container_width=True)
    
    # 최근 주문 현황
    st.subheader("최근 주문 내역")
    df = execute_query("""
        SELECT 
            o.order_id,
            c.name as customer_name,
            o.order_date,
            o.total_amount,
            o.status
        FROM orders o
        JOIN customers c ON o.customer_id = c.customer_id
        ORDER BY o.order_date DESC
        LIMIT 10
    """)
    
    if not df.empty:
        st.dataframe(df, use_container_width=True, hide_index=True)


def show_customer_analysis():
    """고객 분석 뷰"""
    st.header("고객 분석")
    
    # 탭 생성
    tab1, tab2, tab3 = st.tabs(["고객 통계", "VIP 고객", "고객 활동"])
    
    with tab1:
        st.subheader("고객 등급별 통계")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # 등급별 고객 수
            df = execute_query("""
                SELECT grade, COUNT(*) as count
                FROM customers
                GROUP BY grade
                ORDER BY 
                    CASE grade
                        WHEN 'Gold' THEN 1
                        WHEN 'Silver' THEN 2
                        WHEN 'Bronze' THEN 3
                    END
            """)
            
            if not df.empty:
                fig = px.bar(df, x='grade', y='count',
                            title='등급별 고객 수',
                            color='grade',
                            color_discrete_map={'Gold':'gold', 'Silver':'silver', 'Bronze':'#CD7F32'})
                st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # 등급별 평균 포인트
            df = execute_query("""
                SELECT grade, AVG(point) as avg_point
                FROM customers
                GROUP BY grade
                ORDER BY avg_point DESC
            """)
            
            if not df.empty:
                fig = px.bar(df, x='grade', y='avg_point',
                            title='등급별 평균 포인트',
                            color='avg_point',
                            color_continuous_scale='Viridis')
                st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.subheader("VIP 고객 (구매 금액 상위)")
        
        df = execute_query("""
            SELECT 
                c.customer_id,
                c.name,
                c.grade,
                c.point,
                COUNT(o.order_id) as order_count,
                SUM(o.total_amount) as total_purchase
            FROM customers c
            LEFT JOIN orders o ON c.customer_id = o.customer_id AND o.status = 'Completed'
            GROUP BY c.customer_id, c.name, c.grade, c.point
            HAVING total_purchase > 0
            ORDER BY total_purchase DESC
            LIMIT 10
        """)
        
        if not df.empty:
            st.dataframe(df, use_container_width=True, hide_index=True)
            
            # VIP 고객 시각화
            fig = px.bar(df, x='name', y='total_purchase',
                        title='상위 10명 고객 구매액',
                        color='grade',
                        color_discrete_map={'Gold':'gold', 'Silver':'silver', 'Bronze':'#CD7F32'})
            st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        st.subheader("월별 신규 가입 고객")
        
        df = execute_query("""
            SELECT 
                DATE_FORMAT(join_date, '%Y-%m') as month,
                COUNT(*) as new_customers
            FROM customers
            GROUP BY DATE_FORMAT(join_date, '%Y-%m')
            ORDER BY month
        """)
        
        if not df.empty:
            fig = px.line(df, x='month', y='new_customers',
                         title='월별 신규 고객 수',
                         markers=True)
            st.plotly_chart(fig, use_container_width=True)


def show_product_analysis():
    """상품 분석 뷰"""
    st.header("상품 분석")
    
    tab1, tab2, tab3 = st.tabs(["상품 통계", "인기 상품", "재고 현황"])
    
    with tab1:
        st.subheader("카테고리별 상품 통계")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # 카테고리별 상품 수
            df = execute_query("""
                SELECT category, COUNT(*) as count
                FROM products
                GROUP BY category
                ORDER BY count DESC
            """)
            
            if not df.empty:
                fig = px.pie(df, values='count', names='category',
                            title='카테고리별 상품 수')
                st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # 카테고리별 평균 가격
            df = execute_query("""
                SELECT category, AVG(price) as avg_price
                FROM products
                GROUP BY category
                ORDER BY avg_price DESC
            """)
            
            if not df.empty:
                fig = px.bar(df, x='category', y='avg_price',
                            title='카테고리별 평균 가격',
                            color='avg_price',
                            color_continuous_scale='Blues')
                st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.subheader("판매량 상위 상품")
        
        df = execute_query("""
            SELECT 
                p.product_id,
                p.product_name,
                p.category,
                p.price,
                COALESCE(SUM(od.quantity), 0) as total_sold,
                COALESCE(SUM(od.subtotal), 0) as total_revenue
            FROM products p
            LEFT JOIN order_details od ON p.product_id = od.product_id
            GROUP BY p.product_id, p.product_name, p.category, p.price
            ORDER BY total_sold DESC
            LIMIT 10
        """)
        
        if not df.empty:
            st.dataframe(df, use_container_width=True, hide_index=True)
            
            fig = px.bar(df, x='product_name', y='total_sold',
                        title='판매량 상위 10개 상품',
                        color='category')
            st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        st.subheader("재고 현황")
        
        df = execute_query("""
            SELECT 
                product_name,
                category,
                price,
                stock
            FROM products
            ORDER BY stock ASC
        """)
        
        if not df.empty:
            st.dataframe(df, use_container_width=True, hide_index=True)
            
            # 재고 부족 상품 (재고 30개 이하)
            st.warning("재고 부족 상품 (30개 이하)")
            low_stock = df[df['stock'] <= 30]
            if not low_stock.empty:
                st.dataframe(low_stock, use_container_width=True, hide_index=True)
            else:
                st.info("재고 부족 상품이 없습니다.")


def show_order_analysis():
    """주문 분석 뷰"""
    st.header("주문 분석")
    
    tab1, tab2, tab3 = st.tabs(["주문 통계", "일별 주문", "주문 상세"])
    
    with tab1:
        st.subheader("주문 상태별 통계")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # 상태별 주문 수
            df = execute_query("""
                SELECT status, COUNT(*) as count
                FROM orders
                GROUP BY status
                ORDER BY count DESC
            """)
            
            if not df.empty:
                fig = px.pie(df, values='count', names='status',
                            title='주문 상태 분포')
                st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # 상태별 총 금액
            df = execute_query("""
                SELECT status, SUM(total_amount) as total
                FROM orders
                GROUP BY status
                ORDER BY total DESC
            """)
            
            if not df.empty:
                fig = px.bar(df, x='status', y='total',
                            title='상태별 총 주문 금액',
                            color='total',
                            color_continuous_scale='Greens')
                st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.subheader("일별 주문 현황")
        
        df = execute_query("""
            SELECT 
                DATE(order_date) as order_day,
                COUNT(*) as order_count,
                SUM(total_amount) as daily_revenue
            FROM orders
            WHERE status = 'Completed'
            GROUP BY DATE(order_date)
            ORDER BY order_day
        """)
        
        if not df.empty:
            col1, col2 = st.columns(2)
            
            with col1:
                fig = px.line(df, x='order_day', y='order_count',
                             title='일별 주문 건수',
                             markers=True)
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                fig = px.line(df, x='order_day', y='daily_revenue',
                             title='일별 매출',
                             markers=True)
                st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        st.subheader("주문 상세 내역")
        
        df = execute_query("""
            SELECT 
                o.order_id,
                c.name as customer_name,
                o.order_date,
                p.product_name,
                od.quantity,
                od.unit_price,
                od.subtotal,
                o.status
            FROM orders o
            JOIN customers c ON o.customer_id = c.customer_id
            JOIN order_details od ON o.order_id = od.order_id
            JOIN products p ON od.product_id = p.product_id
            ORDER BY o.order_date DESC
            LIMIT 50
        """)
        
        if not df.empty:
            st.dataframe(df, use_container_width=True, hide_index=True)


def show_revenue_analysis():
    """매출 분석 뷰"""
    st.header("매출 분석")
    
    tab1, tab2, tab3 = st.tabs(["전체 매출", "카테고리별", "고객별"])
    
    with tab1:
        st.subheader("전체 매출 현황")
        
        # 총 매출 통계
        df = execute_query("""
            SELECT 
                COUNT(*) as total_orders,
                SUM(total_amount) as total_revenue,
                AVG(total_amount) as avg_order_value,
                MAX(total_amount) as max_order_value,
                MIN(total_amount) as min_order_value
            FROM orders
            WHERE status = 'Completed'
        """)
        
        if not df.empty:
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("총 매출", f"₩{df['total_revenue'].iloc[0]:,.0f}")
                st.metric("평균 주문액", f"₩{df['avg_order_value'].iloc[0]:,.0f}")
            
            with col2:
                st.metric("총 주문 수", f"{df['total_orders'].iloc[0]:,}건")
                st.metric("최고 주문액", f"₩{df['max_order_value'].iloc[0]:,.0f}")
            
            with col3:
                st.metric("최저 주문액", f"₩{df['min_order_value'].iloc[0]:,.0f}")
        
        # 일별 매출 추이
        df = execute_query("""
            SELECT 
                DATE(order_date) as order_day,
                SUM(total_amount) as daily_revenue
            FROM orders
            WHERE status = 'Completed'
            GROUP BY DATE(order_date)
            ORDER BY order_day
        """)
        
        if not df.empty:
            fig = px.area(df, x='order_day', y='daily_revenue',
                         title='일별 매출 추이')
            st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.subheader("카테고리별 매출")
        
        df = execute_query("""
            SELECT 
                p.category,
                COUNT(DISTINCT o.order_id) as order_count,
                SUM(od.quantity) as items_sold,
                SUM(od.subtotal) as total_revenue
            FROM orders o
            JOIN order_details od ON o.order_id = od.order_id
            JOIN products p ON od.product_id = p.product_id
            WHERE o.status = 'Completed'
            GROUP BY p.category
            ORDER BY total_revenue DESC
        """)
        
        if not df.empty:
            st.dataframe(df, use_container_width=True, hide_index=True)
            
            col1, col2 = st.columns(2)
            
            with col1:
                fig = px.pie(df, values='total_revenue', names='category',
                            title='카테고리별 매출 비중')
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                fig = px.bar(df, x='category', y='items_sold',
                            title='카테고리별 판매 수량',
                            color='items_sold',
                            color_continuous_scale='Blues')
                st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        st.subheader("고객별 매출")
        
        df = execute_query("""
            SELECT 
                c.customer_id,
                c.name,
                c.grade,
                COUNT(o.order_id) as order_count,
                SUM(o.total_amount) as total_purchase,
                AVG(o.total_amount) as avg_purchase
            FROM customers c
            LEFT JOIN orders o ON c.customer_id = o.customer_id AND o.status = 'Completed'
            GROUP BY c.customer_id, c.name, c.grade
            HAVING total_purchase > 0
            ORDER BY total_purchase DESC
            LIMIT 20
        """)
        
        if not df.empty:
            st.dataframe(df, use_container_width=True, hide_index=True)
            df['avg_purchase'] = pd.to_numeric(df['avg_purchase']) # 문자처럼 저장된 숫자를 진짜 숫자로 바꿔주는 코드
            fig = px.scatter(df, x='order_count', y='total_purchase',
                           size='avg_purchase', color='grade',
                           hover_data=['name'],
                           title='고객별 주문 건수 vs 총 구매액',
                           color_discrete_map={'Gold':'gold', 'Silver':'silver', 'Bronze':'#CD7F32'})
            st.plotly_chart(fig, use_container_width=True)


def show_raw_data():
    """원본 데이터 뷰"""
    st.header("원본 데이터")
    
    # 테이블 선택
    table = st.selectbox(
        "테이블 선택",
        ["customers", "products", "orders", "order_details"]
    )
    
    # 데이터 조회
    df = execute_query(f"SELECT * FROM {table}")
    
    if not df.empty:
        st.subheader(f"{table} 테이블 ({len(df)}개 행)")
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        # CSV 다운로드 버튼
        csv = df.to_csv(index=False, encoding='utf-8-sig')
        st.download_button(
            label="CSV 다운로드",
            data=csv,
            file_name=f"{table}.csv",
            mime="text/csv"
        )


def show_custom_query():
    """커스텀 쿼리 뷰"""
    st.header("커스텀 SQL 쿼리")
    
    st.info("""
    **사용 가능한 테이블:**
    - `customers` (고객)
    - `products` (상품)
    - `orders` (주문)
    - `order_details` (주문 상세)
    """)
    
    # 예제 쿼리
    with st.expander("예제 쿼리 보기"):
        st.code("""
-- 1. 고객별 총 구매 금액
SELECT c.name, SUM(o.total_amount) as total
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE o.status = 'Completed'
GROUP BY c.name
ORDER BY total DESC;

-- 2. 카테고리별 평균 가격
SELECT category, AVG(price) as avg_price
FROM products
GROUP BY category;

-- 3. 일별 주문 통계
SELECT DATE(order_date) as date, COUNT(*) as orders
FROM orders
GROUP BY DATE(order_date)
ORDER BY date DESC;
        """, language="sql")
    
    # 쿼리 입력
    query = st.text_area(
        "SQL 쿼리 입력",
        height=200,
        placeholder="SELECT * FROM customers LIMIT 10;"
    )
    
    # 실행 버튼
    if st.button("쿼리 실행", type="primary"):
        if query.strip():
            with st.spinner("쿼리 실행 중..."):
                try:
                    df = execute_query(query)
                    if df is not None and not df.empty:
                        st.success(f"{len(df)}개 행 조회")
                        st.dataframe(df, use_container_width=True, hide_index=True)
                    elif df is not None:
                        st.info("조회 결과가 없습니다.")
                    else:
                        st.warning("쿼리가 실행되었지만 반환된 결과가 없습니다.")
                except Exception as e:
                    st.error(f"오류: {e}")
        else:
            st.warning("쿼리를 입력해주세요.")


# ===== 실행 =====
if __name__ == "__main__":
    main()
