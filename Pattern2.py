#Python code for right angle Triangle pattern
num = int(input("Enter Number Of Rows: "))

for row in range(num):
    for col in range(row+1):
        print("X",end=" ")
    print()
