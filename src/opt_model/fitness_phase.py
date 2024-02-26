from abc import ABC, abstractmethod
from src.opt_model.training_parameters import TrainingParameters


class FitnessPhase(ABC):
    def __init__(self):
        self.flexibility_training_parameters = TrainingParameters(muscle_groups=None, reps=None, sets=None, tempo=None, intensity=None, load=None, rest=None, schedule=None, frequency=None, volume=None, split=None, duration=None, exercise_selection=None)
        self.core_training_parameters = TrainingParameters(muscle_groups=None, reps=None, sets=None, tempo=None, intensity=None, load=None, rest=None, schedule=None, frequency=None, volume=None, split=None, duration=None, exercise_selection=None)
        self.balance_training_parameters = TrainingParameters(muscle_groups=None, reps=None, sets=None, tempo=None, intensity=None, load=None, rest=None, schedule=None, frequency=None, volume=None, split=None, duration=None, exercise_selection=None)
        self.plyometric_training_parameters = TrainingParameters(muscle_groups=None, reps=None, sets=None, tempo=None, intensity=None, load=None, rest=None, schedule=None, frequency=None, volume=None, split=None, duration=None, exercise_selection=None)
        self.saq_training_parameters = TrainingParameters(muscle_groups=None, reps=None, sets=None, tempo=None, intensity=None, load=None, rest=None, schedule=None, frequency=None, volume=None, split=None, duration=None, exercise_selection=None)
        self.resistance_training_parameters = TrainingParameters(muscle_groups=None, reps=None, sets=None, tempo=None, intensity=None, load=None, rest=None, schedule=None, frequency=None, volume=None, split=None, duration=None, exercise_selection=None)
        self.progress_data = {}
        self.duration = None  # weeks
        self.intensity = None
        self.trainings = ["flexibility", "core", "balance", "plyometric", "saq" , "resistance"]

    @abstractmethod
    def flexibility(self):
        """
        Abstract method to be implemented by concrete classes.
        Define the flexibility training plan for the phase, including:
        - Exercise selection
        - Progression strategies
        """
        self.flexibility_training_parameters = None

    @abstractmethod
    def core(self):
        """
        Abstract method to be implemented by concrete classes.
        Define the core training plan for the phase, including:
        - Exercise selection
        - Progression strategies
        """
        self.core_training_parameters = None

    @abstractmethod
    def balance(self):
        """
        Abstract method to be implemented by concrete classes.
        Define the balance training plan for the phase, including:
        - Exercise selection
        - Progression strategies
        """
        self.balance_training_parameters = None

    @abstractmethod
    def plyometric(self):
        """
        Abstract method to be implemented by concrete classes.
        Define the plyometric training plan for the phase, including:
        - Exercise selection
        - Progression strategies
        """
        self.plyometric_training_parameters = None

    @abstractmethod
    def saq(self):
        """
        Abstract method to be implemented by concrete classes.
        Define the SAQ (speed, agility, and quickness) training plan for the phase, including:
        - Exercise selection
        - Progression strategies
        """
        self.saq_training_parameters = None

    @abstractmethod
    def resistance(self):
        """
        Abstract method to be implemented by concrete classes.
        Define the resistance training plan for the phase, including:
        - Exercise selection
        - Progression strategies
        """
        self.resistance_training_parameters = None

    @abstractmethod
    def display_training_parameters(self, training_parameters):
        """Display the attributes of the provided TrainingParameters object."""
        print("Training Parameters:")
        print(f"- Muscle Groups: {training_parameters.muscle_groups}")
        print(f"- Reps: {training_parameters.reps}")
        print(f"- Sets: {training_parameters.sets}")
        print(f"- Tempo: {training_parameters.tempo}")
        print(f"- Intensity: {training_parameters.intensity}")
        print(f"- Rest: {training_parameters.rest}")
        print(f"- Load: {training_parameters.load}")
        print(f"- Schedule: {training_parameters.schedule}")
        print(f"- Frequency: {training_parameters.frequency}")
        print(f"- Volume: {training_parameters.volume}")
        print(f"- Split: {training_parameters.split}")
        print(f"- Duration: {training_parameters.duration}")
        print(f"- Exercise Selection: {training_parameters.exercise_selection}")


    @abstractmethod
    def plan(self):
        """
        Abstract method to be implemented by concrete classes.
        Should define the specific training plan for the phase, including:
        - Exercise selection
        - Workout structure
        - Progression strategies
        """
        pass

    @abstractmethod
    def set_parameters(self, training, params: TrainingParameters):
        """
        Set common training parameters for the phase.
        """
        
        print("Common training parameters set.")

    @abstractmethod
    def evaluate_progress(self):
        """
        Evaluate and track progress during the phase based on workout data.
        Update progress_data dictionary.
        """
        print("Evaluating progress...")

        # Implement logic to evaluate progress based on training data and OPT principles
        # Update self.progress_data with relevant metrics

    @abstractmethod
    def record_workouts(self, workouts):
        """
        Record completed workouts for the phase.
        """
        print("Recording workouts...")

        # Implement logic to store completed workouts and link them to the phase

    @abstractmethod
    def adaptations(self):
        """
        Abstract method to be implemented by concrete classes.
        Define phase-specific adaptations based on progress and OPT principles.
        """
        pass

    @abstractmethod
    def progression_methodology(self):
        """
        Abstract method to be implemented by concrete classes.
        Define phase-specific progression methodologies based on OPT model principles.
        """
        pass

    @abstractmethod
    def display_summary(self):
        """
        Display a summary of the fitness phase.
        """
        print(f"Phase: {self.__class__.__name__}")
        print(f"Duration: {self.duration} weeks")
        print(f"Intensity: {self.intensity}")
        print(f"Training Parameters:")
        print(f"\t- Reps: {self.training_parameters.reps}")
        print(f"\t- Sets: {self.training_parameters.sets}")
        print(f"\t- Rest Interval: {self.training_parameters.rest_interval} seconds")
        print(f"\t- Load: {self.training_parameters.load} lbs")
        print(f"Progress Data:")
        # Print relevant progress metrics from self.progress_data

 

