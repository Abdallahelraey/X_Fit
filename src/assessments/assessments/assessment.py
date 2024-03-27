from src.user.user_profile import UserProfile
from src.modules.rule_based_model.rules import FitnessRules

class Assessment:
    def __init__(self, user_profile):
        self.user_profile = user_profile
        self.fitness_level = self._assess_fitness_level()
        self.preferences = self._preferences_setting()
        self.goals = self._goal_setting()
        self.bmr = self._bmr_calculation()
        self.bmi = self._bmi_calculation()
        self.workout_history = []

    @property
    def weight(self):
        return self.user_profile.weight

    @property
    def height(self):
        return self.user_profile.height

    @property
    def age(self):
        return self.user_profile.age

    @property
    def gender(self):
        return self.user_profile.gender
    

    def _bmr_calculation(self):
        if self.user_profile.weight is not None and self.user_profile.height is not None:
            if self.user_profile.gender == 'male':
                return 88.362 + (13.397 * self.user_profile.weight) + (4.799 * self.user_profile.height) - (5.677 * self.user_profile.age)
            elif self.user_profile.gender == 'female':
                return 447.593 + (9.247 * self.user_profile.weight) + (3.098 * self.user_profile.height) - (4.330 * self.user_profile.age)
        else:
            return None







    def _bmi_calculation(self):
        if self.user_profile.weight is not None and self.user_profile.height is not None:
            return self.user_profile.weight / ((self.user_profile.height / 100) ** 2)
        else:
            return None




    def _assess_fitness_level(self):
        if self.user_profile.age >= 18:
            if self.user_profile.gender == 'male':
                if self.user_profile.weight is not None and self.user_profile.height is not None:
                    bmi = self._bmi_calculation()
                    if 18.5 <= bmi < 24.9:
                        return "Normal"
                    elif 25 <= bmi < 29.9:
                        return "Overweight"
                    elif bmi >= 30:
                        return "Obese"
            elif self.user_profile.gender == 'female':
                if self.user_profile.weight is not None and self.user_profile.height is not None:
                    bmi = self._bmi_calculation()
                    if 18.5 <= bmi < 24.9:
                        return "Normal"
                    elif 25 <= bmi < 29.9:
                        return "Overweight"
                    elif bmi >= 30:
                        return "Obese"
                    # Add female-specific fitness assessment logic here
                    # For example, you could consider factors like body fat percentage, muscle mass, etc.
                    else:
                        return "Female-specific fitness assessment placeholder"
        else:
            return "Age under 18, fitness assessment not applicable"
        return "Fitness level assessment not available for provided data"





    def _preferences_setting(self):
        type_preference = self._determine_type_preference()
        duration_preference = self._determine_duration_preference()
        intensity_preference = self._determine_intensity_preference()

        overall_preferences = {
            'type': type_preference,
            'duration': duration_preference,
            'intensity': intensity_preference,
        }

        return overall_preferences

    def _determine_type_preference(self):
        return input("What type of exercise do you prefer? (e.g., cardio, strength training, yoga): ")

    def _determine_duration_preference(self):
        return input("How long do you prefer to exercise? (e.g., 30 minutes, 1 hour): ")

    def _determine_intensity_preference(self):
        return input("How intense do you prefer your workouts? (e.g., low, moderate, high): ")

    def set_preferences(self, duration, intensity, frequency):
        self.user_profile.preferences['duration'] = duration
        self.user_profile.preferences['intensity'] = intensity
        self.user_profile.preferences['frequency'] = frequency

    def _goal_setting(self):
        fitness_goals_list = [
            "Weight Loss",
            "Muscle Gain",
            "Endurance Improvement",
            "Flexibility Improvement",
            "Core Strength",
            "Functional Strength",
            "Body Composition Improvement",
            "Sports Performance Enhancement",
            "Injury Prevention",
            "Stress Reduction"
        ]
        print("Choose one or more goals from the following options:")
        for i, goal in enumerate(fitness_goals_list, start=1):
            print(f"{i}. {goal}")

        selected_goals_indices = input("Enter the numbers corresponding to your chosen goals (comma-separated): ").split(',')
        selected_goals_indices = [int(index) for index in selected_goals_indices]

        selected_goals = []
        for index in selected_goals_indices:
            if 1 <= index <= len(fitness_goals_list):
                selected_goals.append(fitness_goals_list[index - 1])

        return selected_goals

    def add_workout_to_history(self, workout):
        self.workout_history.append(workout)

    def get_workout_recommendation(self):
        data_to_send = {
            "goal": self.goals,
            "fitness_level": self.fitness_level,
            "age": self.user_profile.age,
            "gender": self.user_profile.gender,
            "weight": self.user_profile.weight,
            "height": self.user_profile.height,
            "preferences": self.user_profile.preferences,
        }
        recommendation = FitnessRules.recommend_workout(data_to_send)
        return recommendation

    def create_workout_plan(self):
        """Creates a workout plan based on user data and recommendations.

        Args:
            user_data (dict): A dictionary containing user information like goals, fitness level, preferences.

        Returns:
            dict: A dictionary representing the workout plan or None if no recommendation is available.
        """

        # Get recommendation from rule engine (assume recommendation format is a dictionary)
        recommendation = self.get_workout_recommendation()

        if recommendation:
            # Extract relevant data from recommendation (e.g., type, duration, intensity)
            workout_type = recommendation.get("type")
            duration = recommendation.get("duration")
            intensity = recommendation.get("intensity")

            # Create workout plan based on recommendation and user data
            workout_plan = {
                "type": workout_type,
                "duration": duration,
                "intensity": intensity,
                "exercises": [],  # Add specific exercises based on type and user profile
                "sets": [],  # Add sets and reps based on intensity and user preferences
                "rest": [],  # Add rest periods based on type and intensity
            }
            return workout_plan

        else:
            # Handle cases where no recommendation is available
            return None  # Or provide alternative message or suggestions
            # Add any error handling or logging as needed




