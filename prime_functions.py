import numpy as np
import pandas as pd

def is_prime(n):
    """For integer n>=2, returns True if n is prime, but False if n is composite."""
    for i in range(2, int(n**0.5)+1):
        if n%i != 0: continue
        if n%i == 0: return False
    return True

def odd_primes_array(m, n):
    """Outputs the ordered linear array of odd primes from integer m (inclusive) to integer n (inclusive)."""
    L = []
    if m%2 == 0:
        m+=1
    for i in range(m,n+1,2):
        if is_prime(i):
            L.append(i)
    L = np.array(L)
    return L

# This array of odd primes will be used to count goldbach pairs with the functions below for each even >= 6.
odd_primes = odd_primes_array(2, 200)

def goldbach_pair_count(n):
    """
    For even n>=6, counts how many pairs of primes sum to n. Order doesn't matter (e.g. 3+7 and 7+3 count as one pair, not two).
    """
    relevant_primes = odd_primes[odd_primes <= n]
    complements = n - relevant_primes

    # We only need to look at the primes and complements which are <= n/2; if a complement <= n/2 is prime
    # then we know it is matched with a prime >= n/2 so there is no need to explicitly consider the primes >= n/2.
    primes_at_most_half_n = relevant_primes[relevant_primes <= n/2]
    complements_at_most_half_n = complements[complements <= n/2]

    # Counts how many of the complements <= n/2 are prime.
    pair_count = len(np.intersect1d(primes_at_most_half_n, complements_at_most_half_n))

    return pair_count

def goldbach_pair_counts_for_interval(m, n):
    """
    Counts how many prime pairs there are for each even number from integer m>=6 (inclusive) to integer n (inclusive).
    Output is a dataframe with columns 'even' and 'goldbach_pair_count'.
    """
    if m%2 == 1:
        m += 1
    evens = list(range(m, n+1, 2))
    goldbach_pair_counts = []
    for even in evens:
        goldbach_pair_counts.append(goldbach_pair_count(even))

    df = pd.DataFrame({'even': evens, 'goldbach_pair_count': goldbach_pair_counts})
    return df

def test_equality():
    assert goldbach_pair_count(6) == 1, "The output should be 1."
    assert goldbach_pair_count(20) == 2, "The output should be 2."
    assert goldbach_pair_count(26) == 3, "The output should be 3."
    assert goldbach_pair_count(30) == 3, "The output should be 3."
    assert goldbach_pair_count(50) == 4, "The output should be 4."
    assert goldbach_pair_count(200) == 8, "The output should be 8."
    assert goldbach_pair_counts_for_interval(6,12).equals(pd.DataFrame({'even':[6,8,10,12], 'goldbach_pair_count':[1,1,2,1]})), "An incorrect dataframe was computed."
    assert goldbach_pair_counts_for_interval(66,77).equals(pd.DataFrame({'even':[66,68,70,72,74,76], 'goldbach_pair_count':[6,2,5,6,5,5]})), "An incorrect dataframe was computed."
    assert goldbach_pair_counts_for_interval(123,130).equals(pd.DataFrame({'even':[124,126,128,130], 'goldbach_pair_count':[5,10,3,7]})), "An incorrect dataframe was computed."
    assert goldbach_pair_counts_for_interval(177,185).equals(pd.DataFrame({'even':[178,180,182,184], 'goldbach_pair_count':[7,14,6,8]})), "An incorrect dataframe was computed."

if __name__ == '__main__':
    test_equality()
    print("All unit tests passed.")