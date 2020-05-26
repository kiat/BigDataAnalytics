#
# Source Code  from https://people.duke.edu/~ccc14/sta-663/EMAlgorithm.html
# And here https://mk-minchul.github.io/EM/
#
import numpy as np

# This is our observed data 
# Coin flips by two people, each 10 times, the first number is the number heads and scond is the number of tails
ys = np.array([(9,1), (8,2), (5,5), (4,6), (7,3)])

thetas = np.array([[0.7, 0.3], [0.5, 0.5]])  # initialize theta_1, 2
# Thetas can be the probabilities for the first and second persons for example. 

pis =np.array([0.5, 0.5])  # prob of choosing coin 1 or coin2 is the same.

tolerance = 0.0001
max_iter = 100

loglike_old = 0
for i in range(max_iter):
    E_c1 = []
    E_c2 = []
    EcY_1 = []
    EcY_2 = []

    loglike_new = 0
    # E-step: calculate probability distributions over possible completions
    for i in range(len(ys)):
        # multinomial (binomial) log likelihood
        log_k1 = np.sum([ys[i]*np.log(thetas[0])])  #  \log [\theta_k^{y_{oi}} (1-\theta_k)^{n - y_{oi}} ]
        log_k2 = np.sum([ys[i]*np.log(thetas[1])])  #  \log [\theta_k^{y_{oi}} (1-\theta_k)^{n - y_{oi}} ]

        # Getting the expectation of c_ik
        denom = np.exp(log_k1) * pis[0] + np.exp(log_k2) * pis[1]
        E_ci1 = np.exp(log_k1) * pis[0] / denom
        E_ci2 = np.exp(log_k2) * pis[1] / denom

        # update complete log likelihood
        # we need it only to check if it converged.
        # we dont need it for updating theta.
        loglike_new += E_ci1 * log_k1 + E_ci2 * log_k2
        E_c1.append(E_ci1)
        E_c2.append(E_ci2)


    # M-step: update values for parameters given current distribution
    for i in range(len(ys)):
        EcY_1.append(E_c1[i] * ys[i] )  # this is a scalar times a vector.
        EcY_2.append(E_c2[i] * ys[i] )

    thetas[0] = np.sum(EcY_1, 0)/np.sum(EcY_1)
    thetas[1] = np.sum(EcY_2, 0)/np.sum(EcY_2)

    print ("Iteration: %d" % (i+1))
    print ("theta_A = [%.2f, %.2f], theta_B = [%.2f, %.2f] , difference in loglike = %.2f" % (thetas[0,0], thetas[0,1], thetas[1,0], thetas[1,1], loglike_new - loglike_old))

    if np.abs(loglike_new - loglike_old) < tolerance:
        break

    loglike_old = loglike_new
