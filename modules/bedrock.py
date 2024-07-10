import streamlit as st
import boto3
import os
import json


if os.path.exists(".streamlit"):
    # local
    session = boto3.Session(
        aws_access_key_id=st.secrets["ACCESS_KEY_ID"],
        aws_secret_access_key=st.secrets["SECRET_ACCESS_KEY"],
        region_name=st.secrets["REGION_NAME"],
    )
    bedrock_runtime = session.client('bedrock-runtime')
else:
    # claude9
    session = boto3.Session()
    bedrock_runtime = session.client('bedrock-runtime')


def get_model_response(parameter, prompt):
    body = json.dumps({
        "anthropic_version": parameter["anthropic_version"],
        "max_tokens": parameter["max_tokens"],
        "temperature": parameter["temperature"],
        "top_p": parameter["top_p"],
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }
        ],
    })


    response = bedrock_runtime.invoke_model(body=body, modelId=parameter["model_id"])
    response_body = json.loads(response.get('body').read())  # response 읽기
    result = response_body.get("content")[0].get("text")

    return result
