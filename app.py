from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("text", "")
    
    gemma_api_url = "http://127.0.0.1:1234/v1/chat/completions"
    
    payload = {
        "model": "gemma-3-4b-it",
        "messages": [
            {"role": "user", "content": user_input}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(gemma_api_url, json=payload, timeout=10)
        api_response = response.json()

        if api_response.get("choices") and len(api_response["choices"]) > 0:
            message = api_response["choices"][0]
            assistant_response = message.get("message", {}).get("content") or message.get("text", "")
        else:
            assistant_response = "Yanıt alınamadı."

        return jsonify({"response": assistant_response})

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
