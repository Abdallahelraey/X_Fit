from src.opt_model.fitness_phase import FitnessPhase
from src.opt_model.training_parameters import TrainingParameters


class Hypetrophy(FitnessPhase):
    def __init__(self):
        super().__init__()
        self.duration = None  # weeks
        self.intensity = None

    def flexibility(self):
        # Define specific flexibility training plan for Stabilization Endurance phase
         self.flexibility_training_parameters = TrainingParameters(muscle_groups="Specific", reps=(5, 10), sets=(1, 2), tempo="1–2 s hold", intensity="Low", load="Light", rest=(0, 0), schedule="Fixed", frequency=(3, 7), volume="Low", split="Full Body", duration=(self.duration), exercise_selection="SMR and active*")
    def core(self):
        # Define specific core training plan for Stabilization Endurance phase
         self.core_training_parameters = TrainingParameters(muscle_groups="General", reps=(8, 12), sets=(2, 3), tempo="Medium", intensity="Moderate", load="Moderate", rest=(0, 60), schedule="Flexible", frequency=(3, 6), volume=None, split="0–4 core-strength", duration=(self.duration), exercise_selection="0–4 core-strength")

    def balance(self):
        # Define specific balance training plan for Stabilization Endurance phase
         self.balance_training_parameters = TrainingParameters(muscle_groups="General", reps=(8, 12), sets=(2, 3), tempo="Medium", intensity="Moderate", load="Moderate", rest=(0, 60), schedule="Flexible", frequency=(3, 6), volume=None, split="Full Body", duration=(self.duration), exercise_selection="0–4 balance-strength")

    def plyometric(self):
        # Define specific plyometric training plan for Stabilization Endurance phase (likely minimal or absent)
        self.plyometric_training_parameters = TrainingParameters(muscle_groups="General", reps=(8, 10), sets=(2, 3), tempo="Repeating", intensity="Moderate", load="Moderate", rest=(0, 60), schedule="Flexible", frequency=(3, 6), volume=None, split="Full Body", duration=(self.duration), exercise_selection="0–4 plyometric-strength")

    def saq(self):
        # Define specific SAQ training plan for Stabilization Endurance phase (likely minimal or absent)
        self.saq_training_parameters = TrainingParameters(muscle_groups="General", reps=(3, 5), sets=(3, 4), tempo="Fast", intensity="Moderate", load="Moderate", rest=(0, 60), schedule="Flexible", frequency=(2, 4), volume=None, split="Full Body", duration=(self.duration), exercise_selection="6–8 drills allowing greater horizontal inertia but limited unpredictability")

    def resistance(self):
        # Define specific resistance training plan for Stabilization Endurance phase, focusing on low weight, high reps
        self.resistance_training_parameters = TrainingParameters(muscle_groups="General", reps=(6, 12), sets=(3, 5), tempo="2/0/2", intensity="75–85%", load="Moderate", rest=(0, 60), schedule="Flexible", frequency=(3, 6), volume=None, split="Full Body", duration=(self.duration), exercise_selection="2–4 strength level exercises/body part")

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

