import numpy as np
import matplotlib.pyplot as plt

'''
Returns the square wave with duty ratio = alpha

A -> amplitude
alpha -> duty ratio
T -> time period
t -> time
'''
def square(A, alpha, T, t): 
    if 0 < t%T < alpha*T:
        return A
    else:
        return 0

'''
DE for RL Circuit

di/dt = f(i, t) = (Vin(t) - iR)/L
'''
def f(i, t, R, L, square_args):
    A, alpha, T = square_args
    return (square(A, alpha, T, t) - i*R)/L

'''
h -> step size
tmax -> maximum t to compute
'''
def rk4(h, tmax, R, L, square_args):
    tvals = [0]
    ivals = [0]

    for j in range(1, int(tmax/h)):
        i = ivals[j - 1]
        t = tvals[j - 1]
        k1 = h*f(i, t, R, L, square_args)
        k2 = h*f(i + h/2, t + k1/2, R, L, square_args)
        k3 = h*f(i + h/2, t + k2/2, R, L, square_args)
        k4 = h*f(i + h, t + k3, R, L, square_args)

        tvals.append(t + h)
        ivals.append(ivals[j - 1] + (k1 + 2*k2 + 2*k3 + k4)/6)

    return np.array(tvals), np.array(ivals)

h = 0.001
tmax = 100
L = 1
R = 0.0001
square_args = [10, 1/2, 2]
t, i = rk4(h, tmax, R, L, square_args)

plt.plot(t, i)
plt.show()
