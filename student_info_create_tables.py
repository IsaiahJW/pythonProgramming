# Dylan Weakly and Isaiah Wallendorf _ Final COS 2005 Project _ Week 13 Revision
# Part 1 - Created by Dylan Weakly - Lines 3 through 19
import sqlite3

# Connect to the database.
conn = sqlite3.connect('student_info.db')
# Establish a cursor.
cur = conn.cursor()
# Create the table to store student information.
cur.execute('''CREATE TABLE students (
                student_id INTEGER PRIMARY KEY,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                age INTEGER NOT NULL,
                school TEXT NOT NULL,
                class_code TEXT NOT NULL,
                class_name TEXT NOT NULL
                )
''')
# Part 2 - Created by Isaiah Wallendorf - Lines 21 through end
# Data for the 10 students
student_data = [
    (1, 'James', 'Johnson', 18, 'Northwestern', 'COS 2005', 'Python Programming'),
    (2, 'Kyle', 'Smith', 17, 'Northwestern', 'COS 2005', 'Python Programming'),
    (3, 'Alicia', 'Jones', 18, 'Northwestern', 'COS 2005', 'Python Programming'),
    (4, 'Lucy', 'Thompson', 18, 'Northwestern', 'CYS 2005', 'Python Programming'),
    (5, 'Jack', 'Thompson', 17, 'Northwestern', 'CYS 2005', 'Python Programming'),
    (6, 'Luke', 'Miller', 17, 'Northwestern', 'CYS 2005', 'Python Programming'),
    (7, 'Hannah', 'Lewis', 18, 'Northwestern', 'COS 2005', 'Python Programming'),
    (8, 'Jacob', 'Lewis', 18, 'Northwestern', 'COS 2005', 'Python Programming'),
    (9, 'Samantha', 'Davis', 17, 'Northwestern', 'COS 2005', 'Python Programming'),
    (10, 'Tom', 'Wilson', 18, 'Northwestern', 'COS 2005', 'Python Programming')
]
# Insert data into the students table
cur.executemany('''
                        INSERT INTO students (student_id, first_name, last_name, age,
                         school, class_code, class_name)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                        ''', student_data)
# Commit changes to database.
conn.commit()
# Close connection to database.
conn.close()
