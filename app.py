from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

conversations = {}

SYSTEM_PROMPT = """
너의 이름은 챗미나이야.

사용자와 자연스럽게 대화하는 AI야.

규칙:
- 질문의 내용을 정확하게 이해하고 답해.
- 한국어 질문에는 자연스러운 한국어로 답해.
- 영어 질문에는 영어로 답해.
- 수학, 과학, 역사, 코딩, 글쓰기 등 다양한 주제에 답해.
- 이전 대화 내용을 참고해서 대화의 맥락을 유지해.
- 모르는 내용은 모른다고 말해.
- 필요한 경우 단계별로 설명해.
- 이모지와 이모티콘은 사용하지 마.
- 사용자가 요청하지 않으면 지나치게 길게 답하지 마.
"""


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    message = data.get("message", "").strip()
    conversation_id = data.get("conversation_id", "default")

    if not message:
        return jsonify({
            "answer": "질문을 입력해주세요."
        })

    if conversation_id not in conversations:
        conversations[conversation_id] = []

    conversations[conversation_id].append({
        "role": "user",
        "content": message
    })

    try:

        response = client.responses.create(
            model="gpt-5.6-luna",
            instructions=SYSTEM_PROMPT,
            input=conversations[conversation_id]
        )

        answer = response.output_text

        conversations[conversation_id].append({
            "role": "assistant",
            "content": answer
        })

        return jsonify({
            "answer": answer
        })

    except Exception as e:

        print("ERROR:", e)

        return jsonify({
            "answer": "AI 연결 중 오류가 발생했습니다."
        }), 500


@app.route("/clear", methods=["POST"])
def clear():

    data = request.get_json()

    conversation_id = data.get(
        "conversation_id",
        "default"
    )

    conversations.pop(
        conversation_id,
        None
    )

    return jsonify({
        "success": True
    })


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=int(
            os.environ.get(
                "PORT",
                5000
            )
        )
    )
@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    message = data.get("message", "").strip()
    conversation_id = data.get("conversation_id", "default")

    if not message:
        return jsonify({
            "answer": "질문을 입력해주세요."
        })

    # 해당 사용자의 대화 기록이 없으면 생성
    if conversation_id not in conversations:
        conversations[conversation_id] = []

    # 사용자 메시지 저장
    conversations[conversation_id].append({
        "role": "user",
        "content": message
    })

    try:

        response = client.responses.create(
            model="gpt-5.6-luna",

            instructions=SYSTEM_PROMPT,

            input=conversations[conversation_id]
        )

        answer = response.output_text

        # AI 답변 저장
        conversations[conversation_id].append({
            "role": "assistant",
            "content": answer
        })

        return jsonify({
            "answer": answer
        })

    except Exception as e:

        print("ERROR:", e)

        return jsonify({
            "answer": "AI와 연결하는 과정에서 문제가 발생했습니다."
        }), 500


@app.route("/clear", methods=["POST"])
def clear():

    data = request.get_json()
    conversation_id = data.get("conversation_id", "default")

    conversations.pop(conversation_id, None)

    return jsonify({
        "success": True
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    message = data.get("message", "").strip()
    conversation_id = data.get("conversation_id", "default")

    if not message:
        return jsonify({
            "answer": "질문을 입력해주세요."
        })

    # 해당 사용자의 대화 기록이 없으면 생성
    if conversation_id not in conversations:
        conversations[conversation_id] = []

    # 사용자 메시지 저장
    conversations[conversation_id].append({
        "role": "user",
        "content": message
    })

    try:

        response = client.responses.create(
            model="gpt-5.6-luna",

            instructions=SYSTEM_PROMPT,

            input=conversations[conversation_id]
        )

        answer = response.output_text

        # AI 답변 저장
        conversations[conversation_id].append({
            "role": "assistant",
            "content": answer
        })

        return jsonify({
            "answer": answer
        })

    except Exception as e:

        print("ERROR:", e)

        return jsonify({
            "answer": "AI와 연결하는 과정에서 문제가 발생했습니다."
        }), 500


@app.route("/clear", methods=["POST"])
def clear():

    data = request.get_json()
    conversation_id = data.get("conversation_id", "default")

    conversations.pop(conversation_id, None)

    return jsonify({
        "success": True
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )            ]
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
