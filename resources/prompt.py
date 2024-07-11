prompt = """
<schema>
Table: Departments
Columns:
- department_id: INTEGER, PRIMARY KEY
- department_name: TEXT, NOT NULL

Table: employees
Columns:
  - employee_id: INTEGER, PRIMARY KEY
  - first_name: TEXT, NOT NULL
  - last_name: TEXT, NOT NULL
  - hire_date: TEXT
  - salary: REAL
  
Table: Projects
Columns:
- project_id: INTEGER, PRIMARY_KEY
- project_name: TEXT, NOT NULL
- start_date: TEXT
- end_date: TEXT

Table: EmployeeProjects
Columns:
- employee_id: INTEGER, FOREIGN KEY (employee_id) REFERENCES Employees(employee_id)
- project_id: INTEGER, FOREIGN KEY (project_id) REFERENCES Projects(project_id)
- role: TEXT
- PRIMARY KEY: (employee_id, project_id)
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
Assistant: SELECT first_name, last_name, salary FROM Employees;
Human: "2020년 이후에 고용된 모든 직원 목록"
Assistant: SELECT * FROM Employees WHERE hire_date >= '2020-01-01';
Human: "모든 부서의 이름과 ID"
Assistant: SELECT department_id, department_name FROM Departments;
Human: "모든 프로젝트의 이름과 시작일"
Assistant: SELECT project_name, start_date FROM Projects;
Human: "John Doe가 속한 프로젝트와 그의 역할"
Assistant: SELECT Projects.project_name, EmployeeProjects.role FROM Employees JOIN EmployeeProjects ON Employees.employee_id = EmployeeProjects.employee_id JOIN Projects ON EmployeeProjects.project_id = Projects.project_id WHERE Employees.first_name = 'John' AND Employees.last_name = 'Doe';
Human: "Finance 부서의 모든 직원 이름"
Assistant: SELECT Employees.first_name, Employees.last_name FROM Employees JOIN Departments ON Employees.department_id = Departments.department_id WHERE Departments.department_name = 'Finance';
</example>
"""