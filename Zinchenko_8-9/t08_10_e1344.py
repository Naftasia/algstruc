def main():

    N = int(input())  
    students = []

    for _ in range(N):
        surname = input().strip()
        name = input().strip()
        student_class = input().strip()
        birthdate = input().strip()
        class_num = int(student_class[:-1])  
        class_letter = student_class[-1]  
        students.append((surname, name, class_num, class_letter, birthdate))
    students.sort(key=lambda x: (x[2], x[3], x[0]))

    for student in students:
        print(f"{student[2]}{student[3]} {student[0]} {student[1]} {student[4]}")

if __name__ == "__main__":
    main()
