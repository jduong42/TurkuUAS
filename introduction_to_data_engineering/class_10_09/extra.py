# Create a Python function or script that:
# Reads a CSV file.
# Adds a column of final grades with a custom number of extra points provided by the user.
# Returns the updated DataFrame.

import csv
import pandas as pd

data = [
    ['Name', 'Age', 'Major', 'Grade'],
    ['John', '23', 'Engineering', '80'],
    ['Jane', '22', 'Science', '90'],
    ['Smith', '25', 'Math', '70'],
    ['Tom', '24', 'Art', '75']
]

with open('extra.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)


extra_points = int(input('Enter the number of extra points: '))
df = pd.read_csv('extra.csv')
df['Final Grade'] = df['Grade'] + extra_points
print(df)
