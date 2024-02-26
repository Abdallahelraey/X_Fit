
from user.user_profile import UserProfile

class Assessment:
    def __init__(self, user_id: int, age: int, gender: str, name: str, email: str, password: str,
                workout_history: list[str], fitness_level: str, fitness_goals: str = "General Health",
                preferences: dict[str, int] = None, medical_conditions: [list[str]] = None, weight: float = None, height: float = None):
        self.user_profile = UserProfile(user_id, age, gender, name, email, password, workout_history, fitness_level, fitness_goals, preferences, medical_conditions, weight, height)
        self.weight = self.user_profile.weight
        self.height = self.user_profile.height
        self.age = self.user_profile.age
        self.gender = self.user_profile.gender
        self.fitness_level = self.user_profile.fitness_level
        self.preferences = self.user_profile.preferences
        self.goals = self.user_profile.fitness_goals

    def bmr_calculation(self):
        if self.gender == 'male':
            return 88.362 + (13.397 * self.weight) + (4.799 * self.height) - (5.677 * self.age)
        elif self.gender == 'female':
            return 447.593 + (9.247 * self.weight) + (3.098 * self.height) - (4.330 * self.age)

    def bmi_calculation(self):
        return self.weight / ((self.height / 100) ** 2)

    def fitness_level_assessment(self):
        # This is a placeholder. You would replace this with actual logic to assess fitness level.
        return self.fitness_level

    def preferences_setting(self):
        # This is a placeholder. You would replace this with actual logic to assess exercise preferences.
        return self.preferences

    def goal_setting(self):
        # This is a placeholder. You would replace this with actual logic to set goals.
        return self.goals
