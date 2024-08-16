import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

def get_progress(user_id):
    conn = sqlite3.connect('fitness_tracker.db')
    workouts = pd.read_sql_query('SELECT * FROM workouts WHERE user_id = ?', conn, params=(user_id,))
    nutrition = pd.read_sql_query('SELECT * FROM nutrition WHERE user_id = ?', conn, params=(user_id,))
    conn.close()
    return workouts, nutrition

def plot_progress(workouts, nutrition):
    #plotting the workouts
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.plot(workouts['date'], workouts['calories_burned'], marker='o')
    plt.title('Calories Burned Over Time')
    plt.xlabel('Date')
    plt.ylabel('Calories Burned')
    
    # Plotting nutrition
    plt.subplot(1, 2, 2)
    plt.plot(nutrition['date'], nutrition['calories'], marker='o')
    plt.title('Calories Consumed Over Time')
    plt.xlabel('Date')
    plt.ylabel('Calories Consumed')
    
    plt.tight_layout()
    plt.show()