# feedback.py

class FeedbackSynthesizer:
    """
    .
    """

    def generate_feedback(self, score_dict):
        feedback = []

        if score_dict["semantic_similarity"] < 0.5:
            feedback.append("Requirement may lack semantic clarity.")

        if score_dict["rule_score"] == 0:
            feedback.append("Consider using formal modal verbs (shall/must).")

        if score_dict["final_score"] > 0.75:
            feedback.append("Requirement quality is strong.")

        return feedback