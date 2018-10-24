# http://people.duke.edu/~ccc14/sta-663-2016/16A_MCMC.html

import numpy as np

import seaborn as sns


def make_islands(n, low=10, high=101):
    islands = np.random.randint(low, high, n+2)
    islands[0] = 0
    islands[-1] = 0
    return islands


islands = make_islands(10)
thetas = hop(islands, start=1, niter=10000)



# Main Metroplis implementation 
def metroplis(start, target, proposal, niter, nburn=0):
    current = start
    post = [current]
    for i in range(niter):
        proposed = proposal(current)
        p = min(target(proposed)/target(current), 1)
        if np.random.random() < p:
            current = proposed
        post.append(current)
    return post[nburn:]

# Apply to island hooper - MH
    
target = lambda x: islands[x]
proposal = lambda x: x + np.random.choice([-1, 1])
post = metroplis(1, target, proposal, 2000)
data = np.bincount(post)[1:]
data = data/data.sum()
sns.barplot(x=np.arange(len(data)), y=data)
pass