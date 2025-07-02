# Import needed libraries
import gspread
import json
from datetime import datetime
from flask import Flask, request, jsonify
from openai import OpenAI
import os

# Create Flask web app
app = Flask(__name__)

# Connect to OpenAI using your secret API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Connect to Google Sheets using your service account
service_account_info = json.loads(os.getenv('GOOGLE_SHEETS_KEY'))
gc = gspread.service_account_from_dict(service_account_info)
sh = gc.open('AI Equity Engine Log')
worksheet = sh.sheet1

# Health check route: when you visit /ping, it replies status
@app.route("/ping")
def ping():
    return jsonify({"status": "running"})

# The /ask route: users POST questions here
@app.route("/ask", methods=["POST"])
def ask():
    # Check if request is JSON
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Malformed JSON"}), 400

    question = data.get("question")
    if not question or not isinstance(question, str) or len(question.strip()) == 0:
        return jsonify({"error": "Question must be a non-empty string"}), 400

    # Optional: Limit question length to avoid abuse or errors
    if len(question) > 500:
        return jsonify({"error": "Question too long (max 500 characters)"}), 400

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a kind tutor for middle school students."},
                {"role": "user", "content": question}
            ]
        )
        answer = response.choices[0].message.content

        timestamp = datetime.now().isoformat()
        subject = data.get("subject", "General")
        answer_length = len(answer.split())
        worksheet.append_row([timestamp, subject, question, answer, answer_length])

        return jsonify({"answer": answer})

    except Exception as e:
        # Log error to console (you can also log to a file or external system)
        print(f"Error in /ask: {e}")
        return jsonify({"error": "Internal server error, please try again later"}), 500


# Start the app on port 5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
