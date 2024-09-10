import pandas as pd

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('students.csv')
# Print the DataFrame
print(df)

# Display the first 3 rows of the DataFrame
# First 3 rows: By default, head() shows the first 5 rows; we pass 3 to limit to the first 3
print(df.head(3))

# Print the colum names of the DataFrame
# This shows the column names of the DataFrame
print(df.columns)

# Print the data types of each column
# This tells us the data type of each column(eg. object, int64, float64)
print(df.dtypes)