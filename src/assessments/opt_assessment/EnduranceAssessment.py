

from src.assessments.opt_assessment.OPTPhaseAssessment import OPTPhaseAssessment

class EnduranceAssessment(OPTPhaseAssessment):
    def __init__(self, user_data):
        super().__init__(user_data)

    def calculate_score(self):
        """
        Calculate the endurance assessment score based on the recorded user data.
        """
        # Implement scoring algorithm for endurance assessment
        running_distance = self.assessment_data.get('running_distance', 0)
        running_time = self.assessment_data.get('running_time', 0)
        cycling_distance = self.assessment_data.get('cycling_distance', 0)
        cycling_time = self.assessment_data.get('cycling_time', 0)

        # Calculate endurance score based on the recorded data
        endurance_score = (running_distance / running_time) * 0.4 + (cycling_distance / cycling_time) * 0.6

        self.score = endurance_score

    def run_assessment(self):
        """
        Execute the endurance assessment phase.
        """
        print("Starting endurance assessment...")

        # Collect user data for running
        running_distance = float(input("Enter the distance (in miles) you ran: "))
        running_time = float(input("Enter the time (in minutes) it took you to run: "))
        self.record_user_data({'running_distance': running_distance, 'running_time': running_time})

        # Collect user data for cycling
        cycling_distance = float(input("Enter the distance (in miles) you cycled: "))
        cycling_time = float(input("Enter the time (in minutes) it took you to cycle: "))
        self.record_user_data({'cycling_distance': cycling_distance, 'cycling_time': cycling_time})

        # Calculate the endurance score
        self.calculate_score()

        print(f"Your endurance assessment score is: {self.get_score()}")
        