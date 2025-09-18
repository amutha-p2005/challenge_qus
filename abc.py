# The student has marks in 5 subjects (each out of 100).
# Store the marks in separate variables .
# Calculate:
# Total Marks
# Percentage
# Grade (based on percentage).
# Grading Rules
# 90–100 → Grade A+
# 80–89 → Grade A
# 70–79 → Grade B
# 60–69 → Grade C
# 50–59 → Grade D
# Below 50 → Grade F                                                                                                                                                Example
# Input (marks stored in variables inside the program):
# sub1 = 78
# sub2 = 85
# sub3 = 92
# sub4 = 74 
# sub5 = 88                                                                                                                                                                     Output:
# Total Marks = 417 / 500
# Percentage = 83.4 %
# Grade = A  





# Marks of 5 subjects (each out of 100)
sub1 = 78
sub2 = 85
sub3 = 92
sub4 = 74
sub5 = 88


total = sub1 + sub2 + sub3 + sub4 + sub5
max_marks = 5 * 100
percentage = (total / max_marks) * 100

if percentage >= 90:
    grade = "A+"

elif percentage >= 80:
    grade = "A"

elif percentage >= 70:
    grade = "B"

elif percentage >= 60:
    grade = "C"

elif percentage >= 50:
    grade = "D"

else:
    grade = "F"
    
print("Total Marks =",total)
print("Percentage =",(percentage))
print("Grade =", grade)
