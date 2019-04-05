import numpy as np
from gamblers_environment import states, state_value_max
from plotting import policy_plot, value_plot

# Goal state
WINNING_VAL = 100
# Probability of head
PH = 0.4


def value_iteration(theta=1e-10):
    """Returns optimal state-values and optimal policies after
    performing value iteration dynamic programming."""
    S = states(WINNING_VAL)
    V = np.zeros(len(S))
    V[len(S) - 1] = 1.0
    delta = 1.0

    while delta > theta:
        delta = 0.0
        for s in S[1:-1]:
            v = V[s]
            V[s] = state_value_max(s, V, ph=PH)
            delta = max(delta, abs(v - V[s]))
        print(delta)

    pi = np.zeros(len(S))
    for s in range(1, len(S) - 1):
        pi[s] = state_value_max(s, V, ph=PH, argmax=True)

    return V, pi


if __name__ == '__main__':
    V, pi = value_iteration()
    label = f'_{PH}'
    policy_plot(pi, states(winning_value=100), label)
    value_plot(V, label)