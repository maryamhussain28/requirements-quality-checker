

from checker import check_requirement

if __name__ == "__main__":
    print("=== Requirements Quality Checker ===\n")
    
    requirement = input("Enter your requirement:\n> ")

    issues, score = check_requirement(requirement)

    print("\n--- Analysis ---")
    if issues:
        for issue in issues:
            print(f"⚠ {issue}")
    else:
        print("✓ No major issues detected.")

    print(f"\nQuality Score: {score}/10")