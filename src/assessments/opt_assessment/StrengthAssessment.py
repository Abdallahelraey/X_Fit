

from src.assessments.opt_assessment.OPTPhaseAssessment import OPTPhaseAssessment

class StrengthAssessment(OPTPhaseAssessment):
    def __init__(self, user_data):
        super().__init__(user_data)

    def calculate_score(self):
        """
        Calculate the strength assessment score based on the recorded user data.
        """
        # Implement scoring algorithm for strength assessment
        pushups = self.assessment_data.get('pushups', 0)
        squats = self.assessment_data.get('squats', 0)
        bench_press = self.assessment_data.get('bench_press', 0)
        deadlift = self.assessment_data.get('deadlift', 0)

        # Calculate strength score based on the recorded data
        strength_score = (pushups * 0.2) + (squats * 0.3) + (bench_press * 0.3) + (deadlift * 0.2)

        self.score = strength_score

    def run_assessment(self):
        """
        Execute the strength assessment phase.
        """
        print("Starting strength assessment...")

        # Collect user data for pushups
        pushups = int(input("Enter the number of pushups you completed: "))
        self.record_user_data({'pushups': pushups})

        # Collect user data for squats
        squats = int(input("Enter the number of squats you completed: "))
        self.record_user_data({'squats': squats})

        # Collect user data for bench press
        bench_press = float(input("Enter the maximum weight (in lbs) you benched: "))
        self.record_user_data({'bench_press': bench_press})

        # Collect user data for deadlift
        deadlift = float(input("Enter the maximum weight (in lbs) you deadlifted: "))
        self.record_user_data({'deadlift': deadlift})

        # Calculate the strength score
        self.calculate_score()

        print(f"Your strength assessment score is: {self.get_score()}")