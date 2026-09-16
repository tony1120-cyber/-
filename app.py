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
한국어 질문에는 한국어로 답해.
영어 질문에는 영어로 답해.
수학, 과학, 역사, 코딩, 글쓰기 등 다양한 질문에 답해.
이전 대화의 내용을 참고해서 대화의 흐름을 유지해.
모르는 내용은 아는 척하지 마.
이모지와 이모티콘은 사용하지 마.
쉽고 정확하게 설명해.
"""

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    message = data.get("message", "")
    history = data.get("history", [])

    if not message:
        return jsonify({
            "answer": "질문을 입력해주세요."
        })

    try:

        input_messages = []

        for item in history:

            if item.get("role") == "user":
                input_messages.append({
                    "role": "user",
                    "content": item.get("content", "")
                })

            elif item.get("role") == "assistant":
                input_messages.append({
                    "role": "assistant",
                    "content": item.get("content", "")
                })

        input_messages.append({
            "role": "user",
            "content": message
        })

        response = client.responses.create(
            model="gpt-5.6-luna",
            instructions=SYSTEM_PROMPT,
            input=input_messages
        )

        return jsonify({
            "answer": response.output_text
        })

    except Exception as error:

        print(error)

        return jsonify({
            "answer": "AI 연결에 문제가 발생했습니다."
        })


@app.route("/health")
def health():

    return "ChatMinAI is running"


if __name__ == "__main__":

    port = int(os.environ.get("PORT", "5000"))

    app.run(
        host="0.0.0.0",
        port=port
    )
@app.route("/")
def index():
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

        messages.append({
            "role": "developer",
            "content": SYSTEM_MESSAGE
        })


        for item in history:

            role = item.get("role")
            content = item.get("content")

            if role in ["user", "assistant"] and content:

                messages.append({
                    "role": role,
                    "content": content
                })


        messages.append({
            "role": "user",
            "content": message
        })


        response = client.responses.create(

            model="gpt-5.6-luna",

            input=messages

        )


        answer = response.output_text


        return jsonify({
            "answer": answer
        })


    except Exception as error:

        print("ERROR:", error)

        return jsonify({
            "answer": "AI 연결에 문제가 발생했습니다. Render의 로그를 확인해주세요."
        }), 500


@app.route("/health")
def health():

    return jsonify({
        "status": "ok"
    })


if __name__ == "__main__":

    port = int(
        os.environ.get(
            "PORT",
            5000
        )
    )

    app.run(
        host="0.0.0.0",
        port=port
    )def chat():

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
