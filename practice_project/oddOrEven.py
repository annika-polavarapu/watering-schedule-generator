def is_odd_or_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
if __name__ == '__main__':
    print(is_odd_or_even(2))
    print(is_odd_or_even(3)) 