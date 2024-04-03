

from src.assessments.opt_assessment.OPTPhaseAssessment import OPTPhaseAssessment

class FlexibilityAssessment(OPTPhaseAssessment):
    def __init__(self, user_data):
        super().__init__(user_data)

    def calculate_score(self):
        """
        Calculate the flexibility assessment score based on the recorded user data.
        """
        # Implement scoring algorithm for flexibility assessment
        sit_and_reach = self.assessment_data.get('sit_and_reach', 0)
        shoulder_mobility = self.assessment_data.get('shoulder_mobility', 0)
        trunk_rotation = self.assessment_data.get('trunk_rotation', 0)

        # Calculate flexibility score based on the recorded data
        flexibility_score = (sit_and_reach * 0.4) + (shoulder_mobility * 0.3) + (trunk_rotation * 0.3)

        self.score = flexibility_score

    def run_assessment(self):
        """
        Execute the flexibility assessment phase.
        """
        print("Starting flexibility assessment...")

        # Collect user data for sit-and-reach exercise
        sit_and_reach = float(input("Enter your score (in inches) for the sit-and-reach test: "))
        self.record_user_data({'sit_and_reach': sit_and_reach})

        # Collect user data for shoulder mobility exercise
        shoulder_mobility = float(input("Enter your score (0-10) for the shoulder mobility test: "))
        self.record_user_data({'shoulder_mobility': shoulder_mobility})

        # Collect user data for trunk rotation exercise
        trunk_rotation = float(input("Enter your score (in degrees) for the trunk rotation test: "))
        self.record_user_data({'trunk_rotation': trunk_rotation})

        # Calculate the flexibility score
        self.calculate_score()

        print(f"Your flexibility assessment score is: {self.get_score()}")
        