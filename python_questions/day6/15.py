# # Create a file containing:
# # Rahul 80
# # Aman 35
# # Priya 92
# # Neha 45
# # Read the file and print only students who scored 50 or above.

# file=open("stud_details.txt","w")
# file.write("Rahul 80\nAman 35\nPriya 92\nNeha 45")
# file=open("stud_details.txt","r")

# details=file.readline()

# for detail in details:
    
#     data=detail.split()
#     if len(data)>=2:
#         names=data[0]
#         marks=int(data[1])
#         if marks>=50:
#             print("marks =",marks)
# file.close()


file = open("stud_details.txt", "w")
file.write("Rahul 80\nAman 35\nPriya 92\nNeha 45")
file.close()
file = open("stud_details.txt", "r")
details = file.readlines()
for detail in details:
    data = detail.split()
    names = data[0]
    marks = int(data[1])
    if marks >= 50:
        print(names, marks)
file.close()