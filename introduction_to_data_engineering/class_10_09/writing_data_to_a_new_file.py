import pandas as pd

df = pd.read_csv('students.csv')
df['Final Grade'] = df['Grade'] + 10
df.loc[df['Name'] == 'Tom', 'Major'] = 'Chemistry'

# Write the modified DataFrame to a new CSV file.
df.to_csv('students_final.csv', index=False)