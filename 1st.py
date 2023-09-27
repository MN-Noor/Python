choice="1"
while choice =="1":
 operand1=int(input("Enter 1st number"))
 operand2=int(input("Enter 2nd number"))
 operator=input("Enter operator")
 if operator=='+':
   print(operand1+operand2);
 elif operator=='-':
    print(operand1-operand2)
 elif operator=='*':
    print(operand1*operand2)
 elif operator=='/':
    print(operand1/operand2)
 choice=input("1:Continue/n2:quit")
else:
    print("Quitting")