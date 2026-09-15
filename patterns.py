"""
patterns.py
-----------
Training data and keyword patterns used by the AI detection engine.
AI Concept Used: Rule-Based NLP + Weighted Feature Extraction
"""

# -------------------------------------------------------------------
# HIGH-RISK scam keyword patterns (weight: 3 points each)
# -------------------------------------------------------------------
HIGH_RISK_KEYWORDS = [
    "you have won",
    "congratulations you are selected",
    "claim your prize",
    "click here to claim",
    "your account has been suspended",
    "verify your account immediately",
    "urgent action required",
    "your bank account is at risk",
    "otp",
    "send your otp",
    "wire transfer",
    "western union",
    "gift card",
    "send gift card",
    "bitcoin transfer",
    "cryptocurrency reward",
    "lottery winner",
    "you have been chosen",
    "free iphone",
    "free gift",
    "act now",
    "limited time offer",
    "your package is held",
    "pay customs fee",
    "nigerian prince",
    "inheritance fund",
    "million rupees",
    "double your money",
    "investment opportunity guaranteed",
    "risk free",
    "100% profit",
    "your paypal is limited",
    "unusual sign in activity",
    "reset your password immediately",
    "confirm your details",
    "social security number",
    "it refund",
    "tax refund pending",
    "microsoft support",
    "apple id suspended",
]

# -------------------------------------------------------------------
# MEDIUM-RISK scam keyword patterns (weight: 2 points each)
# -------------------------------------------------------------------
MEDIUM_RISK_KEYWORDS = [
    "click the link below",
    "verify your identity",
    "update your information",
    "account will be closed",
    "login immediately",
    "do not ignore",
    "final warning",
    "suspicious activity detected",
    "security alert",
    "your order has been placed",
    "unexpected charge",
    "refund approved",
    "you owe",
    "debt collection",
    "prize money",
    "free money",
    "earn from home",
    "work from home earn",
    "make money fast",
    "easy cash",
    "no experience needed",
    "job offer",
    "part time job",
    "be your own boss",
    "click here",
    "follow this link",
    "visit this website",
]

# -------------------------------------------------------------------
# LOW-RISK suspicious patterns (weight: 1 point each)
# -------------------------------------------------------------------
LOW_RISK_KEYWORDS = [
    "dear customer",
    "dear user",
    "dear winner",
    "dear friend",
    "hello friend",
    "as soon as possible",
    "asap",
    "do not share",
    "confidential",
    "private offer",
    "exclusive deal",
    "special promotion",
    "you qualify",
    "selected randomly",
    "limited slots",
    "respond within 24 hours",
    "respond within 48 hours",
    "call us now",
    "contact us immediately",
    "toll free",
]

# -------------------------------------------------------------------
# Suspicious URL patterns
# -------------------------------------------------------------------
SUSPICIOUS_URL_PATTERNS = [
    r"bit\.ly",
    r"tinyurl\.com",
    r"goo\.gl",
    r"ow\.ly",
    r"t\.co",
    r"cutt\.ly",
    r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",  # Raw IP address
    r"\.xyz",
    r"\.tk",
    r"\.ml",
    r"\.ga",
    r"\.cf",
    r"free.*\.(com|net|org)",
    r"win.*\.(com|net|org)",
    r"prize.*\.(com|net|org)",
    r"reward.*\.(com|net|org)",
]

# -------------------------------------------------------------------
# Scam category mapping: keywords → category label
# -------------------------------------------------------------------
SCAM_CATEGORIES = {
    "Phishing": [
        "verify your account", "account suspended", "login immediately",
        "confirm your details", "update your information", "otp",
        "reset your password", "apple id suspended", "paypal is limited",
        "microsoft support", "unusual sign in",
    ],
    "Lottery / Prize Fraud": [
        "you have won", "lottery winner", "claim your prize",
        "congratulations you are selected", "you have been chosen",
        "free iphone", "prize money",
    ],
    "Financial Fraud": [
        "wire transfer", "western union", "bitcoin transfer",
        "cryptocurrency reward", "inheritance fund", "nigerian prince",
        "million rupees", "double your money", "investment opportunity",
        "100% profit", "it refund", "tax refund", "gift card",
    ],
    "Job Scam": [
        "work from home earn", "earn from home", "make money fast",
        "easy cash", "no experience needed", "job offer",
        "part time job", "be your own boss",
    ],
    "Package / Delivery Scam": [
        "your package is held", "pay customs fee", "your order has been placed",
        "unexpected charge", "refund approved",
    ],
    "Debt / Legal Threat": [
        "you owe", "debt collection", "final warning",
        "urgent action required", "social security number",
    ],
}

# -------------------------------------------------------------------
# Risk level thresholds (based on cumulative score)
# -------------------------------------------------------------------
RISK_THRESHOLDS = {
    "SAFE":     (0, 2),
    "LOW":      (3, 5),
    "MEDIUM":   (6, 10),
    "HIGH":     (11, 20),
    "CRITICAL": (21, 9999),
}

# Risk level colors (for UI)
RISK_COLORS = {
    "SAFE":     "#27ae60",
    "LOW":      "#f39c12",
    "MEDIUM":   "#e67e22",
    "HIGH":     "#e74c3c",
    "CRITICAL": "#8e44ad",
}

# Risk level icons
RISK_ICONS = {
    "SAFE":     "✅",
    "LOW":      "⚠️",
    "MEDIUM":   "🔶",
    "HIGH":     "🚨",
    "CRITICAL": "☠️",
}
