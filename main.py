import pandas as pd

# 1. Read the dataset shared on LMS (https://lms.uog.edu.pk/pluginfile.php/1721037/mod_page/content/2/students%20marsks%20C.csv?time=1674542360791)

file = 'students marsks C.csv'

# 2. Display its info/details. Also, display selective columns of data-frame. Extract your info from this dataset and
# display it.

students = pd.read_csv(file)
print(students)
print("-----------------------------------------------------------------------------------")
print(students[['Name', 'Roll No']])
print("-----------------------------------------------------------------------------------")
students_byName = pd.read_csv(file, index_col='Name')
print(students_byName.loc['Syed Ali Hamza Shah'])
print("-----------------------------------------------------------------------------------")

# 3. Find and print its type
print(students_byName.dtypes)
print("-----------------------------------------------------------------------------------")

# 4. Try to print its initial and last 7 rows.
print(students.head(1))
print('.')
print('.')
print('.')
print('.')
print(students.tail(7))
print("-----------------------------------------------------------------------------------")

# 5. Display data-frame's Metadata
students.info()
print("-----------------------------------------------------------------------------------")

# 6. Display its attributes
print(students.index)
print(students.columns)
print(students.axes)
print(students.dtypes)
print(students.size)
print(students.shape)
print(students.ndim)
print(students.T)
print(students.empty)
print(students.values)

print("-----------------------------------------------------------------------------------")

# 7. Update your GPA and Marks correct against your record using iat() fun
students.iat[39, 4] = 3.46
students.iat[39, 3] = 3.46
students.iat[39, 5] = 90.2
students.iat[39, 6] = 81.0
print(students)
print("-----------------------------------------------------------------------------------")

# 8. Update your group TAG in Group Column
students.iat[39, 7] = 'A'
print(students)
print("-----------------------------------------------------------------------------------")

# 9. Insert a column with the name of Section and default value as Column

section = 'Column'
students['Section'] = section
print(students)
print("-----------------------------------------------------------------------------------")

# 10. Insert 2 more columns CGPA Percentage and SGPA Percentage and compute it with computed values

cgpa_perc = (students['CGPA'] / 4) * 100
sgpa_perc = (students['SGPA'] / 4) * 100
students['CGPA %'] = cgpa_perc
students['SGPA %'] = sgpa_perc
print(students)
print("-----------------------------------------------------------------------------------")

# 11. Insert another column as AVG_GPA  by computing Average of  CGPA and SGPA
avg_gpa = (students['CGPA'] + students['SGPA']) / 2
students['AVG GPA'] = avg_gpa
print(students)
print("-----------------------------------------------------------------------------------")

# 12. Drop the column created in last step.
del students['AVG GPA']
print(students)
print("-----------------------------------------------------------------------------------")

# 13. Update (0.00) the Matric Marks column values where its value is less than 80
for i in range(0, len(students)):
    if students.iat[i, 5] < 80:
        students.iat[i, 5] = 0.0

print(students[['Name', 'Matric']])
print("-----------------------------------------------------------------------------------")

# 14. Filter the rows with even index
print(students[0::2])
print("-----------------------------------------------------------------------------------")

# 15. Rename the column Matric to matric Percentage
students.rename(columns={'Matric': 'Matric %'}, inplace=True)
print(students[['Name', 'Matric %']])
print("-----------------------------------------------------------------------------------")

# 16. Randomly create a list/dict of numerical values (15-25) as Midterm marks and Join it with existing Data frame.
import random

midterm_marks = []

for i in range(0, len(students)):
    marks = random.randint(15, 25)
    midterm_marks.append(marks)

students['MidTerm'] = midterm_marks
print(students)
print("-----------------------------------------------------------------------------------")

# 17. Apply group-by clause and fetch the useful info from numerical columns
print(students.groupby(["Name"]).min(numeric_only=True))
print("-----------------------------------------------------------------------------------")

# 18. Print each student's data as single table using row-wise iteration.

for i, j in students.iterrows():
    print(j, "\n")
    print("-----------------------------------------------------------------------------------")

# 19. Sort dataframe on the base of different columns and print its results.

print(students[['Name', 'MidTerm']].sort_values(by=['MidTerm'], ascending=False))
print("-----------------------------------------------------------------------------------")
print(students[['Name', 'SGPA']].sort_values(by=['SGPA'], ascending=False))
print("-----------------------------------------------------------------------------------")

# 20. Convert dataframe into dict and display understandable results.
dict_ = students.to_dict()
print(dict_['Name'])
print("-----------------------------------------------------------------------------------")

# 21. Try to add date-index in data-frame
import datetime

todays_date = datetime.datetime.now().date()
print(todays_date)
index = pd.date_range(todays_date, periods=45, freq='D')
students['Date'] = index
students.set_index('Date', inplace=True)
print(students)
print("-----------------------------------------------------------------------------------")

# 22. Try to count the student with simple CGPAs and SGPAs separately.
print(students.count())
print("-----------------------------------------------------------------------------------")

# 23. Export the updated dataframe to CSV, Excel, JSON.
students.to_csv('updated students marsks C.csv')
students.to_excel('students marsks C in excel.xlsx')
students.to_json('students marsks C in json.json')

# 24. Read other sampel dataset file (https://lms.uog.edu.pk/pluginfile.php/1721037/mod_page/content/2/students%20makrs%20dataset%20B.csv?time=1674542494189) and append it to existing dataframe. (combine, concatenate)
students2 = pd.read_csv('students makrs dataset B.csv')
print(students2)
batch = pd.concat([students, students2], ignore_index=True)
print(batch)
print("-----------------------------------------------------------------------------------")

# 25. As you have 2 different data-frames. Now apply SQL like joins (left, right, inner...) based on their serial numbers.
merged_students = pd.merge(students, students2, on='Sr', how='left')
print(merged_students)
print("-----------------------------------------------------------------------------------")
merged_students = pd.merge(students, students2, on='Sr', how='right')
print(merged_students)
print("-----------------------------------------------------------------------------------")
merged_students = pd.merge(students, students2, on='Sr', how='inner')
print(merged_students)
print("-----------------------------------------------------------------------------------")

# 26. Copy any sample table from your excel file or internet and read with as clipboard like cities population. Dop its undesired columns and specially adjust its index.

# !!! COPY THIS FIRST !!!

# City	Population	State
# New York	8175133	New York
# Los Angeles	3792621	California
# Chicago	2695598	Illinois
# Houston	2100910	Texas
# Phoenix	1445632	Arizona

# !!! THEN REMOVE COMMENTS FROM BELOW CODE

# data = pd.read_clipboard()
# print(data)
# print("-----------------------------------------------------------------------------------")
# data.drop(['State'], axis=1, inplace=True)
# print(data)
# print("-----------------------------------------------------------------------------------")
# data.set_index('City', inplace=True)
# print(data)
# print("-----------------------------------------------------------------------------------")

# 27. Try to build a connection your existing SQL Database and read data as Dataframe. Also try to apply different DML-SQL operation.
from sqlalchemy import create_engine, Column, Integer, String, Table, MetaData

# Connect to the database
engine = create_engine('sqlite:///table.db')

# Create a new table
metadata = MetaData()
table = Table('table_name', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String),
              Column('age', Integer)
              )
metadata.create_all(engine)

# Insert data into the table
conn = engine.connect()
conn.execute(table.insert(), [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 35}
])
import pandas as pd

# Connect to the database
engine = create_engine('sqlite:///table.db')

# Read data from the table
df = pd.read_sql_table('table_name', engine)

# Print the DataFrame
print(df)
# Inserting a new row into the table:
conn = engine.connect()
conn.execute(table.insert().values(name='David', age=40))
# Updating rows in the table:
conn.execute(table.update().where(table.c.name == 'Bob').values(age=35))
# Deleting rows from the table:
conn.execute(table.delete().where(table.c.name == 'Charlie'))
# Selecting rows from the table:
result = conn.execute(table.select().where(table.c.age > 30))
print("-----------------------------------------------------------------------------------")
