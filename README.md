
Program to generate a solution to the n-queens problem for a given n.

  

Uses a randomized greedy descent algorithm to find the global minimum of a graph of costs (number of queens that can attack), and prints all states tested as a solution.

  

States are represented as a tuple of integers with each index of the tuple being a column, and the integer contained the row that the queen in that column is on (as any states with two queens in the same column can be disregarded as a solution). States do not allow duplicates as a state with duplicates would have two queens in the same row, which also cannot be a solution. For example the state (3, 1, 2) represents the board state:

|-|X|-|

|-|-|X|

|X|-|-|

To use simply call n_queens(n) with n as the size of the problem you would like a solution for. An example is available with the code. Note that there is no solution for n = 1 or n = 2, and that this algorithm is not very efficient so large as values of n grow to > 50 things start to slow down.