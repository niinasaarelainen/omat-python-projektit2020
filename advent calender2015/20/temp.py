
def vaarinpain():
    number = int(input("Enter a positive integer: "))
    rev = 0
    while(number!=0):
        digit = number%10
        rev = (rev*10)+digit    
        number = number//10
        print(rev, number)
    print(rev)


def prime():
    num = int(input("Enter an integer greater than 1: "))
    isprime = 1 #assuming that num is prime
    for i in range(2, num//2 +1):     # muista: range(2,2) = ei yhtään iteraatiota
        print(i)
        if (num%i==0):
            isprime = 0
            break
    if(isprime==1):
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

def fibo(l1, l2):
    uusi_l2 = l1+ l2
    if (uusi_l2 > 150):
        return
    l1 = l2
    print(uusi_l2)
    fibo(l1, uusi_l2)


def pop():
    numbers = [3,4,1,9,6,2,8]
    print(numbers)
    x = int(input("Enter the position of the element to be deleted: "))
    numbers.pop(x)
    print(numbers)
    numbers.pop()  # poistaa vikan
    print(numbers)

def pali(input):
    print(input, input == input[::-1])


#fibo(1, 1)
#pop()
pali("moi")
pali("moom")