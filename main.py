# student record manager

def menu():
    print("1. add student record")
    print("2. view student record")
    print("3. search student record")
    print("4. Total students record")
    print("5. highest marked students record")
    print("6. lowest marked students record")
    print("7. update the stuent record")
    print("8. delete student record")
    print("9. Student statistics record")
    print("10. exit")
    while True:
        try:
            choice = int(input("enter your choice :"))
            if choice == 1:
                add_record()
            elif choice == 2:
                view_record()
            elif choice == 3:
                search_record()
            elif choice == 4:
                total_students()  
            elif choice == 5:
                high_score()
            elif choice == 6:
                lowest_score()  
            elif choice == 7:
                update_record()
            elif choice == 8:
                delete_record()
            elif choice == 9:
                student_statistics()
            elif choice == 10:
                break
            else:
                print("please choose between valid choice (1 - 10)")            
        except ValueError:
            print("please enter the valid input in numeric")
    

        
def add_record():
      question = "y"
      while question == "y":
        name = input("enter the name of the student :").title()
        while True:    
            try:
                age = int(input("enter the age of the student :"))
                break
            except ValueError:
                print("Please enter age as numbers only. ")
        while True:    
            try:
                marks = int(input("enter the marks of the student :"))
                break
            except ValueError:
                print("Please enter marks as numbers only. ")
        with open("students.txt", "a") as f:
            f.write(f"{name},{age},{marks}\n")
        question = input("do you want to add another record? (y/n) :").lower()
        while question != 'y' and question != 'n':
            print("invalid inpput")
            question = input("do you want to add another record? (y/n) :").lower()

def view_record():
    try:
        with open("students.txt","r") as f:
            first_line = f.readline()
            if first_line == "":
                print("no records found")
            else:
                print("name\tage\tmarks\tgrade")
                print('-' * 30)
            f.seek(0)
            for line in f:
                name, age, marks =line.strip().split(",")
                marks = int(marks)
                grade = calculate_grade(marks)
                print(f"{name}\t{age}\t{marks}\t{grade}")
    except FileNotFoundError:
        print("no students record found")

def search_record():
    search_name = input("enter the name of the student :").title()
    with open("students.txt","r") as f:
        found = False
        for line in f:
            name, age, marks =line.strip().split(",")
            if name == search_name:
                found = True
                name, age, marks =line.strip().split(",")
        if not found:
            print("student not found")
        else:
            print("name\tage\tmarks")
            print('-' * 30)
            print(f"{name}\t{age}\t{marks}")

def total_students():
    total_students = 0
    with open("students.txt","r") as f:
        for line in f:
            line.split(",")
            total_students +=1
        print("Total students :", total_students)

def high_score():
    top_student =[]
    highest_marks = 0
    with open("students.txt","r") as f:
        for line in f:
            name, age, marks = line.strip().split(",")
            marks = int(marks)
            if marks > highest_marks:
                highest_marks = marks
                top_student = []
                top_student.append(name)
            elif marks == highest_marks:
                top_student.append(name)
        if top_student== []:
            print("no student record found")
        else:
            print("highest marks :", highest_marks)
            print("top students")
            print("----------------")
            for student in top_student:
                print(student)

def lowest_score():
    with open("students.txt","r") as f:
        first_line = f.readline()
        name, age, marks = first_line.strip().split(",")
        marks = int(marks)
        students = [name]
        lowest_marks = marks
        for line in f:
            name, age, marks = line.strip().split(",")
            marks = int(marks)
            if marks < lowest_marks:
                lowest_marks = marks
                students = [name]
            elif marks == lowest_marks:
                students.append(name)
        if students == []:
            print("no student record found")
        else:
            print("lowest marks :", lowest_marks)
            print("weak students")
            print("----------------")
            for student in students:
                print(student)

def update_record():
    name_to_update = input("Enter name of the student to update the record :").title()
    with open("students.txt", "r") as f:
        record = f.readlines()
        new_record = []
        found = False
        for line in record:
            name, age, marks = line.strip().split(",")
            marks = int(marks)
            if name == name_to_update:
                found = True
                while True:
                    try:
                        new_age = int(input("enter the new age :"))
                        break
                    except ValueError:
                        print("please enter the valid age")
                while True:
                    try:
                        new_marks = int(input("enter the new marks :"))
                        break
                    except ValueError:
                        print("please enter the valid marks")
                new_record.append(f"{name},{new_age},{new_marks}\n")
            else:
                new_record.append(line)
        if not found:
            print("student record not found")
        else:
            with open("students.txt", "w") as f:
                f.writelines(new_record)
            print("student record updated successfully")      
            view_record()

def delete_record():
    name_to_delete = input("Enter name of the student to delete the record :").title()
    with open("students.txt", "r") as f:
        record = f.readlines()
        new_record = []
        found = False
        for line in record:
            name, age, marks = line.strip().split(",")
            marks = int(marks)
            if name == name_to_delete:
                found = True
            else:
                new_record.append(line)
        if not found:
            print("student record not found")
        else:
            with open("students.txt", "w") as f:
                f.writelines(new_record)
            print("student record deleted successfully") 
            view_record()

def calculate_grade(marks):
    if not (0 <= marks <= 100):
        raise ValueError("marks should be between 0 & 100")
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"

def student_statistics():
    total_students = 0
    total_marks = 0
    highest_marks = 0
    lowest_marks = 100
    pass_students = 0
    fail_students = 0
    with open("students.txt", "r") as f:
        for line in f:
            name, age, marks = line.strip().split(",")
            marks = int(marks)
            total_students += 1
            total_marks += marks
            if marks > highest_marks:
                highest_marks = marks
            
            if marks < lowest_marks:
                lowest_marks = marks
            
            grade = calculate_grade(marks)
            if grade in "F":
                fail_students += 1
            else:
                pass_students += 1
        
        if total_students == 0:
            print("no students record found")
            return 
        
        average_marks = round(total_marks / total_students, 2)

        print("=======Students Statistics=======")
        print("Total students :", total_students)
        print("Highest marks :", highest_marks)
        print("Lowest marks :", lowest_marks)
        print("Average marks :", average_marks)
        print("Pass students :", pass_students)
        print("Fail students :", fail_students)
        print("-----------------------")

print(menu())