#ask for input
#check if input is negative
#If negative, tell user wrong input
#If positive check greater than 50
#If greater than 50, divide by 2
#If less than 50, tell user number less than 50
num = eval(input("Number:"))
if num < 0:
    print("Wrong input.")
else :
    print("Number is correct")
    if num > 50 :
        num = num/2
        print(num)
    elif num < 50 :
        print("Number is less than 50")
    



