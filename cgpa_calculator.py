print("CGPA CALCULATOR")
cgpa = float(input("Enter your cgpa score: "))
if cgpa > 5:
    print("INVALID")
elif cgpa >= 4.5 and cgpa <= 5.0:
    print("First class")
elif cgpa >= 4.0 and cgpa < 4.5:
    print("Second class upper")
elif cgpa >= 3.0 and cgpa < 4.0:
    print("Second class lower")
elif cgpa >= 2.5 and cgpa < 3.0:
    print("Third class")
elif cgpa >= 0 and cgpa < 2.5:
    print("Pass")
print(cgpa)