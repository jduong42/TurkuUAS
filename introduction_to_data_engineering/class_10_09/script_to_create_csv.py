# Import the csv module
import csv


# Data for the students table
data = [
    ['Name', 'Age', 'Major', 'Grade'],
    ['John', '23', 'Engineering', '80'],
    ['Jane', '22', 'Science', '90'],
    ['Smith', '25', 'Math', '70'],
    ['Tom', '24', 'Art', '75']
]

# Open the CSV file in write mode and crete it
with open('studnets.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)