### X_Fit Project Documentation

This document provides an overview of the X_Fit project, a fitness application designed to provide personalized workout recommendations and track user progress.
1. Introduction
Purpose: X_Fit aims to assist users in achieving their fitness goals by providing personalized workout plans and tracking their progress.
Goals and Objectives:
Generate individualized workout plans based on user assessments, fitness levels, goals, and preferences.
Implement the Optimum Performance Training (OPT) model to structure workout phases and progression.
Utilize machine learning and rule-based systems for workout recommendations.
Track user progress and adapt workout plans accordingly.
Offer an intuitive and user-friendly interface.
2. Project Overview
Architecture:
X_Fit follows a modular structure with distinct components responsible for different functionalities.
Main Components:
User: Handles user registration, authentication, and profile management.
UserProfile: Stores user-specific information like fitness level, goals, preferences, and workout history.
Assessment: Conducts initial assessments to determine fitness level and recommend appropriate workout phases.
OPTPhaseAssessment: Implements assessments for each phase of the OPT model (Strength, Stabilization, Power).
AssessmentManager: Manages and runs various assessment phases, generating reports with scores.
FitnessPhase: Abstract class defining the structure for different workout phases (StrengthEndurance, StabilizationEndurance, Power).
TrainingParameters: Defines parameters for each type of training within a phase (e.g., reps, sets, tempo).
FitnessPlan: Generates and updates personalized fitness plans based on recommendations and user preferences.
HealthMetrics: Records and analyzes user health metrics like weight, height, BMI, and body fat percentage.
Rules: Implements rule-based logic for workout recommendations.
ML_Model: Houses machine learning models for more advanced personalized recommendations. (Currently under development)
Dependencies:
Python 3.x
pandas
scikit-learn
pymongo
3. Installation Instructions
Clone the repository: git clone https://github.com/your-username/X_Fit.git
Navigate to the project directory: cd X_Fit
Install required dependencies: pip install -r requirements.txt
4. Usage Guide
Workflow:
User Registration and Profile Creation: The user registers and provides information about their fitness level, goals, and preferences.
Initial Assessment: The system conducts assessments to determine the user's current fitness level and recommend suitable workout phases.
Workout Plan Generation: A personalized workout plan is generated based on assessment results, goals, and preferences, potentially utilizing the OPT model and rule-based systems.
Workout Tracking and Progress Monitoring: Users log their workouts, and the system tracks their progress, making adjustments to the plan as needed.
Interface:
The project currently uses a command-line interface for user interaction and data input. A graphical user interface is planned for future development.
5. Configuration
The configuration options for the project are currently limited and primarily involve database connection details, located in the utils/database_utils.py module.
6. API Documentation
X_Fit does not currently have an API implemented.
7. Troubleshooting
For any issues encountered, please refer to the project's GitHub repository for bug reports and solutions.
8. Contributing Guidelines
The project is currently not open source.
9. License
The project's license is not yet defined.
10. Acknowledgments
We would like to thank the developers of the libraries used in this project, including pandas, scikit-learn, and pymongo.
11. References
Optimum Performance Training (OPT) Model: https://www.nasm.org/
12. Appendix
The appendix may include additional technical details and information about machine learning models used in future versions.