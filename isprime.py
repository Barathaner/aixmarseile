def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def list_primes(N):
    """List all prime numbers less than N."""
    return [i for i in range(2, N) if is_prime(i)]

# Input the number N
N = int(input("Enter the value of N: "))
print(f"Prime numbers less than {N} are:", list_primes(N))
