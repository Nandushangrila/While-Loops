number = input("Enter any number:")

digits = len(number)

if digits == 0:
    print("Number of digits is 1!")
else:
    count = 0
   
    temp_num = abs(digits) 

    while temp_num > 0:
        temp_num //= 10  
        count += 1       

    print("Number of digits:",digits)