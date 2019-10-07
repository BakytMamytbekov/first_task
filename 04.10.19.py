'''#1
while True:
    num = int(input("Enter a number: "))
    if num > 7:
        print("Great")
    elif num == 7:
        print("Yes")
    else num <7:
        print("Noo")
    
#2
while True:
    number = int(input("Your number:"))
    if number ==8:
        print("Yes")
    elif number ==7:
        print("Yes")
    elif number >=10:
        print("Yes")
    elif number ==13:
        print("No")
    else:
        print ("No")

#3

while True:
    fav = int(input("Your favorite number:"))
    if fav ==7:
        print("Yes")
    else:
        print("No")
#4
x = int(input("Enter any number: "))
while True:
    if x>0:
        print("Positive")
    else:
        print ("Negative")
        
    if x ==4:
        print("Yes")
    elif x==-10:
        print("No")
    

    if x ==0: break
    x = int(input("Enter any number: "))
#5
my_dict = {"Bekzat":1,
           "Talgat":222,
           "Bakyt":3}
type(my_dict)
if "Talgat" in my_dict:
    print (my_dict["Talgat"])
#not in 
if "Isco" not in my_dict:
    print("Fuck")

# not
x = []
if not x:
    print("1")
else:
    print("2")
# 'not' makes inverse
x = 237
if not x:
    print("1")
else:
    print("2")

#task 1 and/or
numb = int(input("Choose numbers from 1 to 12: "))
if numb == 1 or numb== 2:
    print ("Winter")
if numb == 3 or numb==4 or numb == 5:
    print ("Spring")
if numb == 6 or numb==7 or numb == 8:
    print ("Summer")
if numb == 9 or numb==10 or numb == 11:
    print ("Fall")
#task2
while True:
    b = int(input("Enter your number: "))
    if b>=50 and b<=60:
        print("Congratulations!")
    elif b>60:
        print("Your number is too high")
    elif b<50:
        print("Your number is too low")

'''

            
    
                 
