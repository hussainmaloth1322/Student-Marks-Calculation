"""Console program: total and average marks for three subjects."""

def main():
    name = input("Enter student name: ").strip()
    marks = []

    for i in range(1, 4):
        while True:
            try:
                mark = float(input(f"Enter marks in Subject {i}: "))
                if not 0 <= mark <= 100:
                    print("Marks must be between 0 and 100. Try again.")
                    continue
                marks.append(mark)
                break
            except ValueError:
                print("Please enter a numeric mark.")

    total = sum(marks)
    average = total / 3

    print("\n----- Student Marks Report -----")
    print("Student Name:", name)
    print("Total Marks:", total)
    print("Average Marks:", round(average, 2))


if __name__ == "__main__":
    main()
