import numpy as np


def states(winning_value=100):
    "Gives all possible states in the Gambler's Problem."
    return tuple(range(winning_value + 1))


def actions(s, winning_value=100):
    "Gives possible actions in the given state `s`."
    return tuple(range(min(s, winning_value - s) + 1))


def state_value_max(s, V, ph=0.4, argmax=False):
    """Gives the return corresponding to best action if `argmax` is
    False, else gives the best action."""
    A = actions(s)
    returns = []
    
    for a in A[1:]:
        v = ph * V[s + a] + (1 - ph) * V[s - a]
        returns.append(v)
        
    if argmax:
        return np.argmax(np.round(returns, 7)) + 1
    return np.max(returns)