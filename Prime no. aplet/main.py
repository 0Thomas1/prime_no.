"""
2021/03/09
prime No.
input any number and the script test if its a prime no.
and
find prime no.s in a range(biggest, smallest, middle)
and
TBC

"""




from pickle import APPEND

def check_input(num):
    """
    check if the input is an integer
    """
    if num //1 != 0:
        print("This is not a prime number.")

def check_prime(num):
    """
    check if the input no. is prime or not,and return boolean expression
    """
    i = 2 
    remain = 1
    if num <= 1:
        return False
    while i < num and remain != 0:
        remain = num % i
        i += 1
    if remain == 0:
        return False
    else:
        return True

def find_prime(lower, higher):
    """
    find all the prime no. in the range and organize them in a list
    """    
    
    num_list = list(range(lower, higher + 1))
    prime_list = []
    
    for i in range(len(num_list)):
        if check_prime(num_list[i]) is True:
            prime_list.append(num_list[i])
        
    return prime_list
    
        

def prime_lst_input():
    """
    prompt user to input lower and upper range
    """
    lower = int(input("What is your lower range?"))
    higher = int(input("What is your upper range?"))
    prime_lst = find_prime(lower, higher)
    return prime_lst


def twin_primes(lst):
    """
    from a sorted prime list, find all twin primes
    """
    twin_prime_lst = []
    for i in range(len(lst)-1):
        if lst[i+1] - lst[i] == 2:
            twin_prime_lst.append(lst[i])
            twin_prime_lst.append(lst[i+1])
            i += 2
            
            print_list(twin_prime_lst)
    
def prime_factor(num): 
    """
    find 2 prime factors of a number
    O(n^2)
    """       
    teli = find_prime(0,num)
    faclst =[]
    for i in range(len(teli)-1):
        j = i
        while j < len(teli)-1 and len(faclst) == 0:
            if teli[i] * teli[j+1] != num:
                j += 1
            else:
                faclst.append(teli[i])
                faclst.append(teli[j+1])
                
    return faclst


def recu(lst, num):
    i = 1
    while lst[0] * lst[i] < num:
        i+=1
    if len(lst) == 3:
        del lst[-1]
        return
    i-=2
    del lst[i+2:]
    del lst[0]
    recu(lst,num)






    