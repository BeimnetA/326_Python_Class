from tkinter import *
from tkinter import messagebox
from db_user import create_user, get_user, log_workout, log_nutrition
from progress import get_progress, plot_progress

def create_gui():
    def submit_user():
        name = entry_name.get()
        age = int(entry_age.get())
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        goals = entry_goals.get()
        create_user(name, age, weight, height, goals)
        messagebox.showinfo("Success", "User created successfully!")
    
    def login_user():
        name = entry_name.get()
        user = get_user(name)
        if user:
            global current_user_id
            current_user_id = user[0]
            messagebox.showinfo("Success", f"Welcome back, {user[1]}!")
        else:
            messagebox.showerror("Error", "User not found!")
    
    def log_workout_entry():
        date = entry_date.get()
        exercise = entry_exercise.get()
        duration = float(entry_duration.get())
        intensity = entry_intensity.get()
        calories_burned = float(entry_calories_burned.get())
        log_workout(current_user_id, date, exercise, duration, intensity, calories_burned)
        messagebox.showinfo("Success", "Workout logged successfully!")
    
    def log_nutrition_entry():
        date = entry_date.get()
        meal = entry_meal.get()
        calories = float(entry_calories.get())
        carbs = float(entry_carbs.get())
        protein = float(entry_protein.get())
        fats = float(entry_fats.get())
        log_nutrition(current_user_id, date, meal, calories, carbs, protein, fats)
        messagebox.showinfo("Success", "Nutrition logged successfully!")
    
    def show_progress():
        workouts, nutrition = get_progress(current_user_id)
        plot_progress(workouts, nutrition)

    root = Tk()
    root.title("Fitness and Nutrition Tracker")

    Label(root, text="Name:").grid(row=0, column=0)
    entry_name = Entry(root)
    entry_name.grid(row=0, column=1)
    
    Label(root, text="Age:").grid(row=1, column=0)
    entry_age = Entry(root)
    entry_age.grid(row=1, column=1)
    
    Label(root, text="Weight (kg):").grid(row=2, column=0)
    entry_weight = Entry(root)
    entry_weight.grid(row=2, column=1)
    
    Label(root, text="Height (cm):").grid(row=3, column=0)
    entry_height = Entry(root)
    entry_height.grid(row=3, column=1)
    
    Label(root, text="Goals:").grid(row=4, column=0)
    entry_goals = Entry(root)
    entry_goals.grid(row=4, column=1)
    
    Button(root, text="Create User", command=submit_user).grid(row=5, column=0, pady=10)
    Button(root, text="Login", command=login_user).grid(row=5, column=1, pady=10)

    Label(root, text="Date (YYYY-MM-DD):").grid(row=6, column=0)
    entry_date = Entry(root)
    entry_date.grid(row=6, column=1)
    
    Label(root, text="Exercise:").grid(row=7, column=0)
    entry_exercise = Entry(root)
    entry_exercise.grid(row=7, column=1)
    
    Label(root, text="Duration (mins):").grid(row=8, column=0)
    entry_duration = Entry(root)
    entry_duration.grid(row=8, column=1)
    
    Label(root, text="Intensity:").grid(row=9, column=0)
    entry_intensity = Entry(root)
    entry_intensity.grid(row=9, column=1)
    
    Label(root, text="Calories Burned:").grid(row=10, column=0)
    entry_calories_burned = Entry(root)
    entry_calories_burned.grid(row=10, column=1)
    
    Button(root, text="Log Workout", command=log_workout_entry).grid(row=11, column=0, pady=10)
    
    Label(root, text="Meal:").grid(row=12, column=0)
    entry_meal = Entry(root)
    entry_meal.grid(row=12, column=1)
    
    Label(root, text="Calories:").grid(row=13, column=0)
    entry_calories = Entry(root)
    entry_calories.grid(row=13, column=1)
    
    Label(root, text="Carbs (g):").grid(row=14, column=0)
    entry_carbs = Entry(root)
    entry_carbs.grid(row=14, column=1)
    
    Label(root, text="Protein (g):").grid(row=15, column=0)
    entry_protein = Entry(root)
    entry_protein.grid(row=15, column=1)
    
    Label(root, text="Fats (g):").grid(row=16, column=0)
    entry_fats = Entry(root)
    entry_fats.grid(row=16, column=1)
    
    Button(root, text="Log Nutrition", command=log_nutrition_entry).grid(row=17, column=0, pady=10)
    Button(root, text="Show Progress", command=show_progress).grid(row=17, column=1, pady=10)
    
    root.mainloop()

create_gui()