#python code for printing Sand Watch
num = int(input("Enter the Number of rows: "))

for row in range((num//num)+1 ):
    for col in range(num):
        print("-",end=" ")
    for col in range(num):
        print("-",end=" ")
    print()

for row in range(num):
    for col in range(row):
        print(" ",end=" ")
    for col in range(row,num):
        print("X",end=" ")
    for col in range(row,num-1):
        print("X",end=" ")
    print()

for row in range(num):
    for col in range(row,num-1):
        print(" ",end=" ")
    for col in range(row+1):
        print("X",end=" ")
    for col in range(row):
        print("X",end=" ")
    print()


for row in range((num//num)+1):
    for col in range(num):
        print("-",end=" ")
    for col in range(num):
        print("-",end=" ")
    print()