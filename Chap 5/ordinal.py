list=[]
for i in range(1,10):
    list.append(i)

for x in list:
    if x<=3:
        if x==1:
            print("1st")
        elif x==2:
            print("2nd")
        elif x==3:
            print("3rd")
    else:
        print(str(x)+"st")