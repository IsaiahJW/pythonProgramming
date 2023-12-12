# Dylan Weakly and Isaiah Wallendorf _ Final COS 2005 Project _ Week 14 Revision
# Dylan worked on this part. Since there wasn't much involved, Isaiah will help Dylan
# work on the mainline next week.
import sqlite3

def main():
    # Connect to the database.
    conn = sqlite3.connect('student_info.db')
    # Establish a cursor.
    cur = conn.cursor()
    # Display database rows.
    cur.execute('SELECT * FROM students')
    # Fetch the results of the SELECT statement.
    results = cur.fetchall()
    # Display the database information.
    print('\nHere is the student information pulled from the database:')
    for row in results:
        print(row)
    # Clsoe the database connection.
    conn.close()
if __name__ == '__main__':
    main()