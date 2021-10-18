totalMarks = int(input("Enter the full marks"))
sub1 = int(input("Enter the marks of subject 1: "))
sub2 = int(input("Enetr the marks of subject 2: "))
sub3 = int(input("Enetr the marks of subject 3: "))
sub4 = int(input("Enetr the marks of subject 4: "))
sub5 = int(input("Enetr the marks of subject 5: "))

sumOfAllSubject = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (sumOfAllSubject * 100 / totalMarks)
print(percentage,"%")