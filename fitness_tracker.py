import json
import datetime

# Define class for Exercise
class Exercise:
    def __init__(self, name, category, duration_min, intensity):
        self.name = name
        self.category = category
        self.duration_min = duration_min
        self.intensity = intensity
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"{self.timestamp} - {self.name} ({self.category}) - {self.duration_min} min, Intensity: {self.intensity}"

# Define class for User
class User:
    def __init__(self, username, age, weight):
        self.username = username
        self.age = age
        self.weight = weight  # in kg
        self.exercises = []  
        self.goals = {}
    
    def log_exercise(self, exercise):
        self.exercises.append(exercise)
        print("Exercise logged successfully!")

    def delete_last_exercise(self):
        if self.exercises:
            removed_exercise = self.exercises.pop()
            print(f"Deleted last exercise: {removed_exercise}")
        else:
            print("No exercises to delete.")

    def calculate_calories_burned(self):
        """Estimates calories burned based on weight and intensity"""
        total_calories = sum((ex.duration_min * ex.intensity * self.weight * 0.0175) for ex in self.exercises)
        return total_calories

    def calculate_total_duration(self):
        return sum(ex.duration_min for ex in self.exercises)

    def set_goal(self, goal_type, target_value):
        self.goals[goal_type] = target_value 

    def track_progress(self):
        progress = {}
        if 'calories' in self.goals:
            total_calories_burned = self.calculate_calories_burned()
            progress['calories'] = (total_calories_burned / self.goals['calories']) * 100

        if 'duration' in self.goals:
            total_duration = self.calculate_total_duration()
            progress['duration'] = (total_duration / self.goals['duration']) * 100

        return progress

    def view_exercise_history(self):
        if not self.exercises:
            print("No exercises logged yet.")
        else:
            print("\nExercise History:")
            for idx, exercise in enumerate(self.exercises, 1):
                print(f"{idx}. {exercise}")

    def save_progress(self, filename="progress.json"):
        """Saves user data to a JSON file"""
        data = {
            "username": self.username,
            "age": self.age,
            "weight": self.weight,
            "exercises": [
                {
                    "name": ex.name,
                    "category": ex.category,
                    "duration_min": ex.duration_min,
                    "intensity": ex.intensity,
                    "timestamp": ex.timestamp
                }
                for ex in self.exercises
            ],
            "goals": self.goals
        }
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print("Progress saved successfully!")

    def load_progress(self, filename="progress.json"):
        """Loads user data from a JSON file"""
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.username = data["username"]
                self.age = data["age"]
                self.weight = data["weight"]
                self.goals = data["goals"]
                self.exercises = [
                    Exercise(ex["name"], ex["category"], ex["duration_min"], ex["intensity"])
                    for ex in data["exercises"]
                ]
                print("Progress loaded successfully!")
        except FileNotFoundError:
            print("No saved progress found.")

# Function to log an exercise
def log_exercise(user):
    name = input("Enter exercise name: ")
    category = input("Enter category (Cardio, Strength, Flexibility): ")
    duration = int(input("Enter duration (minutes): "))
    intensity = int(input("Enter intensity (1-10): "))
    exercise = Exercise(name, category, duration, intensity)
    user.log_exercise(exercise)

# Function to set a goal
def set_goal(user):
    goal_type = input("Enter goal type (calories/duration): ")
    target_value = int(input("Enter target value: "))
    user.set_goal(goal_type, target_value)
    print("Goal set successfully!")

# Function to track progress
def track_progress(user):
    progress = user.track_progress()
    if progress:
        for key, value in progress.items():
            print(f"Progress towards {key} goal: {value:.2f}%")
    else:
        print("No goals set yet.")

# Main function for user interaction
def main():
    username = input("Enter your username: ")
    age = int(input("Enter your age: "))
    weight = float(input("Enter your weight (kg): "))
    
    user = User(username, age, weight)
    
    while True:
        print("\n--- Fitness Tracking System ---")
        print("1. Log Exercise")
        print("2. View Exercise History")
        print("3. Delete Last Exercise")
        print("4. Set Goal")
        print("5. Track Progress")
        print("6. Save Progress")
        print("7. Load Progress")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")
        if choice == "1":
            log_exercise(user)
        elif choice == "2":
            user.view_exercise_history()
        elif choice == "3":
            user.delete_last_exercise()
        elif choice == "4":
            set_goal(user)
        elif choice == "5":
            track_progress(user)
        elif choice == "6":
            user.save_progress()
        elif choice == "7":
            user.load_progress()
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()