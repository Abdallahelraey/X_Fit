from src.opt_model.fitness_phase import FitnessPhase
from src.opt_model.training_parameters import TrainingParameters


class StabilizationEndurance(FitnessPhase):
    def __init__(self):
        super().__init__()
        self.duration = 8  # 8 weeks
        self.intensity = "Moderate" # Adjust based on the intended overall intensity level

    def flexibility(self):
        # Define specific flexibility training plan for Stabilization Endurance phase
        self.flexibility_training_parameters = TrainingParameters(muscle_groups="Specific", reps=(1, 3), sets=(1, 1), tempo=30, intensity="Low", load="Light", rest=(30, 60), schedule="Fixed", frequency=(3, 7), volume="Low", split="Full Body", duration=(self.duration), exercise_selection="SMR and static")

    def core(self):
        # Define specific core training plan for Stabilization Endurance phase
        self.core_training_parameters = TrainingParameters(muscle_groups="General", reps=(12, 20), sets=(1, 4), tempo="Slow 4/2/1", intensity="Moderate", load="Moderate", rest=(0, 90), schedule="Flexible", frequency=(2, 4), volume=None, split="Full Body", duration=(self.duration), exercise_selection="1–4 core-stabilization")

    def balance(self):
        # Define specific balance training plan for Stabilization Endurance phase
        self.balance_training_parameters = TrainingParameters(muscle_groups="General", reps=(12, 20), sets=(6, 10), tempo="Slow 4/2/1", intensity="Moderate", load="Moderate", rest=(0, 90), schedule="Flexible", frequency=(2, 4), volume=None, split="Full Body", duration=(self.duration), exercise_selection="1–4 balance-stabilization")

    def plyometric(self):
        # Define specific plyometric training plan for Stabilization Endurance phase (likely minimal or absent)
        self.plyometric_training_parameters = TrainingParameters(muscle_groups="General", reps=(5, 8), sets=(1, 3), tempo="3–5 s hold on landing", intensity="Moderate", load="Moderate", rest=(0, 90), schedule="Flexible", frequency=(4), volume=None, split="Full Body", duration=(4, 6), exercise_selection="0–2 plyometric-stabilization")

    def saq(self):
        # Define specific SAQ training plan for Stabilization Endurance phase (likely minimal or absent)
        self.saq_training_parameters = TrainingParameters(muscle_groups="General", reps=(2, 3), sets=(1, 2), tempo="Moderate", intensity="Moderate", load="Moderate", rest=(0, 90), schedule="Flexible", frequency=(2, 4), volume=None, split="Full Body", duration=(self.duration), exercise_selection="4–6 drills with limited horizontal inertia and unpredictability")

    def resistance(self):
        # Define specific resistance training plan for Stabilization Endurance phase, focusing on low weight, high reps
        self.resistance_training_parameters = TrainingParameters(muscle_groups="General", reps=(2, 3), sets=(1, 2), tempo="Moderate", intensity="Moderate", load="Low", rest=(0, 90), schedule="Flexible", frequency=(2, 4), volume=None, split="Full Body", duration=(self.duration), exercise_selection="Varied")

    def display_training_parameters(self, training_parameters):
        """Display the attributes of the provided TrainingParameters object."""
        super().display_training_parameters(training_parameters)

    def plan(self):
        """
        Define the specific training plan for the Stabilization phase.
        """
        print("Planning Stabilization phase...")
        # Implement logic to define exercise selection, workout structure, and progression strategie
        # Call all the functions to initialize parameters
        self.flexibility()
        self.core()
        self.balance()
        self.plyometric()
        self.saq()
        self.resistance()
        # Define the structure of the training plan
        training_plan = {
            "Flexibility": self.flexibility_training_parameters,
            "Core": self.core_training_parameters,
            "Balance": self.balance_training_parameters,
            "Plyometric": self.plyometric_training_parameters,
            "SAQ": self.saq_training_parameters,
            "Resistance": self.resistance_training_parameters
        }
        
        # Display the training parameters for each phase
        for phase, parameters in training_plan.items():
            print(f"\n{phase} Training Plan:")
            self.display_training_parameters(parameters)

    def set_parameters(self, training, params: TrainingParameters):
        """
        Set common training parameters for the Stabilization phase.
        """
        super().set_parameters(training, params)

    def evaluate_progress(self):
        """
        Evaluate and track progress during the Stabilization phase based on workout data.
        """
        super().evaluate_progress()
        # Implement logic to evaluate progress based on training data and OPT principles

    def record_workouts(self, workouts):
        """
        Record completed workouts for the Stabilization phase.
        """
        super().record_workouts(workouts)
        # Implement logic to store completed workouts and link them to the phase

    def adaptations(self):
        """
        Define Stabilization phase-specific adaptations based on progress and OPT principles.
        """
        print("Defining Stabilization phase adaptations...")
        # Implement logic to define phase-specific adaptations

    def progression_methodology(self):
        """
        Define Stabilization phase-specific progression methodologies based on OPT model principles.
        """
        print("Defining Stabilization phase progression methodology...")
        # Implement logic to define phase-specific progression methodologies

    def display_summary(self):
        """
        Display a summary of the Stabilization phase.
        """
        super().display_summary()
        print(f"Focus: Building foundational stability and muscular endurance")
