# orchestrator.py

from .preprocessing import TextPreprocessor
#from .embeddings import TransformerEmbeddingEngine
from .scoring import RequirementScorer
from .feedback import FeedbackSynthesizer


class RequirementsQualityPipeline:
    """
    Modular backend pipeline controller.
    Maintains strict separation of concerns.
    """

    def __init__(self):
        self.preprocessor = TextPreprocessor()
       # self.embedding_engine = TransformerEmbeddingEngine()
        self.scorer = RequirementScorer()
        self.feedback_engine = FeedbackSynthesizer()

    def evaluate(self, requirement_text: str, reference_text: str):
        # --- Preprocessing ---
        processed_req = self.preprocessor.preprocess(requirement_text)
        processed_ref = self.preprocessor.preprocess(reference_text)

        # --- Embeddings ---
        req_embedding = self.embedding_engine.generate_embedding(
            processed_req["cleaned_text"]
        )
        ref_embedding = self.embedding_engine.generate_embedding(
            processed_ref["cleaned_text"]
        )

        # --- Scoring ---
        scores = self.scorer.compute_score(
            req_embedding,
            ref_embedding,
            processed_req["tokens"]
        )

        # --- Feedback ---
        feedback = self.feedback_engine.generate_feedback(scores)

        return {
            "scores": scores,
            "feedback": feedback
        }