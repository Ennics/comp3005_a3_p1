# PostgreSQL CRUD Application

This is a Python application that interacts with a PostgreSQL database to perform CRUD (Create, Read, Update, Delete) operations on student records. It includes functions to retrieve all students, add a new student, update a student's email, and delete a student.

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/Ennics/comp3005_a3_p1.git
    ```

2. Install the required dependencies:

    ```bash
    pip install psycopg2
    ```

3. Ensure you have PostgreSQL installed and running on your machine.

4. Create a PostgreSQL database named `students` and run the SQL script `schema.sql` provided in the `sql` directory to create the necessary table and insert initial data.

5. Modify the connection handling code in ./app/database.py at line 11 to correspond to your PostgreSQL server properties.


## Usage

To run the application, navigate to the ./app directory of this project and execute:


    ```bash
    python main.py
    ```

This will start the application, and you will be prompted with a menu to choose from different operations:

1. Display all students
2. Add a new student
3. Update student email
4. Delete a student
5. Exit

Select the appropriate option by entering the corresponding number.

## Demo Video

For a demonstration of the application's functionality, please watch the [demo video](https://youtu.be/X6O3er6fD9E).

## Repository Structure

- `./sql`: Contains SQL scripts for database setup (`schema.sql`).
- `./app`: Contains the Python source code for the application.
  - `main.py`: Main application file containing menu-driven functionality.
  - `database.py`: Module for connecting to the PostgreSQL database and executing CRUD operations.
- `README.md`: This file.
