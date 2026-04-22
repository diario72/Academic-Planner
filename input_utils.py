def get_non_empty_input(message):
    while True:
        value = input(message).strip()
        if value == "":
            print("This field cannot be empty.")
        else:
            return value


def get_valid_day(message):
    valid_days = ["monday", "tuesday", "wednesday", "thursday", "friday"]

    while True:
        day = input(message).strip().lower()
        if day in valid_days:
            return day.capitalize()
        else:
            print("Enter a valid day (Monday-Friday).")


def get_valid_time(message):
    while True:
        time = input(message).strip()

        if ":" in time:
            parts = time.split(":")
            if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                hour = int(parts[0])
                minute = int(parts[1])

                if 0 <= hour <= 23 and 0 <= minute <= 59:
                    return time

        print("Enter time in format HH:MM (e.g. 14:30).")
def get_valid_course_name(message):
    while True:
        name = input(message).strip()

        if name == "":
            print("This field cannot be empty.")
        elif not all(word.isalpha() for word in name.split()):
            print("Course name must contain only letters.")
        else:
            return name
def get_valid_semester(message):
    valid_semesters = ["fall", "winter", "spring", "summer"]

    while True:
        semester = input(message).strip().lower()

        if semester in valid_semesters:
            return semester.capitalize()
        else:
            print("Enter a valid semester (Fall, Winter, Spring, Summer).")