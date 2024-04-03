




class FitnessRules:
    @staticmethod
    def recommend_workout(user_data):
        """
        Recommend a personalized workout based on user's goals, fitness level, and preferences.

        Args:
            user_data (dict): User data containing keys "goal", "fitness_level", "preferences", etc.

        Returns:
            dict or None: Recommended workout details or None if recommendation cannot be made.
        """
        goal = user_data.get("goal")
        fitness_level = user_data.get("fitness_level")
        preferences = user_data.get("preferences", {})

        if goal is None or fitness_level is None:
            raise ValueError("User data is missing required keys 'goal' or 'fitness_level'")

        recommendations = {
            "Weight Loss": {
                "Normal": {"type": "cardio", "duration": 30, "intensity": 0.7},
                "Overweight": {"type": "cardio", "duration": 45, "intensity": 0.8},
                "Obese": {"type": "HIIT", "duration": 60, "intensity": 0.9}
            },
            "Muscle Gain": {
                "Beginner": {"type": "strength training", "duration": 45, "intensity": 0.6},
                "Intermediate": {"type": "strength training", "duration": 60, "intensity": 0.7},
                "Advanced": {"type": "split training", "duration": 75, "intensity": 0.8}
            },
            # Add more recommendations for other goals and fitness levels
        }

        # Adjust recommendations based on user preferences
        if "equipment" in preferences:
            equipment = preferences["equipment"]
            if equipment == "home":
                for goal_recommendations in recommendations.values():
                    for level_recommendation in goal_recommendations.values():
                        if "type" in level_recommendation and " (Home)" not in level_recommendation["type"]:
                            level_recommendation["type"] += " (Home)"
            elif equipment == "gym":
                for goal_recommendations in recommendations.values():
                    for level_recommendation in goal_recommendations.values():
                        if " (Home)" in level_recommendation.get("type", ""):
                            level_recommendation["type"] = level_recommendation["type"].replace(" (Home)", "")

        return recommendations.get(goal, {}).get(fitness_level)
