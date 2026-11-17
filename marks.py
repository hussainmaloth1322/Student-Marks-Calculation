
def calculate_marks():

    name = input("Enter student name: ")

    marks = []

    for i in range(1, 4):

        mark = float(input(f"Enter marks in Subject {i}: "))

        if mark < 0 or mark > 100:
            print("Marks must be between 0 and 100")
            return

        marks.append(mark)

    total = sum(marks)
    average = total / 3

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "F"

    print("\n----- Student Marks Report -----")
    print("Student Name:", name)
    print("Subject Marks:", marks)
    print("Total Marks:", total, "/ 300")
    print("Average:", round(average, 2), "%")
    print("Grade:", grade)


if __name__ == "__main__":
    calculate_marks()
