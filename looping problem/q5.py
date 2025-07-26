def div(a,b):
    for i in range(a,b):
        if i%4==0 and i%5!=0 :
            print(f'{i} is exactly divisible by 4 but not by 5')

a=int(input("enter the range n1:"))
b=int(input("enter the range n2:"))           
div(a,b)  
