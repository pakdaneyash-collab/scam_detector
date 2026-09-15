# 🛡️ ScamShield AI — Scam & Fraud Message Detector

A Python + Flask web application that uses **AI and NLP techniques** to detect scam and fraud messages (SMS, WhatsApp, Email) in real time.

---

## 📁 Project Structure

```
scam_detector/
├── app.py              → Flask web server (main entry point)
├── detector.py         → AI/ML detection engine
├── requirements.txt    → Python dependencies
├── data/
│   ├── __init__.py
│   └── patterns.py     → Scam keyword patterns & training data
├── templates/
│   ├── index.html      → Home page (input form)
│   ├── result.html     → AI analysis result page
│   └── examples.html   → Pre-built example scam messages
└── static/
    ├── css/
    │   └── style.css   → All page styling
    └── js/
        └── main.js     → Frontend JavaScript
```

---

## 🤖 AI Concepts Used

| Concept | Description |
|---|---|
| **Natural Language Processing (NLP)** | Text normalization, tokenization |
| **Rule-Based Classification** | Weighted keyword pattern matching |
| **Feature Extraction** | URL detection, urgency signal analysis |
| **Weighted Scoring Model** | HIGH=3pts, MEDIUM=2pts, LOW=1pt |
| **Multi-Class Text Classification** | Identifies scam type (Phishing, Lottery, etc.) |
| **Sigmoid Confidence Scoring** | Converts score → 0–100% probability |
| **Explainable AI (XAI)** | Human-readable reason for every decision |

---

## 🚀 How to Run

### 1. Install dependencies
```bash
cd scam_detector
pip install -r requirements.txt
```

### 2. Start the server
```bash
python app.py
```

### 3. Open in browser
```
http://127.0.0.1:5000
```

---

## 📡 API Endpoint

You can also call the detector programmatically:

```bash
curl -X POST http://127.0.0.1:5000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"message": "Congratulations! You have won a prize. Click here now!", "message_type": "sms"}'
```

---

## 🔍 Risk Levels

| Level | Score Range | Meaning |
|---|---|---|
| ✅ SAFE | 0–2 | No significant scam indicators |
| ⚠️ LOW | 3–5 | Minor suspicious patterns |
| 🔶 MEDIUM | 6–10 | Likely spam or suspicious |
| 🚨 HIGH | 11–20 | Strong scam indicators |
| ☠️ CRITICAL | 21+ | Almost certainly a scam |

---

## ⚠️ Disclaimer

This tool is built for **educational purposes** to demonstrate how AI/NLP can be used to detect scam messages. It does not replace professional cybersecurity tools.
