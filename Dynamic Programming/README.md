# Dynamic Programming

Dynamic Programming is a problem-solving technique that involves breaking a problem into smaller subproblems and solving each subproblem only once. The solutions to subproblems are cached to avoid redundant calculations, which leads to a significant improvement in efficiency.


Techniques to solve Dynamic Programming Problems:
1. Top-Down(Memoization):

Break down the given problem in order to begin solving it. If you see that the problem has already been solved, return the saved answer. If it hasn’t been solved, solve it and save it. This is usually easy to think of and very intuitive, This is referred to as Memoization.

2. Bottom-Up(Dynamic Programming):

Analyze the problem and see in what order the subproblems are solved, and work your way up from the trivial subproblem to the given problem. This process ensures that the subproblems are solved before the main problem. This is referred to as Dynamic Programming. Also known as Tablulation.

### Fibonacci Series

The Fibonacci sequence is a sequence in which each number is the sum of the two preceding ones. Numbers that are part of the Fibonacci sequence are known as Fibonacci numbers, commonly denoted F<sub>n</sub>.

![Fibonacci Series](https://i.imgur.com/BRUwYWc.png)

The calculations as seen in the above images are repeated and to save time and computation, we use memoization to save already computed values and use them when required. However this does increase the space compexity, but eventually leads to a faster results for larger numbers.

The following are the most frequently asked Dynamic Programming problems:
1. Longest Common Subsequence
2. Shortest Common Supersequence
3. Longest Increasing Subsequence problem
4. The Levenshtein distance (Edit distance) problem
5. Matrix Chain Multiplication
6. 0–1 Knapsack problem
7. Partition problem
8. Rod Cutting
9. Coin change problem
10. Word Break Problem

For more information on Dynamic Programming concepts and problems, visit <a href="https://www.programiz.com/dsa/dynamic-programming"> here</a>.
