from src.user.user_profile import UserProfile
from src.assessments.assessments.assessment import Assessment

# Create a new user profile
# Create a new user profile
user_1 = UserProfile(
    user_id=1,
    age=25,
    gender='male',
    name='John Doe',
    email='johndoe@example.com',
    password='password123',
    workout_history=['Push-ups', 'Running'],
    fitness_level='Intermediate',
    fitness_goals='Lose Weight',
    preferences={'duration': 30, 'intensity': 'High', 'frequency': 5},
    medical_conditions=['None'],
    weight=70,
    height=180
)

# Create a new assessment using the user profile
# Create a new assessment using the user profile
user_1_assessment = Assessment(user_profile=user_1)


# Now you can use the attributes from the assessment
print("Weight: ", user_1_assessment.weight) 
print("Height: ", user_1_assessment.height) 
print("Age: ", user_1_assessment.age)    
print("Gender: ", user_1_assessment.gender)
print("Fitness Level: ", user_1_assessment.fitness_level) 
print("Exercise Preferences: ", user_1_assessment.preferences) 
print("Goals: ", user_1_assessment.goals)   
print("BMR: ", user_1_assessment.bmr) 
print("BMI: ", user_1_assessment.bmi) 


user_trainings,user_parameters = user_1.get_personalized_recommendation()
print(f"A plan of {user_parameters}  \n with excercises are {user_trainings}")