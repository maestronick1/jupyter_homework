'''
Step 1: Understand the problem.
Step 2: Devise a plan (translate).
Step 3: Carry out the plan (solve).
Step 4: Look back (check and interpret).
'''

def is_prime(n):
    # Anything that is less than 2 is not prime
    # A prime number is a number that is only divisible by itself
    
    if n < 2:
        return False
    # check each number from 2 to n to see if any number is divisible by n
    
    for i in range(2, n):
        # check to see if n % i == 0
        # one example 15 -> False
        
        if n % i == 0:
            return False
    # Number is prime    
    return True

print(is_prime(2))
print(is_prime(7))
print(is_prime(9))
print(is_prime(10))
print(is_prime(101))
print(is_prime(104))
print(is_prime(-1))


def prime_range_sum(num1, num2):
    # result variable to store additions of prime numbers
    result = 0
    
    # check to see if num1 is less than num2
    if num1 > num2:
        temp = num2
        num2 = num1
        
        num1 = temp
    
    # loop from num1 to num2 (inclusive) and check each number to see if prime
    # if prime, then I want to add the number to my result
    for i in range(num1, (num2 + 1)):
        # pass in i into my is_prime function
        if (is_prime(i)): # 
            result += i 
    
    return result 

print(prime_range_sum(10, 20))
print(prime_range_sum(20, 10))
print(prime_range_sum(20, 29))
print(prime_range_sum(50, 41))
