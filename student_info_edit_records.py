# Dylan Weakly and Isaiah Wallendorf _ COS 2005 Python Programming Final Project _ Final Revision
# 19 Dec 2023
import sqlite3

# Edit students function created by Dylan.
def edit_student():
    """Edit a specific student record."""
    student_id = int(input("\nEnter the ID of the student to edit: "))

    conn = sqlite3.connect("student_info.db")
    cursor = conn.cursor()

    # Check if the student ID exists
    cursor.execute("SELECT * FROM students WHERE student_id=?", (student_id,))
    student = cursor.fetchone()

    if student is None:
        print("Student not found.")
    else:
        print("\nCurrent Information:")
        print("ID:      ", student[0])
        print("First Name: ", student[1])
        print("Last Name:  ", student[2])
        print("Age:       ", student[3])
        print("School:    ", student[4])
        print("Class Code:     ", student[5])
        print("Class Name:     ", student[6])

        # Get new information from the user
        new_first_name = input("\nEnter new first name: ")
        new_last_name = input("Enter new last name: ")
        new_age = int(input("Enter new age: "))
        new_school = input("Enter new school: ")
        new_class_code = (input("Enter new class code: "))
        new_class_name = input("Enter new class name: ")

        # Update the database with the new information
        cursor.execute('''
            UPDATE students
            SET first_name=?, last_name=?, age=?, school=?, class_code=?, class_name=?
            WHERE student_id=?
        ''', (new_first_name, new_last_name, new_age, new_school, new_class_code, new_class_name, student_id))

        print("\nRecord updated successfully.")

    conn.commit()
    conn.close()

# Main menu created by Isaiah.
def main():


# Initialize the mainline.
if __name__ == "__main__":
    main()