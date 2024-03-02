from isPrime import is_prime

def test_prime_numbers():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(7) == True
    assert is_prime(11) == True
    assert is_prime(13) == True
    assert is_prime(17) == True
    assert is_prime(19) == True

def test_not_prime_numbers():
    assert is_prime(1) == False
    assert is_prime(4) == False
    assert is_prime(6) == False
    assert is_prime(8) == False
    assert is_prime(9) == False
    assert is_prime(10) == False
    assert is_prime(12) == False
    assert is_prime(14) == False

def test_negative_numbers():
    assert is_prime(-1) == False
    assert is_prime(-2) == False
    assert is_prime(-10) == False
    assert is_prime(-15) == False
    assert is_prime(-20) == False

def test_zero():
    assert is_prime(0) == False
