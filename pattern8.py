# python code reverse hill

num = int(input("Enter the Number of Rows: "))

for row in range(num):
    for col in range(row):
        print(" ",end=" ")
    for col in range(row,num):
        print("X",end= " ")
    for col in range(row,num-1):
        print("X",end=" ")
    
    print()