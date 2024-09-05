#python pattern code

num = int(input("Enter Number Of Rows: "))
for row in range(num):
    for col in range(row,num):
        print("X",end=" ")
    print()