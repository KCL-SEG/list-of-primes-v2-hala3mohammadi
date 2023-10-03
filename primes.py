"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    p = 2
    
    if number_of_primes <= 0: 
        raise ValueError(f"0 or negative numbers are not valid")
    
    while len(list) < number_of_primes:
        flag = True
        for i in range(2, int(p**0.5) + 1):
            if (p%i==0):
                flag = False
                break    
        if flag:
            list.append(p)
        p += 1
    
    return list
