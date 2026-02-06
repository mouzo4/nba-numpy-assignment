# NBA NumPy Assignment

import numpy as np

# Load column names
with open("NBA_Column_Names.txt", "r") as f:
    columns = f.read().strip().split(",")

# Load player stats data
data = np.genfromtxt(
    "NBA_Player_Stats.tsv",
    delimiter="\t",
    skip_header=1
)

# Simple check
print("Data loaded")
print("Number of rows:", data.shape[0])
print("Number of columns:", data.shape[1])

# Example calculations (will expand later)

# Minutes played column index (example)
MIN_INDEX = 6
POINTS_INDEX = 26

minutes = data[:, MIN_INDEX]
points = data[:, POINTS_INDEX]

# Avoid division by zero


# Field Goal Accuracy

FG_MADE_INDEX = 7
FG_ATTEMPT_INDEX = 8

fg_made = data[:, FG_MADE_INDEX]
fg_attempts = data[:, FG_ATTEMPT_INDEX]

fg_accuracy = np.where(fg_attempts > 0, fg_made / fg_attempts, 0)

print("Average field goal accuracy:", np.mean(fg_accuracy))

points_per_minute = np.where(minutes > 0, points / minutes, 0)

print("Average points per minute:", np.mean(points_per_minute))

