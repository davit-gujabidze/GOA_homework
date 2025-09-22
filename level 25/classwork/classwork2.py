def Verification(age, experience):
    if age > 18 and experience > 1:
        print("Hired")
    else:
        print("Not Hired")

Verification(20, 2)   # Hired
Verification(17, 3)   # Not Hired
Verification(25, 0)   # Not Hired
