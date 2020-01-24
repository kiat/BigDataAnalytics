# http://people.duke.edu/~ccc14/sta-663-2016/16A_MCMC.html

import numpy as np

import seaborn as sns


def make_islands(n, low=10, high=101):
    islands = np.random.randint(low, high, n+2)
    islands[0] = 0
    islands[-1] = 0
    return islands

def hop(islands, start=1, niter=1000):
    pos = start
    pop = islands[pos]
    thetas = np.zeros(niter+1, dtype='int')
    thetas[0] = pos
    for i in range(niter):
        # generate sample from proposal distribution
        k = np.random.choice([-1, 1], 1)
        next_pos = pos + k
        # evaluate unnormalized target distribution at proposed position
        next_pop = islands[next_pos]
        # calculate acceptance probability
        p = min(1, next_pop/pop)
        # use uniform random to decide accept/reject proposal
        if np.random.random() < p:
            pos = next_pos
            pop = next_pop
        thetas[i+1] = pos
    return thetas

islands = make_islands(10)
thetas = hop(islands, start=1, niter=10000)

# Generic Metropolis scheme

# data = islands[1:-1]
# data = data/data.sum()
# sns.barplot(x=np.arange(len(data)), y=data)
# pass

# Estimated population proportions by doing hops
data = np.bincount(thetas)[1:]
data = data/data.sum()
sns.barplot(x=np.arange(len(data)), y=data)
pass
