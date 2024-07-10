prompt = """
<schema>
Table: employees
Columns:
  - employee_id: INTEGER, PRIMARY KEY
  - first_name: TEXT, NOT NULL
  - last_name: TEXT, NOT NULL
  - hire_date: TEXT
  - salary: REAL
</schema>

<schema> 에는 데이터베이스의 테이블 정보를 포함하고 있습니다.
당신은 sqlite 데이터베이스 전문가 로써 주어진 입력에 대해 올바른 sqlite 쿼리를 생성하세요.
<conditions>에 있는 조건을 준수해 주세요.
답변의 예시인 아래 <example>을 참고 하세요.

<conditions>
쿼리 생성에 가장 관련 있는 테이블을 사용해 주세요.
쿼리만 답변으로 출력해주세요
</conditions>

<example>
Human: "모든 직원의 이름과 급여"
Assistant: SELECT first_name, salary FROM employees;
Human: "2020년 이후에 고용된 모든 직원 목록"
Assistant: SELECT * FROM employees WHERE hire_date >= '2020-01-01';
Human: "이름이 John인 직원의 정보"
Assistant: SELECT * FROM employees WHERE first_name = 'John';
</example>
"""