# Write a program that asks the user for a number (integer only) and prints the sum of its digits

def sumofdigits(text):
    s = 0
    for c in text:
        s = s + int(c)
    return s

print (sumofdigits(input('input an integer: ')))