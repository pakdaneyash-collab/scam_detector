"""
app.py
------
Flask Web Application — Scam & Fraud Message Detector
Entry point for the web server.

AI Concept: Serves the AI detection engine via a web interface.
"""

from flask import Flask, render_template, request, jsonify
from detector import analyze

app = Flask(__name__)


# ===========================================================================
# ROUTES
# ===========================================================================

@app.route("/", methods=["GET"])
def index():
    """
    Home page — shows the message input form.
    """
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze_message():
    """
    POST /analyze
    Accepts form data: message (str), message_type (sms | email)
    Returns the result.html page with full AI analysis.
    """
    message = request.form.get("message", "").strip()
    message_type = request.form.get("message_type", "message")

    if not message:
        return render_template(
            "index.html",
            error="Please enter a message or email to analyze."
        )

    result = analyze(message, message_type)
    return render_template("result.html", result=result, original_message=message)


@app.route("/api/analyze", methods=["POST"])
def api_analyze():
    """
    POST /api/analyze
    JSON API endpoint for programmatic access.

    Request body:
        { "message": "...", "message_type": "sms" | "email" }

    Response:
        Full analysis JSON object
    """
    data = request.get_json(force=True)
    message = data.get("message", "").strip()
    message_type = data.get("message_type", "message")

    if not message:
        return jsonify({"error": "message field is required"}), 400

    result = analyze(message, message_type)
    return jsonify(result)


@app.route("/examples")
def examples():
    """
    Shows pre-built example scam messages for demonstration.
    """
    sample_scams = [
        {
            "title": "Lottery Scam",
            "type": "message",
            "message": "Congratulations! You have won ₹10,00,000 in the national lottery. "
                       "Click here to claim your prize: http://bit.ly/win-prize. "
                       "Act NOW! Limited time offer!!!",
        },
        {
            "title": "Phishing Message",
            "type": "message",
            "message": "Dear Customer, Your SBI account is limited. "
                       "Unusual sign in activity detected. Verify your account immediately "
                       "or your account will be closed. Click the link below: "
                       "http://192.168.1.100/sbi-verify. DO NOT IGNORE THIS MESSAGE.",
        },
        {
            "title": "Job Scam",
            "type": "message",
            "message": "Hi! Earn from home ₹5,000/day. No experience needed. "
                       "Part time job available. Be your own boss. Make money fast. "
                       "Easy cash. Respond within 24 hours! Call us now: +91-9800-FREE-CASH",
        },
        {
            "title": "Bank Phishing",
            "type": "message",
            "message": "URGENT: Your bank account is at risk. Suspicious activity detected. "
                       "Reset your password immediately and confirm your details. "
                       "Send your OTP to verify. Final warning — urgent action required!!!",
        },
        {
            "title": "Safe Message",
            "type": "message",
            "message": "Hey, are you free for lunch tomorrow? I was thinking of trying "
                       "that new Italian restaurant downtown. Let me know!",
        },
    ]
    return render_template("examples.html", samples=sample_scams)


# ===========================================================================
# RUN
# ===========================================================================

if __name__ == "__main__":
    print("=" * 55)
    print("  🛡️  AI Scam & Fraud Detector — Starting Server")
    print("  📡  Open: http://127.0.0.1:5000")
    print("=" * 55)
    app.run(debug=True, host="0.0.0.0", port=5000)
