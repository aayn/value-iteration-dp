import matplotlib.pyplot as plt


def policy_plot(pi, S, label=''):
    plt.figure(figsize=(20, 20))

    plt.bar(S, pi)
    plt.xlabel('Capital', fontsize=15)
    plt.ylabel('Final policy (stake)', fontsize=15)
    plt.grid()
    plt.savefig(f'data/images/policy{label}.png')
    plt.close()


def value_plot(V, label=''):
    plt.figure(figsize=(20, 20))

    plt.xlabel('Capital', fontsize=15)
    plt.ylabel('Value estimates', fontsize=15)
    plt.plot(V)
    plt.grid()
    plt.savefig(f'data/images/value{label}.png')
    plt.close()