
from src.opt_model.fitness_phase import FitnessPhase
from src.opt_model.training_parameters import TrainingParameters


class Power(FitnessPhase):
    def __init__(self):
        super().__init__()
        self.duration = None  # weeks
        self.intensity = None

    def flexibility(self):
        # Define specific flexibility training plan for Stabilization Endurance phase
        self.flexibility_training_parameters = TrainingParameters(muscle_groups="Specific", reps=(10, 15), sets=(1, 2), tempo="Controlled", intensity="Low", load="Light", rest=(0, 0), schedule="Fixed", frequency=(3, 7), volume="Low", split="Full Body", duration=(self.duration), exercise_selection="SMR and dynamic 3–10 exercises")


    def core(self):
        # Define specific core training plan for Stabilization Endurance phase
        self.core_training_parameters = TrainingParameters(muscle_groups="General", reps=(8, 12), sets=(2, 3), tempo="X/X/X", intensity="Moderate", load="Moderate", rest=(0, 60), schedule="Flexible", frequency=(2, 4), volume=None, split="0–2 core-power", duration=(self.duration), exercise_selection="0–2 core-power")


    def balance(self):
        # Define specific balance training plan for Stabilization Endurance phase
        self.balance_training_parameters = TrainingParameters(muscle_groups="General", reps=(8, 12), sets=(2, 3), tempo="Controlled", intensity="Moderate", load="Moderate", rest=(0, 60), schedule="Flexible", frequency=(2, 4), volume=None, split="Full Body", duration=(self.duration), exercise_selection="0–2 balance-power")


    def plyometric(self):
        # Define specific plyometric training plan for Stabilization Endurance phase (likely minimal or absent)
        self.plyometric_training_parameters = TrainingParameters(muscle_groups="General", reps=(8, 12), sets=(2, 3), tempo="X/X/X", intensity="Moderate", load="Moderate", rest=(0, 60), schedule="Flexible", frequency=(2, 4), volume=None, split="Full Body", duration=(self.duration), exercise_selection="0–2 plyometric-power")


    def saq(self):
        # Define specific SAQ training plan for Stabilization Endurance phase (likely minimal or absent)
        self.saq_training_parameters = TrainingParameters(muscle_groups="General", reps=(3, 5), sets=(3, 5), tempo="X/X/X", intensity="Moderate", load="Moderate", rest=(0, 90), schedule="Flexible", frequency=(2, 4), volume=None, split="Full Body", duration=(self.duration), exercise_selection="6–10 drills allowing maximal horizontal inertia and unpredictability")


    def resistance(self):
        # Define specific resistance training plan for Stabilization Endurance phase, focusing on low weight, high reps
        self.resistance_training_parameters = TrainingParameters(muscle_groups="General", reps=(1, 5), sets=(8, 10), tempo="X/X/X (S) X/X/X (P)", intensity="(Strength) 85–100% (Power) up to 10% BW or 30–45% 1RM", load="Moderate", rest=(60, 120), schedule="Flexible", frequency=(2, 4), volume=None, split="Full Body", duration=(self.duration), exercise_selection="1 strength superset with 1 power")
    
    def display_training_parameters(self, training_parameters):
        """Display the attributes of the provided TrainingParameters object."""
        super().display_training_parameters(training_parameters)

    def plan(self):
        """
        Define the specific training plan for the Stabilization phase.
        """
        print("Planning Stabilization phase...")
        # Implement logic to define exercise selection, workout structure, and progression strategies

    def set_parameters(self, params: TrainingParameters):
        """
        Set common training parameters for the Stabilization phase.
        """
        super().set_parameters(params)

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

