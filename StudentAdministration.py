

def print_instructions():
    print("Please select an action")
    print("1. Add a student")
    print("2. Print all students")
    print("3. Print all majors")
    print("4: Look up a student’s major using their name")
    print("5. Quit")

def get_user_input():
    global user_input
    user_input = int(input("Selection: "))
    return user_input

def print_students(all_students):
    print("The names of all students are:")
    print(all_students)

def print_majors(all_majors):
    print("The names of all majors are:")
    print(all_majors)

def get_student_major_by_name(student_name, all_students, all_majors):
    index = 0
    for i in all_students:
        if i != student_name:
            index = index + 1
        else:
            break
    student_major = all_majors[index]
    print("Major for", student_name, "is:", student_major)

def main():
    all_students: list[str] = ['Ellen', 'Sam', 'Victoria', 'Rachel', 'Austin']
    all_majors: list[str] = ['Information Library Science', 'English', 'Computer Science', 'History', 'Chemistry']
    print_instructions()
    get_user_input()
    while user_input != 5:
        if user_input == 1:
            all_students.append(input("Name of Student to Add: "))
            all_majors.append(input("Student's Major: "))
            print_instructions()
            get_user_input()
        if user_input == 2:
            print_students(all_students)
            print_instructions()
            get_user_input()
        if user_input == 3:
            print_majors(all_majors)
            print_instructions()
            get_user_input()
        if user_input == 4:
            student_name = input("Student Name: ")
            get_student_major_by_name(student_name, all_students, all_majors)
            print_instructions()
            get_user_input()
    print("Done")

main()























