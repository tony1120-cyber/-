import os

from flask import Flask, render_template, request, jsonify
from openai import OpenAI


app = Flask(__name__)


client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)


SYSTEM_PROMPT = """
너의 이름은 챗미나이야.

사용자와 자연스럽게 대화하는 AI야.

사용자의 질문을 이해하고 최대한 정확하게 답해.

한국어 질문에는 한국어로 답해.
영어 질문에는 영어로 답해.

수학, 과학, 역사, 코딩, 게임, 글쓰기 등
다양한 주제의 질문에 답해.

이전 대화 내용을 참고해서 대화의 흐름을 유지해.

모르는 내용은 아는 척하지 마.

필요하면 예시와 단계별 설명을 사용해.

이모지와 이모티콘은 사용하지 마.

사용자가 요청하지 않는 이상 너무 길게 답하지 마.
"""


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    try:

        data = request.get_json()

        message = data.get("message", "")
        history = data.get("history", [])


        if not message:

            return jsonify({
                "answer": "질문을 입력해주세요."
            })


        messages = []


        for item in history:

            role = item.get("role")
            content = item.get("content", "")


            if role == "user":

                messages.append({
                    "role": "user",
                    "content": content
                })


            elif role == "assistant":

                messages.append({
                    "role": "assistant",
                    "content": content
                })


        messages.append({
            "role": "user",
            "content": message
        })


        response = client.responses.create(

            model="gpt-5.6-luna",

            instructions=SYSTEM_PROMPT,

            input=messages

        )


        answer = response.output_text


        return jsonify({
            "answer": answer
        })


    except Exception as error:

        print("ERROR:", error)


        return jsonify({
            "answer": "AI 연결에 문제가 발생했습니다."
        }), 500


@app.route("/health")
def health():

    return "ChatMinAI OK"


if __name__ == "__main__":

    port = int(
        os.environ.get(
            "PORT",
            "5000"
        )
    )


    app.run(

        host="0.0.0.0",

        port=port

    )
