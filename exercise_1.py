print("Enter a string: ",end="")
in1 = input()
x = len(in1) -1

for i in range(len(in1)):
    print(in1[x],end="")
    x -=1