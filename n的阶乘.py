def fact(n):
           value=1
           for count in range(1,n+1):
                value*=count
           return value
n=int(input("Calculate n! Enter n="))
print(n,'!=',fact(n))