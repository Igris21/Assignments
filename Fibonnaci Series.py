print("Input -1 to exit the loop")
while True:
    n = int(input("How many terms? "))
    n1,n2 = 0,1
    c = 0
    if n == 1:
       print("Fibonacci sequence upto",n,":")
       print(n1)
    elif n== -1:
        break
    else:
       print("Fibonacci sequence:")
       while c<n:
           print(n1)
           n3 = n1 + n2
           n1 = n2
           n2 = n3
           c += 1
