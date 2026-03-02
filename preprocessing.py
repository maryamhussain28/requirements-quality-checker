# preprocessing.py

import re
from typing import List

class TextPreprocessor:
    """
    Handles requirement text cleaning and normalization.
    This module is intentionally isolated from scoring logic.
    """

    def __init__(self):
        pass

    def clean_text(self, text: str) -> str:
        text = text.lower()
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'[^\w\s.]', '', text)
        return text.strip()

    def tokenize(self, text: str) -> List[str]:
        return text.split()

    def preprocess(self, text: str) -> dict:
        cleaned = self.clean_text(text)
        tokens = self.tokenize(cleaned)

        return {
            "cleaned_text": cleaned,
            "tokens": tokens,
            "length": len(tokens)
        }