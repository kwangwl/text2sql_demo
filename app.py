import streamlit as st
from modules.bedrock import get_model_response
from modules.database import get_db_connection, query_sqlite, get_table_metadata
from resources.prompt import prompt

# config
MODEL_ID_INFO = {
    "Sonnet": "anthropic.claude-3-sonnet-20240229-v1:0",
    "Haiku": "anthropic.claude-3-haiku-20240307-v1:0"
}


# SQL 생성 함수 (여기서는 간단한 예시로 더미 함수 사용)
def generate_sql_from_text(parameter, user_query):
    # 실제로는 자연어를 SQL로 변환하는 로직 필요
    final_prompt = f"{prompt}\n\nHuman:{user_query}"
    return get_model_response(parameter, final_prompt)


# streamlit 앱
st.set_page_config(page_title="text2sql demo", layout='wide')
st.title("Text2SQL 데모 with SQLite")

with st.expander("Database 관계도"):
    st.image("resources/db_schema.png")

with st.expander("Query 예시"):
    st.text("모든 직원의 이름과 급여\n모든 프로젝트의 이름과 시작일\nJohn Doe가 속한 프로젝트와 그의 역할")
st.header("자연어 쿼리 입력")
user_query = st.text_input("쿼리:")

# bedrock setting
st.sidebar.subheader("Claude Setting")
model_name = st.sidebar.selectbox("Select Model (Claude 3)", list(MODEL_ID_INFO.keys()))
max_token = st.sidebar.number_input(label="Max Token", min_value=0, step=1, max_value=4096, value=2048)
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.3)
top_p = st.sidebar.number_input(label="Top P", min_value=0.000, step=0.001, max_value=1.000, value=0.999, format="%f")


if st.button("SQL 생성 및 데이터 쿼리"):
    parameter = {
        "anthropic_version": "bedrock-2023-05-31",
        "model_id": MODEL_ID_INFO[model_name],
        "max_tokens": max_token,
        "temperature": temperature,
        "top_p": top_p,
    }
    generated_sql = generate_sql_from_text(parameter, user_query)

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
