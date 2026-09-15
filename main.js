/**
 * main.js — ScamShield AI
 * Purpose: Frontend interactivity for the scam detector web app
 * 
 * Features:
 *   - Live character count on textarea
 *   - Submit button loading state
 *   - Confidence bar animation on result page
 *   - Auto-resize textarea
 */

document.addEventListener("DOMContentLoaded", function () {

  // -----------------------------------------------------------------------
  // 1. LIVE CHARACTER COUNT
  // -----------------------------------------------------------------------
  const textarea = document.getElementById("message");
  const charCount = document.getElementById("charCount");

  if (textarea && charCount) {
    textarea.addEventListener("input", function () {
      charCount.textContent = this.value.length;

      // Warn if message is very short
      if (this.value.length > 0 && this.value.length < 10) {
        charCount.style.color = "#e74c3c";
      } else {
        charCount.style.color = "#6b7280";
      }
    });
  }


  // -----------------------------------------------------------------------
  // 2. SUBMIT BUTTON — LOADING STATE
  // -----------------------------------------------------------------------
  const form = document.getElementById("analyzeForm");
  const submitBtn = document.getElementById("submitBtn");

  if (form && submitBtn) {
    form.addEventListener("submit", function () {
      submitBtn.textContent = "⏳ Analyzing...";
      submitBtn.disabled = true;
      submitBtn.style.opacity = "0.8";
    });
  }


  // -----------------------------------------------------------------------
  // 3. CONFIDENCE BAR — ANIMATE ON RESULT PAGE
  // -----------------------------------------------------------------------
  const confBarInner = document.querySelector(".conf-bar-inner");
  if (confBarInner) {
    // Start at 0 width, then animate to the actual width
    const targetWidth = confBarInner.style.width;
    confBarInner.style.width = "0%";
    setTimeout(() => {
      confBarInner.style.width = targetWidth;
    }, 200);
  }


  // -----------------------------------------------------------------------
  // 4. AUTO-RESIZE TEXTAREA AS USER TYPES
  // -----------------------------------------------------------------------
  if (textarea) {
    textarea.addEventListener("input", function () {
      this.style.height = "auto";
      this.style.height = Math.max(160, this.scrollHeight) + "px";
    });
  }


  // -----------------------------------------------------------------------
  // 5. HIGHLIGHT TEXTAREA BORDER ON FOCUS
  // -----------------------------------------------------------------------
  if (textarea) {
    textarea.addEventListener("focus", function () {
      this.style.borderColor = "#3b82d4";
    });
    textarea.addEventListener("blur", function () {
      this.style.borderColor = "#d1d5db";
    });
  }


  // -----------------------------------------------------------------------
  // 6. SCROLL TO FIRST CARD SMOOTHLY ON RESULT PAGE
  // -----------------------------------------------------------------------
  const verdictBanner = document.querySelector(".verdict-banner");
  if (verdictBanner) {
    setTimeout(() => {
      verdictBanner.scrollIntoView({ behavior: "smooth", block: "start" });
    }, 100);
  }

});
