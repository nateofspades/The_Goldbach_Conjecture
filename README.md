# The Goldbach Conjecture

Dating back to 1742, the Goldbach Conjecture is one of the most famous still-unsolved problems in number theory and mathematics. It predicts that every even number >= 4 can be expressed as the sum of two primes (not necessarily distinct) in at least one way.

For example:

**4** = 2 + 2                 (2 and 2 are prime)
**6** = 3 + 3                 (3 and 3 are prime)
**8** = 3 + 5                 (3 and 5 are prime)
**10** = 3 + 7 = 5 + 5        (3 and 7 are prime; 5 and 5 are prime)
...

I first encountered this problem in the margins of my grade 11 math textbook, and I have since played around with it from time to time. One key advantage in pursuing this problem that I have now versus when I was a high school student is that now I know how to code. This has allowed me, in particular, to create the data visualization found in **visualizing_goldbach_data_graph_6_15000000.png**.

Along the x-axis of the graph in this file you'll find all of the evens from 6 to 15000000. Along the y-axis you'll find what I have called **Goldbach Pair Count**. An even number's Goldbach pair count is defined as the number of unordered pairs of primes which sum to that even number.

For example:

4 = 2 + 2                 ->      **Goldbach pair count** = 1
6 = 3 + 3                 ->      **Goldbach pair count** = 1
8 = 3 + 5                 ->      **Goldbach pair count** = 1
10 = 3 + 7 = 5 + 5        ->      **Goldbach pair count** = 2

Pay special attention to the bottom blue "edge" of the triangle-like shape found in the graph. 

What's relevant and encouraging is that it looks like an approximate straight line that slopes upwards. Why does this matter? It suggests that, if we were to extend this graph to include the evens beyond 15000000, all the way up to infinity, then there would never be a point where the Goldbach pair count drops to 0. In other words, if this is true, then there would be no even number >= 4 which cannot be expressed as the sum of two primes in at least one, and so the Goldbach Conjecture would be true.
