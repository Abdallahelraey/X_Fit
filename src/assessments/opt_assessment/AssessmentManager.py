

class AssessmentManager:
    def __init__(self, user_data):
        self.user_data = user_data
        self.assessments = []
        self.assessment_scores = {}

    def register_assessment(self, assessment_class):
        """
        Register an assessment phase with the manager.

        Args:
            assessment_class (OPTPhaseAssessment): A class representing an assessment phase.
        """
        assessment = assessment_class(self.user_data)
        self.assessments.append(assessment)

    def run_assessments(self):
        """
        Execute all registered assessment phases.
        """
        for assessment in self.assessments:
            assessment.run_assessment()
            score = assessment.get_score()
            self.assessment_scores[type(assessment).__name__] = score

    def generate_report(self):
        """
        Generate and print a report summarizing the assessment scores.
        """
        print("Assessment Report:")
        for assessment_name, score in self.assessment_scores.items():
            print(f"{assessment_name}: {score}")


    def get_score_for_phase(self, phase_name):
        """
        Get the assessment score for a specific phase.

        Args:
            phase_name (str): Name of the assessment phase.

        Returns:
            float: The assessment score for the specified phase, or None if the phase is not found.
        """
        return self.assessment_scores.get(phase_name)