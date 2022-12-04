num=int(input("Enter a number:"))
if num>1:
    for i in range(2,num//2):
        if(num%i)==0:
            print(num,"is not a prime number")
            break
    else:
        print(num,"is a prime number")
        for num in range(1, 100 + 1):
            count = 0
            for i in range(2, (num // 2 + 1)):
                if (num % i == 0):
                    count = count + 1
                    break
            if (count == 0 and num != 1):
                print(" %d" % num, end='  ')
else:
    print(num,"is neither prime nor composite")