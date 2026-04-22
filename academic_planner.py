import input_utils
import psycopg2

class Course:
    def __init__(self, name, code, semester, day, time):
        self.name = name
        self.code = code
        self.semester = semester
        self.day = day
        self.time = time


conn = psycopg2.connect(
    host="localhost",
    database="academic_planner_db",
    user="postgres",
    password="YOUR_PA$$WORD",
    port="5432"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    id SERIAL PRIMARY KEY,
    course_name TEXT,
    course_code TEXT,
    semester TEXT,
    class_day TEXT,
    class_time TEXT
)
""")

conn.commit()

while True:
    print("\n--- Academic Planner ---")
    print("1. Add Course")
    print("2. View Courses")
    print("3. View Schedule")
    print("4. Search Course")
    print("5. Delete Course")
    print("6. Exit")

    option = input("Choose: ")

    if option == "1":
        name = input_utils.get_valid_course_name("Course name: ")
        code = input_utils.get_non_empty_input("Course code: ")
        semester = input_utils.get_valid_semester("Semester: ")
        day = input_utils.get_valid_day("Class day: ")
        time = input_utils.get_valid_time("Class time: ")

        course = Course(name, code, semester, day, time)

        cursor.execute(
            "INSERT INTO courses (course_name, course_code, semester, class_day, class_time) VALUES (%s, %s, %s, %s, %s)",
            (course.name, course.code, course.semester, course.day, course.time)
        )
        conn.commit()
        print("Course added!")

    elif option == "2":
        cursor.execute("SELECT * FROM courses ORDER BY id")
        courses = cursor.fetchall()

        if not courses:
            print("No courses found.")
        else:
            for course in courses:
                print(f"ID: {course[0]} | {course[1]} | {course[2]} | {course[3]} | {course[4]} | {course[5]}")

    elif option == "3":
        cursor.execute("""
        SELECT course_name, course_code, semester, class_day, class_time
        FROM courses
        ORDER BY class_day, class_time
        """)
        schedule = cursor.fetchall()

        if not schedule:
            print("No schedule found.")
        else:
            for item in schedule:
                print(f"{item[0]} ({item[1]}) | {item[2]} | {item[3]} | {item[4]}")

    elif option == "4":
        keyword = input("Search course: ")
        cursor.execute(
            "SELECT * FROM courses WHERE course_name ILIKE %s",
            ('%' + keyword + '%',)
        )
        results = cursor.fetchall()

        if not results:
            print("No matching courses.")
        else:
            for r in results:
                print(f"ID: {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[5]}")

    elif option == "5":
        course_id = input_utils.get_non_empty_input("Course ID to delete: ")
        cursor.execute("DELETE FROM courses WHERE id = %s", (course_id,))
        conn.commit()
        print("Course deleted!")

    elif option == "6":
        break

    else:
        print("Invalid option")

cursor.close()
conn.close()