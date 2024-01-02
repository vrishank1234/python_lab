#Q2 Write a program to perform arithmetic, Relational operators.
m = float(input("Enter student marks"))

if m >= 80 :
    print("you are eligible for sci")
elif m < 80  :
    print ("you are eligible for commerce")
elif m < 70 and m < 65  :
    print ("you are eligible for arts")
else :
    print ("you have failed")
