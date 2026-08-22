students = {"Rahul": 85, "Priya": 92, "Amit": 78, "Sneha": 95, "Karan": 88}
high_mark=0
high_stud=""
for k,v in students.items():
    if v>high_mark:
        high_mark=v
        high_stud=k
print(high_stud,high_mark)