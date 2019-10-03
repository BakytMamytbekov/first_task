'''#1
b = int(input("Enter a number: "))
if b > 0:
    print ("Positive")
if b < 0:
    print ("Negative")


#2
numb = int(input("Enter a number: "))
if numb % 2 == 0 :
    print ("Even")
else:
    print ("Odd")

#3
word = input("Enter Yes or No:")
if word == 'Yes':
    print ("You printed 'YES'")
if word == 'No':
    print ("You printed 'NO'")
else:
    print("You are pothead")

#4
while True:
    x = int(input("Enter a number:"))
    if x == 0: break
print(x)
#5
while True:
    x = str(input("Text something: "))
    if x == "stop": break
    else:
        print (len(x))
'''
