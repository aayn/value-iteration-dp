
def states(winning_value=100):
    "Gives all possible states in the Gambler's Problem."
    return tuple(range(winning_value + 1))


def actions(s, winning_value=100):
    "Gives possible actions in the given state `s`."
    return tuple(range(min(s, winning_value - s)))


def state_value_max(s, V, ph=0.4, argmax=False):
    A = actions(s)
    max_v = 0
    max_a = 0

    for a in A:
        next_states = p(s, a, ph)
        v = [p * (r + V[s_]) for s_, (p, r) in next_states.items()]
        if v > max_v:
            max_v = v
            if argmax:
                max_a = a

    if argmax:
        return max_a
    return max_v


def p(s, a, ph):
    "Gives p(s', r| s, a)."
    p_success = (ph, reward(s + a))
    p_fail = (1 - ph, reward(s - a))
    return {(s + a): p_success, (s - a): p_fail}


def reward(s_, winning_value=100):
    if s_ == winning_value:
        return 1
    return 0