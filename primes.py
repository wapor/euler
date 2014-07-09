# Helper class to deal with prime numbers.

class Primes:
    def __init__(self, precompute_limit=1000):
        self.Precompute(precompute_limit)

    def as_list(self):
        return self.primes

    def as_set(self):
        if not self.primes_set:
            self.primes_set = set(self.primes)
        return self.primes_set

    def is_prime(self, num):
        if num < self.limit:
            return num in self.as_set()

        if num <= 3:
            if num <= 1:
                return False
            return True

        if not num % 2 or not num % 3:
            return False

        # Small optimization - use precomputed primes as divisors first.
        end = int(num ** 0.5) + 1
        for i in self.primes:
            if i > end:
                return True
            if not num % i:
                return False
        
        # Not enough primes - fall back to usual iteration.
        start = 5 if self.limit < 6 else (self.limit - (self.limit % 6) - 1)
        for i in xrange(start, end, 6):
            if not num % i or not num % (i + 2):
                return False
        return True

    def Precompute(self, limit):
        self.primes = []
        self.limit = limit
        self.primes_set = set()
        sieve = [True] * limit
        sieve[0] = False  # 1 is not prime
        sum = 0
        curr = 1
        while curr < limit:
            # Find next prime by skipping False in the sieve
            while curr <= limit and sieve[curr - 1] == False:
                curr += 1
            if curr > limit:
                break
            sieve[curr - 1::curr] = [False] * (limit / curr)
            self.primes.append(curr)


def RunTests():
    primes = Primes(10)
    assert primes.as_list() == [2, 3, 5, 7]
    assert primes.as_set() == set([2, 3, 5, 7])
    assert primes.is_prime(2)
    assert not primes.is_prime(4)
    assert primes.is_prime(2333)
    assert not primes.is_prime(2343)
    primes.Precompute(7920)
    assert len(primes.as_list()) == 1000
    assert primes.is_prime(6661)
    assert not primes.is_prime(6667)

if __name__ == "__main__":
    RunTests()
