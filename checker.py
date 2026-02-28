# Optional future AI integration (currently inactive)
from ai_module import RequirementQualityModel

_ai_model = RequirementQualityModel()
_ai_model.load_model()

def check_requirement(text):
    results = {
        "Clarity": [],
        "Unambiguity": [],
        "Verifiability": [],
        "Atomicity": []
    }

    suggestions = []
    score = 10
    text_lower = text.lower()

    # --- Unambiguity ---
    ambiguous_terms = ["fast", "efficient", "user-friendly", "robust", "easy"]
    for word in ambiguous_terms:
        if word in text_lower:
            results["Unambiguity"].append(
                f"Ambiguous term detected: '{word}'"
            )
            suggestions.append(
                f"Replace '{word}' with a measurable criterion (e.g., response time < 2 seconds)."
            )
            score -= 1

    # --- Clarity ---
    weak_modals = ["should", "may", "might", "could"]
    for word in weak_modals:
        if word in text_lower:
            results["Clarity"].append(
                f"Weak modal verb detected: '{word}'"
            )
            suggestions.append(
                f"Replace '{word}' with 'shall' to indicate mandatory requirement."
            )
            score -= 1

    # --- Verifiability ---
    if not any(char.isdigit() for char in text):
        results["Verifiability"].append(
            "No measurable criteria found."
        )
        suggestions.append(
            "Add quantifiable metrics (e.g., 'within 3 seconds', '99% accuracy')."
        )
        score -= 2

    # --- Atomicity ---
    if " and " in text_lower:
        results["Atomicity"].append(
            "Requirement may not be atomic (contains 'and')."
        )
        suggestions.append(
            "Consider splitting into separate independent requirements."
        )
        score -= 1

    return results, suggestions, max(score, 0)


