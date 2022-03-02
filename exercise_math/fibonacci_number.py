print("""
****************
fibonacciiiiii
****************""")
a=1
b=1
fibo= [a,b]
for i in range(10):
    a,b = b,a+b
    fibo.append(b)
print(fibo)