# scoring.py

import numpy as np

class RequirementScorer:
    """
    Multi-dimensional evaluation logic:
    - Embedding similarity
    - Rule-guided validation
    """

    def __init__(self):
        pass

    def cosine_similarity(self, vec1, vec2):
        return np.dot(vec1, vec2) / (
            np.linalg.norm(vec1) * np.linalg.norm(vec2) + 1e-8
        )

    def rule_based_validation(self, tokens):
        """
        Dummy rule logic.
        Example: Requirement must contain modal verb.
        """
        modal_keywords = ["shall", "must", "should"]
        contains_modal = any(word in tokens for word in modal_keywords)

        return {
            "has_modal": contains_modal,
            "rule_score": 1 if contains_modal else 0
        }

    def compute_score(self, embedding_a, embedding_b, tokens):
        similarity = self.cosine_similarity(embedding_a, embedding_b)
        rule_eval = self.rule_based_validation(tokens)

        final_score = (0.7 * similarity) + (0.3 * rule_eval["rule_score"])

        return {
            "semantic_similarity": similarity,
            "rule_score": rule_eval["rule_score"],
            "final_score": final_score
        }