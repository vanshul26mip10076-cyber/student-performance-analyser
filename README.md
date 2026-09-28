# Student Performance Analyzer

A Python-based Student Performance Analyzer designed to manage student academic records and perform class-level and subject-wise analysis using fundamental Python programming concepts and algorithms.

## Project Overview

The Student Performance Analyzer is a menu-driven console application developed using Python.

The application allows a teacher to add student records, view all students, search for a student using a unique 6-digit roll number, calculate academic performance, analyze class statistics, and perform subject-wise analysis.

The project demonstrates the practical use of fundamental algorithms, lists, tuples, dictionaries, functions, conditional statements, loops, searching, counting, summation, maximum finding, array reversal, and duplicate removal.

## Problem Statement

Managing student academic records manually can make it difficult to calculate results, compare performance, and obtain useful class-level and subject-level statistics.

This project provides a simple Python-based solution that allows student information and marks to be organized and analyzed through a menu-driven system.

## Objectives

- Store student information and academic marks.
- Use a unique 6-digit roll number to identify each student.
- Display all registered students.
- View complete student performance using the student's roll number.
- Calculate total marks and average marks.
- Assign grades based on average marks.
- Determine student pass/fail status.
- Calculate class statistics.
- Analyze subject-wise performance.
- Find the highest scorer in each subject.
- Calculate subject-wise pass/fail counts.
- Find the top performer.
- Find the lowest performer.
- Demonstrate fundamental array/list algorithms.

## Subjects

The project uses the following subjects:

- Python
- Mathematics
- EVS
- English

Each subject is evaluated out of 100 marks.

## Main Features

### 1. Add Student

The application allows the user to add a new student by entering:

- 6-digit roll number
- Student name
- Python marks
- Mathematics marks
- EVS marks
- English marks

The program validates the roll number and prevents duplicate roll numbers.

### 2. View All Students

Displays all registered students along with:

- Roll number
- Student name

The roll number is used as the unique identifier for each student.

### 3. View Student by Roll Number

A student can be searched using their unique 6-digit roll number.

After entering the roll number, the program displays:

- Roll number
- Student name
- Subject-wise marks
- Total marks
- Average marks
- Grade
- Pass/Fail result

This ensures that individual student performance is accessed using the unique roll number.

### 4. Class Statistics

The application calculates and displays:

- Total number of students
- Class average
- Number of passed students
- Number of failed students

### 5. Subject-wise Analysis

The program calculates the average marks obtained by students in each subject.

This helps identify the overall performance of the class in each subject.

### 6. Subject-wise Highest Scorer

The program compares marks of all students and identifies the highest scorer in each subject.

For every subject, it displays:

- Student name
- Roll number
- Highest marks

### 7. Subject-wise Pass/Fail Count

The program calculates the number of students who passed and failed in each subject.

The pass criteria is:

```text
Marks >= 40  → PASS
Marks < 40   → FAIL
```

### 8. Top Performer

The program compares the average marks of all students and displays the student with the highest overall average.

### 9. Lowest Performer

The program compares the average marks of all students and displays the student with the lowest overall average.

### 10. Array Analysis

The project demonstrates fundamental array/list operations using student performance values.

The operations include:

- Finding the maximum value
- Reversing an array
- Counting elements
- Removing duplicate values
- Finding frequency of values

## Program Menu

```text
=================================================================
             STUDENT PERFORMANCE ANALYZER
=================================================================
1. Add Student
2. View All Students
3. View Student by Roll Number
4. Class Statistics
5. Subject-wise Analysis
6. Subject-wise Highest Scorer
7. Subject-wise Pass/Fail Count
8. Top Performer
9. Lowest Performer
10. Array Analysis
11. Exit
=================================================================
```

## Grade System

The grade is calculated using the student's average marks.

| Average Marks | Grade |
|---|---|
| 90 - 100 | A+ |
| 80 - 89 | A |
| 70 - 79 | B |
| 60 - 69 | C |
| 50 - 59 | D |
| Below 50 | F |

## Pass/Fail System

For overall student performance, a student is considered to have passed when the student scores at least 40 marks in every subject.

If the student scores below 40 in any subject, the overall result is:

```text
FAIL
```

For subject-wise analysis:

```text
Marks >= 40 → PASS
Marks < 40  → FAIL
```

## Roll Number Validation

Every student must have a unique 6-digit numerical roll number.

**Valid Example**

```text
123456
```

**Invalid Examples**

```text
12345
1234567
12A456
```

The program also checks whether the entered roll number already exists.

## Python Concepts Used

This project demonstrates the following Python concepts:

- Variables
- Values and types
- Expressions
- Statements
- Functions
- Parameters and arguments
- Conditional statements
  - if
  - elif
  - else
- for loops
- while loops
- break
- Lists
- Tuples
- Dictionaries
- Searching
- Counting
- Summation
- Maximum finding
- Array reversal
- Duplicate removal
- Frequency counting

## Fundamental Algorithms Used

### Searching

The program searches for students using their unique roll number.

### Summation

Student marks are added together to calculate total marks.

### Average Calculation

The total marks are divided by the number of subjects to calculate the average.

### Maximum Finding

Values are compared sequentially to determine the maximum value.

### Counting

Counting algorithms are used for:

- Number of students
- Pass/fail counts
- Frequency of performance values

### Array Reversal

The performance array is traversed from the last element to the first element.

### Duplicate Removal

Each value is checked before being added to a new list so that duplicate values are removed.

## Data Structures Used

### Lists

Lists are used to store:

- Student records
- Subject marks
- Performance values
- Reversed arrays
- Unique values

### Tuples

A tuple is used to store the fixed subject names.

### Dictionaries

Dictionaries are used to represent student records and to calculate frequency values.

Example student record structure:

```python
{
    "roll_no": "123456",
    "name": "Rahul",
    "marks": [85, 78, 91, 82]
}
```

## Top-Down Design

The program follows a top-down approach.

```text
Student Performance Analyzer
│
├── Student Management
│   ├── Add Student
│   ├── View All Students
│   └── Search by Roll Number
│
├── Performance Calculation
│   ├── Total Marks
│   ├── Average
│   ├── Grade
│   └── Pass/Fail
│
├── Class Analysis
│   ├── Class Average
│   ├── Passed Students
│   └── Failed Students
│
├── Subject Analysis
│   ├── Subject Average
│   ├── Highest Scorer
│   └── Pass/Fail Count
│
├── Overall Performance
│   ├── Top Performer
│   └── Lowest Performer
│
└── Array Analysis
    ├── Maximum
    ├── Reverse
    ├── Counting
    ├── Duplicate Removal
    └── Frequency
```

## Program Flow

```text
Start
  |
  v
Display Main Menu
  |
  v
Enter Choice
  |
  +---- Add Student
  |
  +---- View All Students
  |
  +---- View Student by Roll Number
  |
  +---- Class Statistics
  |
  +---- Subject-wise Analysis
  |
  +---- Subject-wise Highest Scorer
  |
  +---- Subject-wise Pass/Fail Count
  |
  +---- Top Performer
  |
  +---- Lowest Performer
  |
  +---- Array Analysis
  |
  +---- Exit
  |
  v
Display Result
  |
  v
Return to Main Menu
```

## Example Student Performance

Example input:

```text
Roll Number: 123456
Name: Rahul

Python: 85
Mathematics: 78
EVS: 91
English: 82
```

Example output:

```text
Roll Number : 123456
Name        : Rahul

Subject-wise Marks
------------------------------------------------------------
Python            : 85
Mathematics       : 78
EVS               : 91
English           : 82
------------------------------------------------------------
Total Marks : 336
Average     : 84.0
Grade       : A
Result      : PASS
```

## How to Run

### Requirements

- Python 3.x
- Any Python-compatible IDE or terminal

### Run Using IDLE

1. Open the Python file in IDLE.
2. Save the file.
3. Press F5 or select Run → Run Module.
4. The Student Performance Analyzer menu will appear.

### Run Using Terminal

Open the project folder in a terminal and execute:

```bash
python student_performance_analyzer.py
```

## Project Structure

```text
student-performance-analyzer/
│
├── student_performance_analyzer.py
├── README.md
├── .gitignore
│
└── screenshots/
    ├── main_menu.png
    ├── all_students.png
    ├── student_performance.png
    ├── class_statistics.png
    ├── subject_analysis.png
    ├── highest_scorer.png
    └── pass_fail_count.png
```

## Testing

The program can be tested using different types of input.

### Student Registration Testing

- Valid 6-digit roll number
- Invalid roll number
- Duplicate roll number
- Empty student name

### Marks Testing

- Marks between 0 and 100
- Marks below 0
- Marks above 100
- Non-numeric input

### Search Testing

- Existing roll number
- Non-existing roll number
- Invalid roll number

### Performance Testing

- Student with all subjects passed
- Student failing one subject
- Student with high average
- Student with low average

### Analysis Testing

- Class statistics
- Subject averages
- Subject highest scorers
- Subject pass/fail counts
- Top performer
- Lowest performer
- Array operations

## Algorithm Efficiency

Let n represent the number of students.

Most operations that process every student require sequential traversal of the student list.

Therefore, their time complexity is approximately:

```text
O(n)
```

Searching for a student by roll number uses sequential searching.

Worst-case time complexity:

```text
O(n)
```

Finding the highest scorer for a subject also requires checking all students:

```text
O(n)
```

The same applies to subject-wise pass/fail counting:

```text
O(n)
```

## Program Verification

The program uses input validation to reduce incorrect input.

Examples include:

- Checking that the roll number contains exactly 6 digits.
- Checking that roll numbers are unique.
- Checking that marks are between 0 and 100.
- Handling invalid numeric input.
- Checking whether a searched student exists.

## Limitations

- Student data is stored only during program execution.
- Data is not permanently stored in a database or file.
- The application is console-based.
- No graphical user interface is included.
- The project currently supports four fixed subjects.

## Future Scope

The project can be extended in the future with:

- File-based student data storage
- Database integration
- Graphical user interface
- CSV result export
- PDF report generation
- Data visualization
- Additional academic subjects
- Attendance analysis
