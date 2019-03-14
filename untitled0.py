# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 16:39:13 2019

@author: riccardo.scheda
"""
import matplotlib.pylab as plt
import numpy as np


x = np.random.randn(1000) 
y = x**2 + 0.1 + np.random.randn(len(x)) 

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 4))

ax1.scatter(x, y, marker='^')
ax2.hist(x, alpha=0.5, color='r', density=True, bins=33)
ax3.hist(y, label='transformed data', histtype='step')
ax3.legend()
ax3.set_ylabel("$x^2$ value counts")

fig.tight_layout()

import numpy as np
import scipy as sp

a = np.array([[1,2,3,4,5]])
b = np.array([1,2,3,4,5])
c = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])

print(np.dot(b, b)) # scalar product of b and b
print(sp.dot(b, b))
print(b@b)