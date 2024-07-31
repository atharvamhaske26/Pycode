a=4
if a>1:
    for i in range(2,(a//2)+1):
        if a%i==0:
            print(a ,"is not a prime no.")
            break
    else:
        print(a ,"is a prime no.")
