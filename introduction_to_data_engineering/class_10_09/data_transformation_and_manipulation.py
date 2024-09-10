import pandas as pd

# Add a new column to the dataframe
df = pd.read_csv('students.csv')
df['Final Grade'] = df['Grade'] + 10
#print(df)

# Filter and sort the data:
# Filter out students who have final grade of 90 or above and display their details.
# Sort the DataFrame based on the Final grade in decending order.
high_grade_students = df[df['Final Grade'] >= 90]
#print(high_grade_students)

sorted_df = df.sort_values(by='Final Grade', ascending=False)
#print(sorted_df)

# Modify a specific column value:
# Change the major of the sudent "Tom" to "Chemistry" in the DataFrame.
df.loc[df['Name'] == 'Tom', 'Major'] = 'Chemistry'
#print(df)

# Group by and aggregate:
# Group the data by the Major column and calculate the average final grade for each major.
avg_grade_by_major = df.groupby('Major')['Final Grade'].mean()
#print(avg_grade_by_major)