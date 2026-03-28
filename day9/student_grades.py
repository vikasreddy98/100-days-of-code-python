student_scores = {}

student_grades ={}

add_grades= True

while add_grades:
    s_name = input("Enter the Student name: ")
    s_score= int(input("Enter the Student score out of '100': "))
    student_scores[s_name] = s_score
    add_students = input("Do you want to add more students? Type 'yes' or 'no'. \n").lower()

    if add_students == "no":

        for key in student_scores:
            if student_scores[key] > 91 and student_scores[key] < 101:
                student_grades[key] = "Outstanding"
            elif student_scores[key] > 80 and student_scores[key] < 91:
                student_grades[key] = "Exceeds Expectations"
            elif student_scores[key] > 70 and student_scores[key] < 81:
                student_grades[key] = "Acceptable"
            else:
                student_grades[key] = "Fail"

        for key in student_grades:
            print(f"{key}'s Grade is '{student_grades[key]}' with a score of '{student_scores[key]}'")
        add_grades = False