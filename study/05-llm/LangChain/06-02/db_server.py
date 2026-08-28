import sqlite3
import json
import random
from fastmcp import FastMCP

mcp = FastMCP(name='DbServer')
DB_FILE = r"C:\skn29\LangChain\06-02\database.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS emp (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            name       TEXT NOT NULL,
            department TEXT,
            position   TEXT,
            salary     INTEGER,
            age        INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def insert_emp(name, department, position, salary, age):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO emp (name, department, position, salary, age) VALUES (?, ?, ?, ?, ?)",
        (name, department, position, salary, age)
    )
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return new_id

@mcp.tool()
def insert_dummy_data(count: int = 100) -> str:
    """가상의 직원 데이터를 count건 삽입합니다."""
    names = [
        "김민준", "이서연", "박도윤", "최지우", "정하준",
        "강서현", "조민서", "윤예준", "장수아", "임현우",
        "오지민", "한예린", "신동혁", "권나은", "황태양",
        "송지호", "안서윤", "유준혁", "남지아", "백찬우"
    ]
    departments = ["개발팀", "마케팅팀", "영업팀", "인사팀", "기획팀", "디자인팀", "운영팀"]
    positions = ["사원", "주임", "대리", "과장", "차장", "부장"]
    salary_range = {
        "사원": (2800, 3500), "주임": (3200, 4000), "대리": (3800, 4800),
        "과장": (4500, 6000), "차장": (5500, 7000), "부장": (6500, 9000)
    }
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    for _ in range(count):
        name       = random.choice(names) + str(random.randint(1, 999))
        department = random.choice(departments)
        position   = random.choice(positions)
        salary     = random.randint(*salary_range[position]) * 1000
        age        = random.randint(24, 58)
        cursor.execute(
            "INSERT INTO emp (name, department, position, salary, age) VALUES (?, ?, ?, ?, ?)",
            (name, department, position, salary, age)
        )
    conn.commit()
    conn.close()
    return f"가상 데이터 {count}건 삽입 완료"

@mcp.tool()                          # ← 괄호 추가
def get_database_schema() -> str:    # ← 오타 수정 shema → schema
    """데이터베이스의 테이블 스키마를 반환합니다."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT sql FROM sqlite_master WHERE type='table';")
    schemas = [row[0] for row in cursor.fetchall() if row[0]]
    conn.close()
    return "\n\n".join(schemas)

@mcp.tool()
def get_all_employees(department: str = "", position: str = "") -> str:
    """emp 테이블의 직원 목록을 조회합니다."""
    try:
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        conditions, params = [], []
        if department:
            conditions.append("department = ?")
            params.append(department)
        if position:
            conditions.append("position = ?")
            params.append(position)
        where = ("WHERE " + " AND ".join(conditions)) if conditions else ""
        cursor.execute(f"SELECT * FROM emp {where} ORDER BY id", params)
        rows = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return json.dumps({"count": len(rows), "employees": rows}, ensure_ascii=False, indent=2)
    except sqlite3.Error as e:
        return json.dumps({"error": str(e)}, ensure_ascii=False)

@mcp.tool()
def get_employee_by_id(emp_id: int) -> str:
    """ID로 특정 직원 한 명을 조회합니다."""
    try:
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM emp WHERE id = ?", (emp_id,))
        row = cursor.fetchone()
        conn.close()
        if row is None:
            return json.dumps({"error": f"id={emp_id} 직원을 찾을 수 없습니다."}, ensure_ascii=False)
        return json.dumps(dict(row), ensure_ascii=False, indent=2)
    except sqlite3.Error as e:
        return json.dumps({"error": str(e)}, ensure_ascii=False)

@mcp.tool()
def get_employees_stats() -> str:
    """부서별 직원 수, 평균 급여, 최고/최저 급여 통계를 반환합니다."""
    try:
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("""
            SELECT
                department,
                COUNT(*)           AS 직원수,
                ROUND(AVG(salary)) AS 평균급여,
                MAX(salary)        AS 최고급여,
                MIN(salary)        AS 최저급여
            FROM emp
            GROUP BY department
            ORDER BY 직원수 DESC
        """)
        rows = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return json.dumps({"department_stats": rows}, ensure_ascii=False, indent=2)
    except sqlite3.Error as e:
        return json.dumps({"error": str(e)}, ensure_ascii=False)

@mcp.tool()
def execute_sql_query(query: str) -> str:
    """SELECT 쿼리만 실행하고 결과를 JSON으로 반환합니다."""
    if not query.strip().upper().startswith("SELECT"):
        return json.dumps({"error": "SELECT 쿼리만 허용됩니다."}, ensure_ascii=False)
    try:
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(query)
        rows = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return json.dumps(rows, ensure_ascii=False, indent=2)
    except sqlite3.Error as e:
        return json.dumps({"error": str(e)}, ensure_ascii=False)

if __name__ == '__main__':
    init_db()
    # 데이터가 없을 때만 삽입 (중복 방지)
    conn = sqlite3.connect(DB_FILE)
    count = conn.execute("SELECT COUNT(*) FROM emp").fetchone()[0]
    conn.close()
    if count == 0:                  # ← 핵심: 최초 1회만 삽입
        insert_dummy_data(100)
    mcp.run(transport='stdio')