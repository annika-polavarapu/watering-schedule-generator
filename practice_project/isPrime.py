def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    elif number <= 3:
        return True
    
    i = 2
    while i * i <= number: # check the divisibility of each integer up to the square root of the number
         if number % i == 0:
              return False
         i += 1
    return True
         
print (is_prime(9))
print (is_prime(7))
print (is_prime(13))