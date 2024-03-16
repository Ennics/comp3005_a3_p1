import psycopg2

def connect():
    """
    Establishes a connection to the PostgreSQL database.

    Returns:
        conn (psycopg2.extensions.connection): A connection object if successful, otherwise None.
    """
    try:
        conn = psycopg2.connect(
            dbname="students",
            user="postgres",
            password="pass4n",
            host="localhost",
            port="3001"
        )
        return conn
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)

def getAllStudents():
    """
    Retrieves all student records from the database and prints them.

    Prints:
        Student records in a tabular format.
    """
    conn = connect()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM students")
            rows = cur.fetchall()
            print("Student ID | First Name | Last Name | Email | Enrollment Date")
            print("-" * 60)
            for row in rows:
                print(f"{row[0]:<3} | {row[1]:<10} | {row[2]:<9} | {row[3]:<35} | {row[4]}")
        except psycopg2.Error as e:
            print("Error fetching data:", e)
        finally:
            conn.close()

def addStudent(first_name, last_name, email, enrollment_date):
    """
    Adds a new student record to the database.

    Args:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        email (str): The email address of the student.
        enrollment_date (str): The enrollment date of the student.
    """
    conn = connect()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
                        (first_name, last_name, email, enrollment_date))
            conn.commit()
            print("Student added successfully!")
        except psycopg2.Error as e:
            print("Error adding student:", e)
        finally:
            conn.close()

def updateStudentEmail(student_id, new_email):
    """
    Updates the email address of a student record in the database.

    Args:
        student_id (int): The ID of the student whose email is to be updated.
        new_email (str): The new email address for the student.
    """
    conn = connect()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("UPDATE students SET email = %s WHERE student_id = %s",
                        (new_email, student_id))
            conn.commit()
            print("Email updated successfully!")
        except psycopg2.Error as e:
            print("Error updating email:", e)
        finally:
            conn.close()

def deleteStudent(student_id):
    """
    Deletes a student record from the database.

    Args:
        student_id (int): The ID of the student to be deleted.
    """
    conn = connect()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("DELETE FROM students WHERE student_id = %s",
                        (student_id,))
            conn.commit()
            print("Student deleted successfully!")
        except psycopg2.Error as e:
            print("Error deleting student:", e)
        finally:
            conn.close()
