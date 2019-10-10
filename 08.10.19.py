#1
'''
those_numbers=[]
for n in range(1500, 2700):
    if (n%7==0) and (n%5==0):
        those_numbers.append(str(n))
print(','.join(those_numbers))

#2
Celcius = int(input("Enter a temperature in Celcius: "))
Fahrenheit = 9.0/5.0*Celcius+32
print("Temperature: ", Celcius, "Celcius= ", Fahrenheit, "F")
Fahrenheit = int(input("Enter a temperature in Fahrenheit: "))
Celcius = (Fahrenheit-32)*5.0/9.0
print("Temperature: ", Fahrenheit, "Fahrenheit= ", Celcius, "C")

#3
star=5
for s in range(star):
    for t in range(s):
        print('*', end=' ')
    print()
for s in range(star, 0, -1):
    for t in range(t):
        print('*', end=' ')
    print()

#4
number = (1, 2, 3, 4, 5, 6, 7, 8, 9)
odd_numb = 0
even_numb = 0
for n in number:
        if not n % 2:
          even_numb+=1
        else:
          odd_numb+=1
print("Number of even numbers :",even_numb)
print("Number of odd numbers :",odd_numb)

#5
for n in range(7):
    if (n==3 or n==6):
        continue
    print(n, end=' ')
print("n")
'''

                
    
