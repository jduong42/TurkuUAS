import pandas as pd
import numpy as np

# NumPy array creation:
# Convert the Final Grade column into a Numpy Array and calculate the following statistics using NumPy:
# - Mean of final grades.
# - Standard deviation of final grades.
# - Maximum and minimum final grades.

df = pd.read_csv('students.csv')
df['Final Grade'] = df['Grade'] + 10
df.loc[df['Name'] == 'Tom', 'Major'] = 'Chemistry'

final_grades = df['Final Grade'].to_numpy()

mean_grade = np.mean(final_grades)
std_grade = np.std(final_grades)
max_grade = np.max(final_grades)
min_grade = np.min(final_grades)

print(f'Mean: {mean_grade}, Standard Deviation: {std_grade}, Maximum: {max_grade}, Minimum: {min_grade}.')