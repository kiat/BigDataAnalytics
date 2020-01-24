
# http://people.duke.edu/~ccc14/sta-663-2016/16A_MCMC.html

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


thetas = np.linspace(0, 1, 200)



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


def target(lik, prior, n, h, theta):
    if theta < 0 or theta > 1:
        return 0
    else:
        return lik(n, theta).pmf(h)*prior.pdf(theta)

n = 100
h = 61
a = 10
b = 10




lik = stats.binom
prior = stats.beta(a, b)
sigma = 0.3

naccept = 0
theta = 0.1
niters = 10000
samples = np.zeros(niters+1)
samples[0] = theta



for i in range(niters):
    theta_p = theta + stats.norm(0, sigma).rvs()
    rho = min(1, target(lik, prior, n, h, theta_p)/target(lik, prior, n, h, theta ))
    u = np.random.uniform()
    if u < rho:
        naccept += 1
        theta = theta_p
    samples[i+1] = theta
nmcmc = len(samples)//2
print("Efficiency = ", naccept/niters)




post = stats.beta(h+a, n-h+b)

plt.hist(samples[nmcmc:], 40, histtype='step', density=True, linewidth=1, label='Prior');
plt.hist(prior.rvs(nmcmc), 40, histtype='step', density=True, linewidth=1, label='Posterior');
plt.plot(thetas, post.pdf(thetas), c='red', linestyle='--', alpha=0.5, label='True posterior')
plt.xlim([0,1]);
plt.legend(loc='upper left')
pass













