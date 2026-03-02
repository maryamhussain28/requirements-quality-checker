# pipeline_adapter.py

class QualityEvaluationAdapter:
    """
    Safe wrapper that integrates the new modular backend
   
    """

    def __init__(self, existing_function=None):
        self.existing_function = existing_function

        # Lazy import to avoid interfering with runtime
        #from backend.pipeline.orchestrator import RequirementsQualityPipeline
        #self.pipeline = RequirementsQualityPipeline()

    def run(self, requirement_text, reference_text):
        # Run original functionality first
        original_output = None
        if self.existing_function:
            original_output = self.existing_function(requirement_text)

        # Run new modular backend
        pipeline_output = self.pipeline.evaluate(
            requirement_text,
            reference_text
        )

        return {
            "original_output": original_output,
            "quality_analysis": pipeline_output
        }