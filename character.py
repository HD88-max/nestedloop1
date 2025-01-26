string=input("Enter a Name/Word: ")
char=input("Enter a character: ")

i = 0
sum = 0
while i<len(string):
    if string[i] == char:
        sum = sum+1
    i = i+1
print(f"The number of times {char} is repeated is {sum}")