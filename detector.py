"""
detector.py
-----------
AI Detection Engine for Scam / Fraud Messages and Emails.

AI Concepts Used:
  1. Natural Language Processing (NLP)       - Text normalization, tokenization
  2. Rule-Based Classification               - Weighted keyword matching
  3. Feature Extraction                      - URL detection, urgency signals
  4. Scoring Model                           - Cumulative weighted risk scoring
  5. Multi-Class Text Classification         - Categorizing scam type
  6. Confidence Scoring                      - Percentage confidence of scam
"""

import re
import math
from data.patterns import (
    HIGH_RISK_KEYWORDS,
    MEDIUM_RISK_KEYWORDS,
    LOW_RISK_KEYWORDS,
    SUSPICIOUS_URL_PATTERNS,
    SCAM_CATEGORIES,
    RISK_THRESHOLDS,
    RISK_COLORS,
    RISK_ICONS,
)


# ===========================================================================
# NLP UTILITY FUNCTIONS
# ===========================================================================

def normalize_text(text: str) -> str:
    """
    NLP Step 1 — Text Normalization
    Converts text to lowercase and removes excess whitespace.
    This ensures consistent matching regardless of case or formatting.
    """
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    text = text.strip()
    return text


def tokenize(text: str) -> list:
    """
    NLP Step 2 — Tokenization
    Splits normalized text into individual word tokens.
    Used for bag-of-words style feature extraction.
    """
    tokens = re.findall(r"\b\w+\b", text)
    return tokens


def extract_urls(text: str) -> list:
    """
    Feature Extraction — URL Detection
    Finds all URLs in the message using regex.
    """
    url_pattern = r"(https?://[^\s]+|www\.[^\s]+)"
    return re.findall(url_pattern, text, re.IGNORECASE)


def detect_suspicious_urls(urls: list) -> list:
    """
    Feature Extraction — Suspicious URL Classifier
    Checks each URL against known suspicious patterns.
    """
    flagged = []
    for url in urls:
        for pattern in SUSPICIOUS_URL_PATTERNS:
            if re.search(pattern, url, re.IGNORECASE):
                flagged.append(url)
                break
    return list(set(flagged))


def count_exclamations_and_caps(text: str) -> dict:
    """
    Feature Extraction — Urgency Signal Detection
    Counts exclamation marks and ALL CAPS words.
    Scam messages often use these for psychological pressure.
    """
    exclamations = text.count("!")
    caps_words = len(re.findall(r"\b[A-Z]{3,}\b", text))
    return {"exclamations": exclamations, "caps_words": caps_words}


# ===========================================================================
# WEIGHTED KEYWORD MATCHING (Rule-Based NLP)
# ===========================================================================

def match_keywords(normalized_text: str) -> dict:
    """
    Rule-Based Classification — Weighted Keyword Matching
    Scans the normalized text for high, medium, and low-risk keywords.
    Assigns weighted scores to each match.

    Weights:
      HIGH   = 3 points per match
      MEDIUM = 2 points per match
      LOW    = 1 point per match
    """
    matched = {"high": [], "medium": [], "low": []}

    for kw in HIGH_RISK_KEYWORDS:
        if kw in normalized_text:
            matched["high"].append(kw)

    for kw in MEDIUM_RISK_KEYWORDS:
        if kw in normalized_text:
            matched["medium"].append(kw)

    for kw in LOW_RISK_KEYWORDS:
        if kw in normalized_text:
            matched["low"].append(kw)

    return matched


def calculate_keyword_score(matched: dict) -> int:
    """
    Scoring Model — Computes weighted score from matched keywords.
    """
    score = 0
    score += len(matched["high"]) * 3
    score += len(matched["medium"]) * 2
    score += len(matched["low"]) * 1
    return score


# ===========================================================================
# SCAM CATEGORY CLASSIFIER (Multi-Class Text Classification)
# ===========================================================================

def classify_scam_type(normalized_text: str) -> list:
    """
    Multi-Class Text Classification
    Identifies which scam categories are present in the message.
    Returns a list of detected scam types.
    """
    detected_categories = []
    for category, keywords in SCAM_CATEGORIES.items():
        for kw in keywords:
            if kw in normalized_text:
                detected_categories.append(category)
                break
    return detected_categories


# ===========================================================================
# RISK LEVEL RESOLVER
# ===========================================================================

def get_risk_level(score: int) -> str:
    """
    Resolves the risk level string based on cumulative score.
    """
    for level, (low, high) in RISK_THRESHOLDS.items():
        if low <= score <= high:
            return level
    return "SAFE"


# ===========================================================================
# CONFIDENCE SCORE (Probabilistic Estimation)
# ===========================================================================

def calculate_confidence(score: int, max_possible: int = 60) -> float:
    """
    Confidence Scoring — Sigmoid-based probability estimation.
    Uses a sigmoid function to convert raw score to 0–100% confidence.

    AI Concept: Logistic/Sigmoid Function used in Neural Networks
    for binary classification (Scam vs Not Scam).

    Formula: confidence = 1 / (1 + e^(-k * (score - midpoint)))
    """
    if score == 0:
        return 0.0
    k = 0.25          # steepness of sigmoid curve
    midpoint = 8      # score at which confidence = 50%
    confidence = 1 / (1 + math.exp(-k * (score - midpoint)))
    return round(confidence * 100, 2)


# ===========================================================================
# MAIN ANALYSIS FUNCTION
# ===========================================================================

def analyze(message: str, message_type: str = "message") -> dict:
    """
    Main AI analysis pipeline.
    
    Steps:
      1. Normalize text (NLP preprocessing)
      2. Extract features (URLs, urgency signals)
      3. Match keywords (Rule-Based NLP)
      4. Calculate score (Weighted Scoring Model)
      5. Classify scam type (Multi-Class Classification)
      6. Determine risk level (Threshold Classification)
      7. Calculate confidence (Sigmoid Confidence Score)
      8. Generate explanation (Explainable AI)

    Args:
        message      : Raw input message/email text
        message_type : "sms" or "email"

    Returns:
        dict with full analysis result
    """

    # --- Step 1: NLP Preprocessing ---
    normalized = normalize_text(message)
    tokens = tokenize(normalized)

    # --- Step 2: Feature Extraction ---
    urls = extract_urls(message)
    suspicious_urls = detect_suspicious_urls(urls)
    urgency = count_exclamations_and_caps(message)

    # --- Step 3: Keyword Matching ---
    matched_keywords = match_keywords(normalized)

    # --- Step 4: Scoring ---
    base_score = calculate_keyword_score(matched_keywords)

    # Bonus score for suspicious URLs
    url_score = len(suspicious_urls) * 3

    # Bonus score for urgency signals
    urgency_score = min(urgency["exclamations"], 5)

    total_score = base_score + url_score + urgency_score

    # --- Step 5: Scam Type Classification ---
    scam_types = classify_scam_type(normalized)

    # --- Step 6: Risk Level ---
    risk_level = get_risk_level(total_score)

    # --- Step 7: Confidence Score ---
    confidence = calculate_confidence(total_score)

    # --- Step 8: Explainable AI — Build explanation ---
    explanations = build_explanation(
        matched_keywords, suspicious_urls, urgency, scam_types, total_score
    )

    return {
        "message_type":       message_type.upper(),
        "risk_level":         risk_level,
        "risk_color":         RISK_COLORS.get(risk_level, "#888"),
        "risk_icon":          RISK_ICONS.get(risk_level, "❓"),
        "confidence":         confidence,
        "total_score":        total_score,
        "base_score":         base_score,
        "url_score":          url_score,
        "urgency_score":      urgency_score,
        "scam_types":         scam_types if scam_types else ["Unknown / General Spam"],
        "matched_high":       matched_keywords["high"],
        "matched_medium":     matched_keywords["medium"],
        "matched_low":        matched_keywords["low"],
        "suspicious_urls":    suspicious_urls,
        "all_urls":           urls,
        "urgency_signals":    urgency,
        "word_count":         len(tokens),
        "explanations":       explanations,
        "is_scam":            risk_level not in ("SAFE",),
    }


# ===========================================================================
# EXPLAINABLE AI — Human-Readable Explanations
# ===========================================================================

def build_explanation(matched, suspicious_urls, urgency, scam_types, score) -> list:
    """
    Explainable AI (XAI) — Generates human-readable reasons
    for why the message was flagged, making the AI decision transparent.
    """
    reasons = []

    if matched["high"]:
        reasons.append(
            f"🔴 Found {len(matched['high'])} HIGH-RISK phrase(s): "
            f"'{', '.join(matched['high'][:3])}'"
            + (" and more..." if len(matched["high"]) > 3 else "")
        )

    if matched["medium"]:
        reasons.append(
            f"🟠 Found {len(matched['medium'])} MEDIUM-RISK phrase(s): "
            f"'{', '.join(matched['medium'][:3])}'"
            + (" and more..." if len(matched["medium"]) > 3 else "")
        )

    if matched["low"]:
        reasons.append(
            f"🟡 Found {len(matched['low'])} LOW-RISK phrase(s): "
            f"'{', '.join(matched['low'][:3])}'"
        )

    if suspicious_urls:
        reasons.append(
            f"🔗 Detected {len(suspicious_urls)} suspicious URL(s): "
            f"{', '.join(suspicious_urls[:2])}"
        )

    if urgency["exclamations"] > 2:
        reasons.append(
            f"❗ Message uses {urgency['exclamations']} exclamation marks "
            f"— a common psychological pressure tactic."
        )

    if urgency["caps_words"] > 3:
        reasons.append(
            f"🔠 Message contains {urgency['caps_words']} ALL-CAPS words "
            f"— often used to create urgency or fear."
        )

    if scam_types:
        reasons.append(
            f"📂 Classified as: {', '.join(scam_types)}"
        )

    if not reasons:
        reasons.append("✅ No significant scam indicators were detected in this message.")

    return reasons
