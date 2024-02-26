
from user.user_profile import UserProfile

from src.modules.rule_based_model.rules import FitnessRules  

class Assessment:
    def __init__(self, user_id: int, age: int, gender: str, name: str, email: str, password: str, medical_conditions: [list[str]] = None, weight: float = None, height: float = None):
        self.user_profile = UserProfile(user_id, age, gender, name, email, password, medical_conditions, weight, height)
        self.weight = self.user_profile.weight
        self.height = self.user_profile.height
        self.age = self.user_profile.age
        self.gender = self.user_profile.gender
        self.fitness_level = self.assess_fitness_level()
        self.preferences = self.preferences_setting()
        self.goals = self.goal_setting()  
        self.bmi = self.bmi_calculation()
        self.workout_history = []


    def bmr_calculation(self):
        if self.weight is not None and self.height is not None:
            if self.gender == 'male':
                return 88.362 + (13.397 * self.weight) + (4.799 * self.height) - (5.677 * self.age)
            elif self.gender == 'female':
                return 447.593 + (9.247 * self.weight) + (3.098 * self.height) - (4.330 * self.age)
        else:
            # Handle case where weight or height is None
            return None


    def bmi_calculation(self):
        if self.weight is not None and self.height is not None:
            return self.weight / ((self.height / 100) ** 2)
        else:
            # Handle case where weight or height is None
            return None



    def assess_fitness_level(self):
        if self.age >= 18:
            if self.gender == 'male':
                if self.weight is not None and self.height is not None:
                    bmi = self.bmi_calculation()
                    if 18.5 <= bmi < 24.9:
                        return "Normal"
                    elif 25 <= bmi < 29.9:
                        return "Overweight"
                    elif bmi >= 30:
                        return "Obese"
            elif self.gender == 'female':
                if self.weight is not None and self.height is not None:
                    bmi = self.bmi_calculation()
                    if 18.5 <= bmi < 24.9:
                        return "Normal"
                    elif 25 <= bmi < 29.9:
                        return "Overweight"
                    elif bmi >= 30:
                        return "Obese"
                    # Add female-specific fitness assessment logic here
                    # For example, you could consider factors like body fat percentage, muscle mass, etc.
                    else:
                        # Placeholder logic for female fitness assessment
                        return "Female-specific fitness assessment placeholder"
        else:
            return "Age under 18, fitness assessment not applicable"
        return "Fitness level assessment not available for provided data"




    def preferences_setting(self):
        # Define factors influencing exercise preferences
        type_preference = self.determine_type_preference()
        duration_preference = self.determine_duration_preference()
        intensity_preference = self.determine_intensity_preference()
        
        # Combine factors to assess overall preferences
        overall_preferences = {
            'type': type_preference,
            'duration': duration_preference,
            'intensity': intensity_preference,
            # Add more preferences as needed
        }
        
        return overall_preferences

    # Define methods to determine individual preferences
    def determine_type_preference(self):
        # Placeholder logic - ask user for their preferred type of exercise
        return input("What type of exercise do you prefer? (e.g., cardio, strength training, yoga): ")

    def determine_duration_preference(self):
        # Placeholder logic - ask user for their preferred exercise duration
        return input("How long do you prefer to exercise? (e.g., 30 minutes, 1 hour): ")

    def determine_intensity_preference(self):
        # Placeholder logic - ask user for their preferred exercise intensity
        return input("How intense do you prefer your workouts? (e.g., low, moderate, high): ")

    def set_preferences(self, duration, intensity, frequency):
        self.preferences['duration'] = duration
        self.preferences['intensity'] = intensity
        self.preferences['frequency'] = frequency



    def goal_setting(self):
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
            "age": self.age,
            "gender": self.gender,
            "weight": self.weight,
            "height": self.height,
            "preferences": self.preferences,
        # Add other relevant user data as needed
        }
        # Use Reason to load and apply rules
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




