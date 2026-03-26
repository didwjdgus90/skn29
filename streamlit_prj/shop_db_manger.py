'''
쇼핑몰 데이터베이스 관리 모듈
mysql을 사용하여 쇼핑몰 데이터베이스를 관리하는 클래스와 유틸리티 함수들
'''
import mysql.connector
from mysql.connector import Error
from datetime import datetime, timedelta
import pandas as pd

class ShopDB:
    """쇼핑몰 데이터베이스 관리 클래스 (MySQL)"""
    
    def __init__(self, host, user, password, database, port=3306):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.conn = None
        self.cursor = None
    
    def connect(self):
        """데이터베이스 연결"""
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                port=self.port
            )
            self.cursor = self.conn.cursor()
            
            # 데이터베이스 생성 및 선택
            self.cursor.execute(
                f"CREATE DATABASE IF NOT EXISTS {self.database} " # 존재하지 않으면 생성
                "CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"
            )
            self.cursor.execute(f"USE {self.database}")
            
            print(f" MySQL 데이터베이스 '{self.database}' 연결 성공!")
            return True
        except Error as e:
            print(f" 연결 실패: {e}")
            return False
    
    def close(self):
        """연결 종료"""
        if self.cursor:
            self.cursor.close()
        if self.conn and self.conn.is_connected():
            self.conn.close()
            print(" 연결 종료")
    
    def execute(self, query, params=None):
        """쿼리 실행"""
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            return True
        except Error as e:
            print(f"❌ 쿼리 오류: {e}")
            return False
    
    def fetchall(self):
        return self.cursor.fetchall() # 실행된 쿼리 결과를 전부 가져오기
    
    def fetchone(self):
        return self.cursor.fetchone() # 결과에서 한 행만 가져오기
    
    def commit(self):
        if self.conn:
            self.conn.commit()
    
    def query_to_dataframe(self, query, params=None):
        """쿼리 결과를 Pandas DataFrame으로 반환"""
        self.execute(query, params)
        columns = [desc[0] for desc in self.cursor.description]
        data = self.fetchall()
        return pd.DataFrame(data, columns=columns)

# 일반 함수 (클래스에 속한 메소드 아님)
def create_tables(db):
    '''쇼핑몰 데이터베이스 테이블 생성'''

    # 기존 테이블 삭제 (초기화)
    tables = ['order_details', 'orders', 'customers', 'products']
    for table in tables:
        db.execute(f"DROP TABLE IF EXISTS {table}")

    print(" 기존 테이블 삭제 완료\n")

    # 1. customers 테이블
    db.execute("""
        CREATE TABLE customers (
            customer_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            grade VARCHAR(20) DEFAULT 'Bronze',
            point INT DEFAULT 0,
            join_date DATE NOT NULL
        )
    """)
    print(" customers 테이블 생성")

    # 2. products 테이블
    db.execute("""
        CREATE TABLE products (
            product_id INT AUTO_INCREMENT PRIMARY KEY,
            product_name VARCHAR(200) NOT NULL,
            category VARCHAR(50) NOT NULL,
            price INT NOT NULL,
            stock INT DEFAULT 0
        )
    """)
    print(" products 테이블 생성")

    # 3. orders 테이블
    db.execute("""
        CREATE TABLE orders (
            order_id INT AUTO_INCREMENT PRIMARY KEY,
            customer_id INT NOT NULL,
            order_date DATETIME NOT NULL,
            total_amount INT NOT NULL,
            status VARCHAR(20) DEFAULT 'Pending',
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        )
    """)
    print(" orders 테이블 생성")

    # 4. order_details 테이블
    db.execute("""
        CREATE TABLE order_details (
            detail_id INT AUTO_INCREMENT PRIMARY KEY,
            order_id INT NOT NULL,
            product_id INT NOT NULL,
            quantity INT NOT NULL,
            unit_price INT NOT NULL,
            subtotal INT NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders(order_id),
            FOREIGN KEY (product_id) REFERENCES products(product_id)
        )
    """)
    print(" order_details 테이블 생성")

    db.commit()

def insert_sample_data(db):
    '''샘플 데이터 삽입'''

    # 고객 데이터
    customers_data = [
        ('김철수', 'kim@email.com', 'Gold', 5000, '2023-01-15'),
        ('이영희', 'lee@email.com', 'Silver', 3000, '2023-03-20'),
        ('박민수', 'park@email.com', 'Bronze', 1000, '2023-06-10'),
        ('최지은', 'choi@email.com', 'Gold', 6000, '2023-02-05'),
        ('정수진', 'jung@email.com', 'Silver', 2500, '2023-04-18'),
        ('강동원', 'kang@email.com', 'Bronze', 500, '2024-01-20'),
        ('윤서연', 'yoon@email.com', 'Silver', 3500, '2023-05-12'),
        ('임하늘', 'lim@email.com', 'Bronze', 800, '2024-02-01'),
        ('송민호', 'song@email.com', 'Gold', 7000, '2023-01-28'),
        ('한지민', 'han@email.com', 'Bronze', 1200, '2023-07-15'),
    ]

    for customer in customers_data:
        db.execute(
            "INSERT INTO customers (name, email, grade, point, join_date) VALUES (%s, %s, %s, %s, %s)",
            customer
        )

    print(f" 고객 {len(customers_data)}명 삽입 완료")
    db.commit()

    # 상품 데이터
    products_data = [
        ('노트북', '전자기기', 1200000, 15),
        ('무선마우스', '전자기기', 35000, 50),
        ('키보드', '전자기기', 89000, 30),
        ('모니터', '전자기기', 350000, 20),
        ('청바지', '의류', 59000, 100),
        ('티셔츠', '의류', 25000, 150),
        ('운동화', '의류', 89000, 80),
        ('백팩', '가방', 45000, 40),
        ('텀블러', '생활용품', 15000, 200),
        ('책상스탠드', '생활용품', 28000, 60),
    ]

    for product in products_data:
        db.execute(
            "INSERT INTO products (product_name, category, price, stock) VALUES (%s, %s, %s, %s)",
            product
        )

    print(f" 상품 {len(products_data)}개 삽입 완료")
    db.commit() 

    # 주문 데이터
    orders_data = [
        (1, '2024-02-15 10:30:00', 1235000, 'Completed'),
        (1, '2024-02-20 14:20:00', 89000, 'Completed'),
        (2, '2024-02-16 09:15:00', 375000, 'Completed'),
        (3, '2024-02-17 16:45:00', 143000, 'Completed'),
        (4, '2024-02-18 11:00:00', 1550000, 'Completed'),
        (5, '2024-02-19 13:30:00', 84000, 'Completed'),
        (6, '2024-02-21 10:00:00', 59000, 'Pending'),
        (7, '2024-02-22 15:20:00', 254000, 'Completed'),
        (8, '2024-02-23 12:10:00', 45000, 'Cancelled'),
        (9, '2024-02-24 14:50:00', 1289000, 'Completed'),
    ]

    for order in orders_data:
        db.execute(
            "INSERT INTO orders (customer_id, order_date, total_amount, status) VALUES (%s, %s, %s, %s)",
            order
        )

    print(f" 주문 {len(orders_data)}건 삽입 완료")
    db.commit()
    
    # 주문 상세 데이터
    order_details_data = [
        (1, 1, 1, 1200000, 1200000),
        (1, 2, 1, 35000, 35000),
        (2, 3, 1, 89000, 89000),
        (3, 4, 1, 350000, 350000),
        (3, 5, 1, 25000, 25000),
        (4, 5, 2, 59000, 118000),
        (4, 6, 1, 25000, 25000),
        (5, 1, 1, 1200000, 1200000),
        (5, 4, 1, 350000, 350000),
        (6, 7, 1, 89000, 89000),
        (7, 5, 1, 59000, 59000),
        (8, 2, 3, 35000, 105000),
        (8, 3, 1, 89000, 89000),
        (8, 9, 2, 15000, 30000),
        (8, 10, 1, 28000, 28000),
        (9, 8, 1, 45000, 45000),
        (10, 1, 1, 1200000, 1200000),
        (10, 3, 1, 89000, 89000),
    ]

    for detail in order_details_data:
        db.execute(
            "INSERT INTO order_details (order_id, product_id, quantity, unit_price, subtotal) VALUES (%s, %s, %s, %s, %s)",
            detail
        )

    print(f" 주문 상세 {len(order_details_data)}건 삽입 완료")
    db.commit()

    print("\n 모든 샘플 데이터 삽입 완료!")