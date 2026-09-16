from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "")

    # 아직 AI 연결 전
    answer = f"챗미나이가 받은 메시지: {message}"

    return jsonify({
        "answer": answer
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
