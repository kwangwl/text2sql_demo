import streamlit as st
import sqlite3
import pandas as pd
from modules.bedrock import get_model_response
from modules.database import get_db_connection, query_sqlite


# SQL 생성 함수 (여기서는 간단한 예시로 더미 함수 사용)
def generate_sql_from_text(parameter, user_query):
    # 실제로는 자연어를 SQL로 변환하는 로직 필요
    prompt = f"{user_query}"
    return get_model_response(parameter, prompt)


# SQLite 쿼리 실행 함수
def query_sqlite(query):
    conn = get_db_connection()
    result = conn.execute(query).fetchall()
    conn.close()
    return pd.DataFrame(result)


st.title("텍스트-투-SQL 데모 with SQLite")

conn = get_db_connection()

st.header("자연어 쿼리 입력")
user_query = st.text_input("쿼리:")

if st.button("SQL 생성 및 데이터 쿼리"):
    generated_sql = generate_sql_from_text(user_query)

    st.write("생성된 SQL:")
    st.code(generated_sql, language='sql')

    try:
        result = query_sqlite(generated_sql)
        st.write("쿼리 결과:")
        st.dataframe(result)
    except Exception as e:
        st.write("에러 발생:")
        st.error(str(e))
        # 오류 수정 로직 추가 가능
        corrected_sql = generated_sql.replace("employees", "corrected_employees")
        st.write("수정된 SQL:")
        st.code(corrected_sql, language='sql')
        result = query_sqlite(corrected_sql)
        st.write("수정된 쿼리 결과:")
        st.dataframe(result)