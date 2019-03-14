import numpy as np
import pylab as plt
from scipy.integrate import odeint

from scipy.optimize import curve_fit

def decay_equation(tempo, alfa):
    return 10 * np.exp(-alfa*tempo)

def derivative(y, t):
    return -y

time = np.linspace(0, 10, 20)
y0 = 10.0
# integration of the differential equation: (function, initial condition, time)
yt = odeint(derivative, y0, time) 

fig, ax = plt.subplots()

ax.plot(time, yt, marker = 'o', color = 'k', label = 'exponential')
ax.set_xlabel('$time$', fontsize = 14)
ax.set_ylabel('$y(t)$', fontsize = 14)
ax.set_title('Exponential ODEint', fontsize = 16)
ax.legend(loc = 'best')
#%%

y_obs = yt.ravel() + np.random.randn(len(yt))*0.5

fig, ax = plt.subplots()

ax.plot(time, y_obs, 'bo', label = 'sperimentali')
ax.plot(time, yt, 'k-', label = 'teorici')
ax.legend(loc = 'best')

fit_alfa, var_alfa = curve_fit(decay_equation, time, y_obs, p0=[0.9]) 
std_alfa = np.sqrt(var_alfa)
print(fit_alfa,std_alfa)
fig, ax = plt.subplots(figsize=(8, 8))

ax.plot(time, yt, color='blue', linewidth=1, label='original curve')
ax.plot(time, y_obs, marker='o', label='experimental data');

y_hat = decay_equation(time, fit_alfa)
ax.plot(time, y_hat, '-r', label='fitted curve');
ax.legend(loc = 'best', numpoints = 2)

#%%

import numpy as np
import time

N = 100000 # number of MC events
N_run = 100 # number of runs
Nhits = 0.0 # number of points accepted
pi = np.zeros(N_run) # values of pi

start_time = time.time() # start clock 
for I in range(N_run):
    Nhits = 0.0
    for i in range(N):
        x = np.random.rand()*2-1
        y = np.random.rand()*2-1
        res = x*x + y*y
        if res < 1:
            Nhits += 1.0
    pi[I] += 4. * Nhits/N

run_time = time.time()

print("pi with ", N, " steps for ", N_run, " runs is ", np.mean(pi), " in ", run_time-start_time, " sec")
print("Precision computation : ", np.abs(np.mean(pi)-np.pi))

#%%

import numpy as np
import time


N = 100000 # number of MC events
N_run = 100 # number of runs
Nhits = 0.0 # number of points accepted
pi = np.zeros(N_run) # values of pi



x = np.random.rand(N,N_run)*2-1
y = np.random.rand(N,N_run)*2-1

res = x*x + y*y
if res<1:
    Nhits+=1
    
