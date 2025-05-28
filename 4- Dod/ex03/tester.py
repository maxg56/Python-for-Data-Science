from new_student import Student

if __name__ == "__main__":
    # Create a new student instance
    student = Student(first_name="Alice", last_name="Smith", age=20)
    print(student)

    # Mark the student as not alive
    student.die()
    print(student)
