SUBJECTS = ("Python", "Mathematics", "EVS", "English")


def add_student(students):
    print("\n" + "=" * 60)
    print("                    ADD STUDENT")
    print("=" * 60)

    while True:
        roll_no = input("Enter 6-digit Roll Number: ").strip()

        if len(roll_no) == 6 and roll_no.isdigit():
            break

        print("Roll number must contain exactly 6 digits.")

    for student in students:
        if student["roll_no"] == roll_no:
            print("A student with this roll number already exists.")
            return

    name = input("Enter Student Name: ").strip()

    if name == "":
        print("Name cannot be empty.")
        return

    marks = []

    print("\nEnter marks out of 100:")

    for subject in SUBJECTS:
        while True:
            try:
                mark = int(input(f"{subject}: "))

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break

                print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    student = {
        "roll_no": roll_no,
        "name": name,
        "marks": marks
    }

    students.append(student)

    print("\nStudent added successfully!")


def calculate_total(marks):
    total = 0

    for mark in marks:
        total = total + mark

    return total


def calculate_average(marks):
    if len(marks) == 0:
        return 0

    return calculate_total(marks) / len(marks)


def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def check_pass_fail(marks):
    for mark in marks:
        if mark < 40:
            return "FAIL"

    return "PASS"


def search_student(students, roll_no):
    for student in students:
        if student["roll_no"] == roll_no:
            return student

    return None


def view_all_students(students):
    print("\n" + "=" * 60)
    print("                   ALL STUDENTS")
    print("=" * 60)

    if len(students) == 0:
        print("No student records available.")
        return

    print(f"{'Roll Number':<18}{'Name':<30}")
    print("-" * 60)

    for student in students:
        print(
            f"{student['roll_no']:<18}"
            f"{student['name']:<30}"
        )


def view_student_by_roll(students):
    print("\n" + "=" * 60)
    print("              STUDENT PERFORMANCE")
    print("=" * 60)

    roll_no = input("Enter 6-digit Roll Number: ").strip()

    if len(roll_no) != 6 or not roll_no.isdigit():
        print("\nInvalid Roll Number. Enter exactly 6 digits.")
        return

    student = search_student(students, roll_no)

    if student is None:
        print("\nStudent not found.")
        return

    total = calculate_total(student["marks"])
    average = calculate_average(student["marks"])
    grade = calculate_grade(average)
    result = check_pass_fail(student["marks"])

    print("\n" + "-" * 60)
    print("Student Details")
    print("-" * 60)

    print("Roll Number :", student["roll_no"])
    print("Name        :", student["name"])

    print("\nSubject-wise Marks")
    print("-" * 60)

    for index in range(len(SUBJECTS)):
        print(
            f"{SUBJECTS[index]:<18}: "
            f"{student['marks'][index]}"
        )

    print("-" * 60)
    print("Total Marks :", total)
    print("Average     :", round(average, 2))
    print("Grade       :", grade)
    print("Result      :", result)


def highest_performer(students):
    if len(students) == 0:
        return None

    highest = students[0]

    for student in students:
        if calculate_average(student["marks"]) > calculate_average(
            highest["marks"]
        ):
            highest = student

    return highest


def lowest_performer(students):
    if len(students) == 0:
        return None

    lowest = students[0]

    for student in students:
        if calculate_average(student["marks"]) < calculate_average(
            lowest["marks"]
        ):
            lowest = student

    return lowest


def count_pass_fail(students):
    passed = 0
    failed = 0

    for student in students:
        if check_pass_fail(student["marks"]) == "PASS":
            passed = passed + 1
        else:
            failed = failed + 1

    return passed, failed


def calculate_class_average(students):
    if len(students) == 0:
        return 0

    total_average = 0

    for student in students:
        total_average = total_average + calculate_average(
            student["marks"]
        )

    return total_average / len(students)


def class_statistics(students):
    if len(students) == 0:
        print("\nNo student records available.")
        return

    average = calculate_class_average(students)
    passed, failed = count_pass_fail(students)

    print("\n" + "=" * 60)
    print("                  CLASS STATISTICS")
    print("=" * 60)

    print("Total Students :", len(students))
    print("Class Average  :", round(average, 2))
    print("Passed         :", passed)
    print("Failed         :", failed)


def subject_analysis(students):
    if len(students) == 0:
        print("\nNo student records available.")
        return

    print("\n" + "=" * 60)
    print("                 SUBJECT ANALYSIS")
    print("=" * 60)

    for index in range(len(SUBJECTS)):
        total = 0

        for student in students:
            total = total + student["marks"][index]

        average = total / len(students)

        print(
            f"{SUBJECTS[index]:<18}: "
            f"Average = {average:.2f}"
        )


def subject_highest_scorer(students):
    if len(students) == 0:
        print("\nNo student records available.")
        return

    print("\n" + "=" * 60)
    print("             SUBJECT-WISE HIGHEST SCORER")
    print("=" * 60)

    for index in range(len(SUBJECTS)):
        highest_student = students[0]
        highest_mark = students[0]["marks"][index]

        for student in students:
            mark = student["marks"][index]

            if mark > highest_mark:
                highest_mark = mark
                highest_student = student

        print(
            f"{SUBJECTS[index]:<18}: "
            f"{highest_student['name']} "
            f"({highest_student['roll_no']}) - "
            f"{highest_mark}"
        )


def subject_pass_fail_count(students):
    if len(students) == 0:
        print("\nNo student records available.")
        return

    print("\n" + "=" * 60)
    print("             SUBJECT-WISE PASS/FAIL COUNT")
    print("=" * 60)

    for index in range(len(SUBJECTS)):
        passed = 0
        failed = 0

        for student in students:
            if student["marks"][index] >= 40:
                passed = passed + 1
            else:
                failed = failed + 1

        print(f"\n{SUBJECTS[index]}")
        print("Passed :", passed)
        print("Failed :", failed)


def find_maximum(array):
    if len(array) == 0:
        return None

    maximum = array[0]

    for value in array:
        if value > maximum:
            maximum = value

    return maximum


def reverse_array(array):
    reversed_array = []

    for index in range(len(array) - 1, -1, -1):
        reversed_array.append(array[index])

    return reversed_array


def count_elements(array):
    frequency = {}

    for element in array:
        if element in frequency:
            frequency[element] = frequency[element] + 1
        else:
            frequency[element] = 1

    return frequency


def remove_duplicates(array):
    unique_values = []

    for value in array:
        if value not in unique_values:
            unique_values.append(value)

    return unique_values


def array_analysis(students):
    if len(students) == 0:
        print("\nNo student records available.")
        return

    averages = []

    for student in students:
        average = calculate_average(student["marks"])
        averages.append(round(average, 2))

    print("\n" + "=" * 60)
    print("                    ARRAY ANALYSIS")
    print("=" * 60)

    print("Performance Array:")
    print(averages)

    print("\nMaximum Average:")
    print(find_maximum(averages))

    print("\nReversed Performance Array:")
    print(reverse_array(averages))

    print("\nUnique Performance Values:")
    print(remove_duplicates(averages))

    print("\nFrequency of Performance Values:")

    frequency = count_elements(averages)

    for value in frequency:
        print(
            value,
            "->",
            frequency[value],
            "student(s)"
        )


def show_top_performer(students):
    student = highest_performer(students)

    if student is None:
        print("\nNo student records available.")
        return

    print("\n" + "=" * 60)
    print("                    TOP PERFORMER")
    print("=" * 60)

    print("Name    :", student["name"])
    print("Roll No :", student["roll_no"])
    print(
        "Average :",
        round(calculate_average(student["marks"]), 2)
    )


def show_lowest_performer(students):
    student = lowest_performer(students)

    if student is None:
        print("\nNo student records available.")
        return

    print("\n" + "=" * 60)
    print("                   LOWEST PERFORMER")
    print("=" * 60)

    print("Name    :", student["name"])
    print("Roll No :", student["roll_no"])
    print(
        "Average :",
        round(calculate_average(student["marks"]), 2)
    )


def show_menu():
    print("\n")
    print("=" * 65)
    print("             STUDENT PERFORMANCE ANALYZER")
    print("=" * 65)

    print("1. Add Student")
    print("2. View All Students")
    print("3. View Student by Roll Number")
    print("4. Class Statistics")
    print("5. Subject-wise Analysis")
    print("6. Subject-wise Highest Scorer")
    print("7. Subject-wise Pass/Fail Count")
    print("8. Top Performer")
    print("9. Lowest Performer")
    print("10. Array Analysis")
    print("11. Exit")

    print("=" * 65)


def main():
    students = []

    while True:
        show_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            view_all_students(students)

        elif choice == "3":
            view_student_by_roll(students)

        elif choice == "4":
            class_statistics(students)

        elif choice == "5":
            subject_analysis(students)

        elif choice == "6":
            subject_highest_scorer(students)

        elif choice == "7":
            subject_pass_fail_count(students)

        elif choice == "8":
            show_top_performer(students)

        elif choice == "9":
            show_lowest_performer(students)

        elif choice == "10":
            array_analysis(students)

        elif choice == "11":
            print("\nThank you for using Student Performance Analyzer!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
