student={
    "name":"Alex",
    "roll_no":"34",
    "register_no":"678123",
    "department":"MCA",
    "semester":2}
student["total_mark"]=85
marks=student["total_mark"]
if marks>=90:
     grade="A"
elif marks>=82:
     grade="B"
elif marks>=75:
     grade="C"
elif marks>=60:
     grade="D"
elif marks>=50:
     grade= "P"
else:
     grade="F"
student["grade"]=grade
del student["roll_no"]
print(student)
