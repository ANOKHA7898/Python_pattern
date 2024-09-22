# Python code for printing Hill


num = int(input("Enter the Number Of Rows:"))

for row in range(num):
    for col in range(row,num-1):
        print(" ",end=" ")
    for col in range(row+1):
        print("X",end=" ")
    for col in range(row):
        print("X",end=" ")

    print()