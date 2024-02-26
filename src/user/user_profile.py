from src.user import User
from src.opt_model.stabilization.stabilization_endurance import StabilizationEndurance

class UserProfile(User):
    def __init__(self, user_id: int, age: int, gender: str, name: str, email: str, password: str,
                workout_history: list[str], fitness_level: str, fitness_goals: str = "General Health",
                preferences: dict[str, int] = None, medical_conditions: [list[str]] = None, weight: float = None, height: float = None):
        super().__init__(user_id, age, gender, name, email, password)
        self.fitness_level = fitness_level
        self.workout_history = list(workout_history) if workout_history else []
        self.fitness_goals = fitness_goals or "General Health"
        self.preferences = preferences
        self.medical_conditions = medical_conditions or []
        self._weight = weight
        self._height = height

        
    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, new_weight):
        self._weight = new_weight

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, new_height):
        self._height = new_height

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        self._age = new_age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, new_user_id):
        self._user_id = new_user_id

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, new_gender):
        self._gender = new_gender

    @property
    def fitness_level(self):
        return self._fitness_level

    @fitness_level.setter
    def fitness_level(self, new_fitness_level):
        self._fitness_level = new_fitness_level

    @property
    def fitness_goals(self):
        return self._fitness_goals

    @fitness_goals.setter
    def fitness_goals(self, new_fitness_goals):
        self._fitness_goals = new_fitness_goals

    @property
    def workout_history(self):
        return self._workout_history

    @workout_history.setter
    def workout_history(self, new_workout_history):
        self._workout_history = new_workout_history

    @property
    def preferences(self):
        return self._preferences

    @preferences.setter
    def preferences(self, new_preferences):
        self._preferences = new_preferences

    @property
    def medical_conditions(self):
        return self._medical_conditions

    @medical_conditions.setter
    def medical_conditions(self, new_medical_conditions):
        self._medical_conditions = new_medical_conditions


    # Additional methods can be added based on our requirements

    def add_workout_to_history(self, workout):
        self.workout_history.append(workout)

    def set_fitness_goals(self, fitness_goals):
        self.fitness_goals = fitness_goals

    def get_profile_info(self):
        return f"User Profile for {self.user.user_id}: Fitness Goals: {self.fitness_goals}, Preferred Duration: {self.preferred_duration}"

    def set_preferences(self, duration, intensity, frequency):
        self.preferences['duration'] = duration
        self.preferences['intensity'] = intensity
        self.preferences['frequency'] = frequency

    def get_personalized_recommendation(self):
        # Implement logic to generate personalized workout recommendations
        # based on user preferences and history.
        # We can use machine learning models or rule-based systems for this.

        # Example: Dummy recommendation

        inintial_plan = StabilizationEndurance()
        inintial_plan.flexibility()
        trainings = self.workout_history #["Push-ups", "Running", "Plank"]
        parameters =  inintial_plan.flexibility_training_parameters
        return trainings, parameters.__dict__
