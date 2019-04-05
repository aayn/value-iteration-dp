import numpy as np
from gamblers_environment import states, state_value_max


def value_iteration(theta=0.1, winning_value=100):
    S = states(winning_value)
    V = np.random.random(len(S))
    V[len(S)] = 0
    delta = 1

    while delta > theta:
        for s in S[:-1]:
            v = V[s]
            V[s] = state_value_max(s, V)
            delta = max(delta, abs(v - V[s]))

    pi = tuple(map(lambda s: state_value_max(s, V, argmax=True), S[::-1]))
    return pi

