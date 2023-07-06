def choice_1():
    temp=float(input("\nEnter the temperature:  "))
    print("\nThe user input is {:.2f}".format(temp),"degree Celsius")
    Fahren=(temp*9/5)+32
    print("The {:.2f}".format(temp),"degree Celsius is equal to:  {:.2f}".format(Fahren),"degree Fahrenheit")
def choice_2():
    temp=float(input("\nEnter the temperature:  "))
    print("\nThe user input is {:.2f}".format(temp),"degree Fahrenheit")
    Celsius=(temp-32)*5/9
    print("The {:.2f}".format(temp),"degree Fahrenheit is equal to:  {:.2f}".format(Celsius),"degree Celsius")
def taking_input():
    print("\n\n===================TEMPERATURE CONVERTER====================================")
    print("Type 1(if you want to convert Celsius to Fahrenheit)")
    print("Type 2(if you want to convert Fahrenheit to Celsius)\n")
    choice=input("Enter the choice:  ")
    if choice=="1":
        choice_1()
    if choice=="2":
        choice_2()
     
taking_input()
