#Python Pattern for printing Square

n=  int(input("Enter Number of Rows: "))
for row in range(n):
    for col in range(n):
        print("X",end=" ")
    print()