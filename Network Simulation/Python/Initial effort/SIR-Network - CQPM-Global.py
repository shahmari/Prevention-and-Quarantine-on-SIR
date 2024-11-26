import numpy as np
import random as rm
import matplotlib.pyplot as plt

betta = 1
gamma = 1/5
I0 = 0.1
P_s = 0.35
P_b = 0.35
dim = 333
ND = 50
L = dim
betta_p = (1-P_b)*betta

snod = []
inod = []
rnod = []
tdata = []

adj = {1: 3, 3: 1, 2: 4, 4: 2}
adjx = {1: 0, 3: 0, 2: 1, 4: -1}
adjy = {1: -1, 3: 1, 2: 0, 4: 0}
a = np.zeros((dim, dim), dtype=int)

n_s = 0
while n_s < P_s*(dim**2):
    rmsx = rm.randint(0, dim-1)
    rmsy = rm.randint(0, dim-1)
    if a[rmsx, rmsy] == 0:
        a[rmsx, rmsy] = 1
        n_s += 1
n_i=0
while n_i < I0*(dim**2):
    rmix=rm.randint(0,dim-1)
    rmiy=rm.randint(0,dim-1)
    if a[rmix,rmiy]==0 :
        a[rmix,rmiy]=2
        n_i+=1

Z = a[:, :]
x = np.arange(0, dim+1, 1)
y = np.arange(0, dim+1, 1)
#plt.figure(figsize=(15,15))
#plt.pcolormesh(x, y, Z, cmap="bwr", ec='w', lw=0.06)
#plt.savefig('global')


def pps(n, ND):
    P = n*100/ND
    print("\r\r", end="")
    print("processes {:.2f} %% completed:   ".format(P), end="")
    i = 50*n/ND
    a = 50-int(i)
    b = (int(i)+1)*"🟩"
    c = (a-1)*"⬜️"
    print(b+c, end="")


nd_p = 0
while nd_p < ND:

    pps(nd_p, ND)

    n_L = 0
    while n_L < L**2:
        rmx1 = rm.randint(-1, dim-2)
        rmy1 = rm.randint(-1, dim-2)
        rmx2 = rm.randint(-1, dim-2)
        rmy2 = rm.randint(-1, dim-2)
        if a[rmx1, rmy1] == 2 and a[rmx2, rmy2] == 0:
            if rm.random() < betta_p:
                a[rmx2, rmy2] = 2
        if a[rmx2, rmy2] == 2 and a[rmx1, rmy1] == 0:
            if rm.random() < betta_p:
                a[rmx1, rmy1] = 2
        rmx = rm.randint(0, dim-1)
        rmy = rm.randint(0, dim-1)
        if a[rmx, rmy] == 2 and rm.random() < gamma:
            a[rmx, rmy] = 3
        n_L += 1
    snum = 0
    inum = 0
    rnum = 0
    for i in range(dim):
        for j in range(dim):
            if a[i, j] == 0:
                snum += 1
            if a[i, j] == 2:
                inum += 1
            if a[i, j] == 3:
                rnum += 1
    snod.append(snum)
    inod.append(inum)
    rnod.append(rnum)
    tdata.append(nd_p)
    nd_p += 1
print("\r", "computing successfully completed!   ", 50*"🟦")

plt.figure(figsize=(15, 7))
plt.rcParams.update({'font.size': 10})
plt.title('SIR Network pandemie simulation (Global)')
plt.plot(tdata, inod, 'brown', label='Infectious network')
plt.plot(tdata, snod, 'darkblue', label='Susceptibles network')
plt.plot(tdata, rnod, 'darkgreen', label='Recovereds network')
plt.legend(loc=0)
plt.xlabel('Time(day)')
plt.ylabel('people number')
plt.grid(color='navy', linestyle='--', linewidth=0.5)
plt.savefig('SIR-Network-Global')
