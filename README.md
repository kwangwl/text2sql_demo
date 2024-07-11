Text2SQL Demo

실습 환경조건
1. AWS Cloud9 (us-west-2 리전, bedrock claude3 지원 리전)
2. bedrock model access - claude3 sonnet, haiku

실습 환경설정
1. AWS Cloud9 IDE에서 bash terminal을 선택합니다.
2. 터미널에 다음을 붙여넣고 실행하여 git 코드를 다운로드 받습니다.
git clone https://github.com/kwangwl/text2sql_demo.git
3. 다음 명령어를 입력하여 폴더를 이동합니다.
cd text2sql_demo
4. 다음 명령어를 입력하여 실습에 필요한 종속성을 설치합니다.
pip install -r requirements.txt
5. 다음 명령어를 입력하여 application 을 실행합니다.
streamlit run app.py --server.port 8080
6. AWS Cloud9에서 Preview -> Preview Running Application을 선택합니다.
7. 어플리케이션이 실행된 웹페이지가 표시됩니다.


Ref
1. https://aws.amazon.com/blogs/machine-learning/build-a-robust-text-to-sql-solution-generating-complex-queries-self-correcting-and-querying-diverse-data-sources/
2. https://medium.com/pinterest-engineering/how-we-built-text-to-sql-at-pinterest-30bad30dabff
3. https://www.linkedin.com/pulse/text-sql-prompting-technique-enterprise-analytics-ritu-singhal-owjyc/