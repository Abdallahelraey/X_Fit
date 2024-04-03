

from src.assessments.opt_assessment.OPTPhaseAssessment import OPTPhaseAssessment

class PowerAssessment(OPTPhaseAssessment):
    def __init__(self, user_data):
        super().__init__(user_data)

    def calculate_score(self):
        """
        Calculate the power assessment score based on the recorded user data.
        """
        # Implement scoring algorithm for power assessment
        vertical_jump = self.assessment_data.get('vertical_jump', 0)
        medicine_ball_throw = self.assessment_data.get('medicine_ball_throw', 0)
        plyometric_score = self.assessment_data.get('plyometric_score', 0)

        # Calculate power score based on the recorded data
        power_score = (vertical_jump * 0.4) + (medicine_ball_throw * 0.3) + (plyometric_score * 0.3)

        self.score = power_score

    def run_assessment(self):
        """
        Execute the power assessment phase.
        """
        print("Starting power assessment...")

        # Collect user data for vertical jump
        vertical_jump = float(input("Enter your vertical jump height (in inches): "))
        self.record_user_data({'vertical_jump': vertical_jump})

        # Collect user data for medicine ball throw
        medicine_ball_throw = float(input("Enter the distance (in feet) you threw the medicine ball: "))
        self.record_user_data({'medicine_ball_throw': medicine_ball_throw})

        # Collect user data for plyometric exercise
        plyometric_score = float(input("Enter your score (0-10) for the plyometric exercise: "))
        self.record_user_data({'plyometric_score': plyometric_score})

        # Calculate the power score
        self.calculate_score()

        print(f"Your power assessment score is: {self.get_score()}")
        