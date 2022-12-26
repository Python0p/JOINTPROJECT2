print(" Choose from the following operations : ")
print("1. + for addition \n2. - for subtraction \n3. * for multiplication \n4. / for dividinng \n5. C for exiting the program ")
while(True):
    c=str(input("Enter the operation : "))
    if(c=="c" or c=="C"):
        break
    a=int(input("Enter the first number : "))
    b=int(input("Enter the Second number : "))
    if(c=="+"):
            print("Addition of the numbers is : ",a+b)
    elif(c=="-"):
            print("Subtraction of the numbers is : ",a-b)
    elif(c=="*"):
            print("Multiplication of the numbers is : ",a*b)
    elif(c=="/"):
            print("After dividing the numbers we get : ",a/b)
    else:
            print("You entered the wrong operator please choose it from the given operations ")
    
