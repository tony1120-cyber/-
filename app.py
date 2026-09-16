from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "").strip()

    if not message:
        return jsonify({"answer": "메시지를 입력해주세요."})

    try:
        response = client.responses.create(
            model="gpt-5.6-mini",
            input=[
                {
                    "role": "system",
                    "content": "너는 친절한 AI 챗봇 챗미나이야. 한국어로 이해하기 쉽게 답해줘."
                },
                {
                    "role": "user",
                    "content": message
                }
            ]
        )

        return jsonify({
            "answer": response.output_text
        })

    except Exception as e:
        print(e)
        return jsonify({
            "answer": "AI 연결에 문제가 발생했습니다."
        }), 500


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
