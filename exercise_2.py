print("Enter a string: ",end="")
in1 = input()
in1

for i in range(len(in1)):
    if(in1[i].isupper() == False):
        print(in1[i],end="")

for i in range(len(in1)):
    if(in1[i].isupper() == True):
        print(in1[i],end="")
