# -*- coding: utf-8 -*-

# The sum of Two Numbers
n,m=map(int,input().split())
print("Sum",n+m)

# Odd or Even
n=int(input())
if n%2==0:
  print("Even")
else:
  print("Odd")

# Factorial Calculation
n=int(input())
fact=1
for i in range(1,n+1):
  fact*=i
print("Factorial is:",fact)

# Fibonacci Sequence
n = int(input("how many needed for fibonacci:"))
if n <= 0:
    print("Value should be greater than 0")
elif n == 1:
    print("Fibonacci Sequence: [0]")
elif n == 2:
    print("Fibonacci Sequence: [0, 1]")
else:
    fib= [0, 1]
    for i in range(2, n):
        next= fib[i - 1] + fib[i - 2]
        fib.append(next)
    print("Fibonacci Sequence:", fib)

# Reverse a String
s=input("Input of string:")
print("reverse is:",s[::-1])

# Palindrome check
s= ''.join(s.lower() for s in input("Enter a string: ") if s.isalnum())
if s== s[::-1]:
    print("palindrome")
else:
    print("not a palindrome")

# Leap year check
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
  print(f"{year} is a leap year")
else:
  print(f"{year} is not a leap year")

# Armstrong number
n = int(input("Enter a number: "))
s = str(n)
a = 0
for d in s:
    a += int(d) ** len(s)
if a == n:
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")

def encrypt(text, shift):
  encrypted_text = ""
  for char in text:
    if char.isalpha():
     shift_base = 65 if char.isupper() else 97
     encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
    else:
      encrypted_text += char
  return encrypted_text
def decrypt(encrypted_text, shift):
    return encrypt(encrypted_text, -shift)

# input
message = input("Enter a message: ")
shift = int(input("Enter the shift value: "))

encrypted_message = encrypt(message, shift)
print("Encrypted message:", encrypted_message)

decrypted_message = decrypt(encrypted_message, shift)
print("Decrypted message:", decrypted_message)