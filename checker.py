def check_requirement(text):
    """
    Evaluates a requirement statement across four quality dimensions:
    - Clarity
    - Unambiguity
    - Verifiability
    - Atomicity

    Returns:
        results (dict)
        suggestions (list)
        score (int out of 10)
    """

    # ----------- INPUT VALIDATION -----------
    if not text or not text.strip():
        return (
            {"Error": ["Requirement cannot be empty."]},
            ["Please enter a valid requirement statement."],
            0
        )

    if len(text.split()) < 4:
        return (
            {"Error": ["Requirement is too short to evaluate meaningfully."]},
            ["Provide a complete requirement sentence."],
            0
        )

    results = {
        "Clarity": [],
        "Unambiguity": [],
        "Verifiability": [],
        "Atomicity": []
    }

    suggestions = []
    score = 10
    text_lower = text.lower()

    # ----------- UNAMBIGUITY -----------
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

    # ----------- CLARITY -----------
    weak_modals = ["should", "may", "might", "could"]
    for word in weak_modals:
        if word in text_lower:
            results["Clarity"].append(
                f"Weak modal verb detected: '{word}'"
            )
            suggestions.append(
                f"Replace '{word}' with 'shall' to indicate a mandatory requirement."
            )
            score -= 1

    # ----------- VERIFIABILITY -----------
    if not any(char.isdigit() for char in text):
        results["Verifiability"].append(
            "No measurable criteria found."
        )
        suggestions.append(
            "Add quantifiable metrics (e.g., 'within 3 seconds', '99% accuracy')."
        )
        score -= 2

    # ----------- ATOMICITY -----------
    if " and " in text_lower:
        results["Atomicity"].append(
            "Requirement may not be atomic (contains 'and')."
        )
        suggestions.append(
            "Consider splitting into separate independent requirements."
        )
        score -= 1

    # Prevent negative score
    score = max(score, 0)

    return results, suggestions, score