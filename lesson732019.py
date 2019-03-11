import numpy as np
import pylab as plt 

rule30 = {"000": "1",
          "001": "1",
          "010": "1",
          "111": "1",
          "011": "0",
          "100": "0",
          "101": "0",
          "110": "0"
         }

def generate_state():
    return "1111111111111111111111111111111111111111111111111111101111111111111111111111111111111111111111111111111111111"

def evolve(stato):
    vecchio = stato[-1] + stato + stato[0]
    nuovo = ""
    for i in range(1,len(vecchio)-1):
        key = vecchio[i-1:i+2]
        nuovo =  nuovo + rule30[key]
    return nuovo

def simulation(nsteps):
    initial_state = generate_state()
    states_seq = [initial_state]
    for i in range(nsteps):
        old_state = states_seq[-1]
        new_state = evolve(old_state)
        states_seq.append(new_state)
        #print(old_state)
        
    return states_seq

matrix=simulation(len(generate_state())) 
res = []
for i in range(0, len(matrix)):
  res.append([int(x) for x in str(matrix[i])]) 
       
res = np.matrix(res)
plt.imshow(res)