
def fact(n):
    f=1
    for i in range(1, n + 1):
        f = f * i
    return f
n=int(input("Enter the number to find factorial: "))
a=fact(n)
print(f"{a} is the factorial of {n}")
