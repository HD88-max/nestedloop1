lowerrange = int(input("Give a number: "))
upperrange = int(input("Give another number: "))


for i in range(lowerrange,upperrange+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)