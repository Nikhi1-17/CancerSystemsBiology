import numpy as np
import copy
import random
def states(n, s=()):
    if n == 0:
        # Base case: If n becomes 0, return the current combination as a tuple
        return (s,)

    si = ()

    if n > 0:
        # Recursively explore two possibilities: Activation and Inactivation
        # Activation
        si = si + states(n - 1, s + ("1",))
        # Inactivation
        si = si + states(n - 1, s + ("0",))
    return si

#n = int (input ("How many nodes in the system ...  "))
n = 4

# Converting tuple to list. The elements inside are tuples as well, we ought to covert those too.
amp = list(states(n))
for i in range(0, len(amp)):
    amp[i] = list(amp[i])

# Now from this list we need to make two copies.
# One is a dictionary to count steps ie. keep track of system as it goes to different nodes.
# The other is converted to a feasible form w.r.t boolean formalism i.e ON --> 1 and OFF --> -1. It is used for calulations

# Making a copy of amp.
camp = copy.deepcopy(amp)

# Dictionary to keep track of ...
for i in range(0, len(amp)):
    amp[i] = "".join(amp[i])
amp = tuple(amp)

tday = {}
tweek = {}

# Conversion to a feasible ising formalism form.
for i in range (0,2**n) :
    for j in range (0,n) :
        camp[i][j] = int((camp[i][j]))
for i in range(0,len(camp)):
    for j in range(0,n):
        if camp[i][j] == 0:
            camp[i][j] = -1
samp = []
for i in range (0,len(camp)) :
  wrap1 = []
  for j in camp[i] :
    wrap2 = []
    wrap2.append (j)
    wrap1.append (wrap2)
  samp.append (wrap1)
"""
em = np.full (shape = (n,n), fill_value= -1)
for i in range (0,n) :
    em [i,i] = 1
"""
em = np.array([[0, -1, -1, 0],
                      [-1, 0, 0, -1],
                      [-1, 0, 0, -1],
                      [0, -1, -1, 0]
                      ])
for ans in samp : # Choosing a node from our possible set of outcomes ...

    for i in range(0, len(amp)): # Clearing records before start of iterative journey
        tweek[amp[i]] = 0
    for ml in range (1,101) : # Start of iterative journey
        disp = ans
        disp = np.array(disp)

        for i in range(0, len(amp)): # Clearing records before start of random walk
            tday[amp[i]] = 0
        for rw in range(1, 101): # Start of random walk
            ss = np.matmul(em, disp)
            for o in range(0, n):
                if ss[o, 0] == 0:
                    ss[o, 0] = disp[o, 0]
                if ss[o, 0] > 0:
                    ss[o, 0] = 1
                if ss[o, 0] < 0:
                    ss[o, 0] = -1
            w = random.randint(1, n)
            ssf = disp
            ssf = np.array(ssf)
            ssf[w - 1, 0] = ss[w - 1, 0]
            #print(f"displaying route ... {ssf}")
            # Counting
            while True :
                for i in range (0,len(samp)) :
                    if np.array_equal(ssf,samp[i]) :
                        tweek[amp[i]] = tweek[amp[i]] + 1
                        break
                break
            # Re initialising
            disp = ssf
            disp = np.array(disp)
            #print (f"tweek)
        # Tallying results after each random walk. Below is summation after multiple random walks.
        for i in range(0, len(amp)):
            tweek[amp[i]] = tweek.get(amp[i]) + tday.get(amp[i])
    print (f"For start point of {ans}, we have ... ")
    print (tweek)
    print ()


