

n = int(input())
grades = []

for _ in range(n):
    grades_item = int(input())
    grades.append(grades_item)
   
rounded_grades = [] 
for grade in grades:
        if grade < 38:
            print(grade)
        else:
            next_multiple_of_5 = ((grade // 5) + 1) * 5
            if (next_multiple_of_5 - grade )< 3:
                print(next_multiple_of_5)
            else:
                print(grade)
