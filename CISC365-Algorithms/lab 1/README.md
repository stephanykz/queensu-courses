# Faster Collatz
This project is to create faster test code for the collatz conjecture, by optimizing the algorithms.

## Collatz Conjecture
The [collatz conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture) is a conjecture in mathematics that concerns a sequence defined as follows: start with any positive integer n. Then each term is obtained from the previous term as follows: if the previous term is even, the next term is one half the previous term. If the previous term is odd, the next term is 3 times the previous term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.

Collatz conjecture defined the following iterative sequence for the set of positive integers:
```
n → n/2 (n is even)
n → 3n + 1 (n is odd)
```
For example, using the rule above and starting with 13, we generate the following sequence:
```
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
```
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 

**It is believed (but hasn't been proved) that for any positive starting integers, the loop will terminate and finish at 1.**

## Project Objects
Reducing times of iteration to accelerate the test

### Attempt 1. Reducing times of iteration by eliminating repetitive  work

If the loop comes across any value that haves been previously checked, then we don't need to finish the loop -- we know that it's going to terminate.

For example, if we run the loop with initial value 4 and it terminates, then if we start it again with initial value 8, the first iteration will divide x by 2, giving 4, and we know that starting at 8 will also terminate, without doing much work. 
```
8 → 4 → 2 → 1
```

_Idea 1_ 
Create a list that stores the previous checked values. The loop terminates whenever it comes to a listed value.

_Idea 2_ 
Run the test of conjecture with consecutive integers. The loop terminates whenever it comes to a value smaller than the starting value.(i.e "smaller" means "checked" for consecutive test

### Attempt 2. Reducing times of iteration by observing the inner structure of the collatz algorithm

When the function iterates over an odd number, it yields an even number (because 3x+1 is always even if x is odd). If it iterates over an even number it can yield either another even number or an odd number. 

Therefore we can modify the function in following way:
```
n → n/2 (n is even)
n → (3n + 1)/n (n is odd)
```
Here we reduce the next two steps into one when the loop comes to a odd value.

