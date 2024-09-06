#python to print a Diamond pattern

num = int(input("Enter Number Of Rows: "))

for row in range(num-1):
    for col in range(row,num-1):
        print(" ",end=" ")
    for col in range(row+1):
        print("X",end=" ")
    for col in range(row):
        print("X",end=" ")
    print()

for row in range(num):
    for col in range(row):
        print(" ",end=" ")
    for col in range(row,num):
        print("X",end=" ")
    for col in range(row,num-1):
        print("X",end =" ")
    print()