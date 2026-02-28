from checker import check_requirement
import re
import sys


def is_valid_requirement(text):
    """
    Basic structural validation for requirement statements.
    Returns (True, "") if valid,
    otherwise (False, error_message).
    """

    if not text.strip():
        return False, "Requirement cannot be empty."

    if len(text.split()) < 4:
        return False, "Requirement is too short to be meaningful."

    # Check for at least one modal or verb-like structure
    if not re.search(r"\b(shall|should|must|will|may|can|is|are)\b", text.lower()):
        return False, "Requirement does not appear to contain a valid action or modal verb."

    # Must contain alphabetic characters
    if not re.search(r"[a-zA-Z]", text):
        return False, "Requirement must contain valid textual content."

    return True, ""


if __name__ == "__main__":
    print("=== Requirements Quality Checker ===\n")

    requirement = input("Enter your requirement:\n> ")

    is_valid, error_message = is_valid_requirement(requirement)

    if not is_valid:
        print(f"\n❌ Invalid Requirement: {error_message}")
        sys.exit(1)

    issues, score = check_requirement(requirement)

    print("\n--- Analysis ---")

    if issues:
        for issue in issues:
            print(f"⚠ {issue}")
    else:
        print("✓ No major issues detected.")

    print(f"\nQuality Score: {score}/10")