from itertools import combinations
import random
def greedy_descent(initial_state):
    """Returns the list of states to get to a local minimum"""
    
    result = []

    while True:
        # ensures states with the same cost are taken FIFO
        costs = [(cost(state[1]), state[0], state[1]) for state in enumerate(neighbours(initial_state))]
        
        next_state = min(costs)[2]
        result.append(initial_state)
        
        # Break if minimum found
        if cost(next_state) >= cost(initial_state):
            break 

        initial_state = next_state

    return result

def swap_two(state, pos1, pos2):
    """returns a new tuple of the given state but with the two indexes swapped"""
    return tuple([state[pos1] if k == pos2 else state[pos2] if k == pos1 else state[k] for k in range(len(state))])

def neighbours(state):
    """returns a list of all states one move away from the given state""" 
    results = set()
    for i, col in enumerate(state):
        for j, to_swap in enumerate(state):
            if i != j:
                results.add(swap_two(state, i, j))
        
    return sorted(list(results))

def can_attack(q1, q2):
    """returns true if the two given queens are on a diagonal ie. have an absolute gradient of one"""
    # subtract the points to get an x and y value
    x, y = abs((q1[0] + 1) - (q2[0] + 1)), abs(q1[1] - q2[1])
    # return true if the gradient is one
    return y / x == 1

def cost(state):
    """returns the number of combinations of queens that can attack each other."""
    return len([c for c in combinations(enumerate(state), 2) if can_attack(c[0], c[1])])

def random_state(n):
    """generates a random state of size n"""
    return tuple(random.sample(range(1,n+1), n))

def n_queens(n):
    """Prints a solution to an n_queens problem of size n, showing all queried states and restarts"""
    initial_state = random_state(n)
    while True:
        states = greedy_descent(initial_state)
        for state in states:
            print(state)

        # Break if solution found (cost = 0, no queens can attack)
        if cost(states[-1]) == 0:
            print("SOLUTION FOUND")
            break 
        # Try again with another random state
        else:
            print("RESTART")
            initial_state = random_state(n)

n_queens(100)
