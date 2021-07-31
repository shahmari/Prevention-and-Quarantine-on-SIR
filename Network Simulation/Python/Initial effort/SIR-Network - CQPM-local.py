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

snod = []
inod = []
rnod = []
tdata = []

adj = {1: 3, 3: 1, 2: 4, 4: 2}
adjx = {1: 0, 3: 0, 2: 1, 4: -1}
adjy = {1: -1, 3: 1, 2: 0, 4: 0}
a = np.zeros((dim, dim, 5), dtype=int)

n_i = 0
while n_i < I0*(dim**2):
    rmix = rm.randint(0, dim-1)
    rmiy = rm.randint(0, dim-1)
    if a[rmix, rmiy, 0] == 0:
        a[rmix, rmiy, 0] = 2
        n_i += 1

n_b = 0
while n_b < P_b*(dim**2)*2:
    rmbx = rm.randint(-1, dim-2)
    rmby = rm.randint(-1, dim-2)
    rmbz = rm.randint(1, 4)
    if a[rmbx+adjx[rmbz], rmby+adjy[rmbz], adj[rmbz]] == 0:
        a[rmbx, rmby, rmbz] = 1
        n_b += 1

n_s = 0
while n_s < P_s*(dim**2):
    rmsx = rm.randint(0, dim-1)
    rmsy = rm.randint(0, dim-1)
    if a[rmsx, rmsy, 0] == 0:
        a[rmsx, rmsy, 0] = 1
        n_s += 1

Z = a[:, :, 0]
x = np.arange(0, dim+1, 1)
y = np.arange(0, dim+1, 1)

Z = a[:, :, 0]
x = np.arange(0, dim+1, 1)
y = np.arange(0, dim+1, 1)

plt.figure(figsize=(50, 50), dpi=200)
plt.pcolormesh(x, y, Z, cmap="bwr", ec='k')
for i in range(dim):
    for j in range(dim):
        if a[i, j, 1] == 1:
            plt.plot([i+0.1, i+0.9], [j+1, j+1], lw=5*(50/dim), c="dimgray")
        if a[i, j, 2] == 1:
            plt.plot([i+1, i+1], [j+0.1, j+0.9], lw=5*(50/dim), c="dimgray")
        if a[i, j, 3] == 1:
            plt.plot([i+0.1, i+0.9], [j, j], lw=5*(50/dim), c="dimgray")
        if a[i, j, 4] == 1:
            plt.plot([i, i], [j+0.1, j+0.9], lw=5*(50/dim), c="dimgray")
plt.savefig('local')


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
        rmx = rm.randint(-1, dim-2)
        rmy = rm.randint(-1, dim-2)
        rmz = rm.randint(1, 4)
        if a[rmx, rmy, 0] == 2 and a[rmx, rmy, rmz] == 0:
            if rm.random() < betta and a[rmx+adjx[rmz], rmy+adjy[rmz], 0] == 0:
                a[rmx+adjx[rmz], rmy+adjy[rmz], 0] = 2
        rmx = rm.randint(0, dim-1)
        rmy = rm.randint(0, dim-1)
        if a[rmx, rmy, 0] == 2 and rm.random() < gamma:
            a[rmx, rmy, 0] = 3
        n_L += 1
    snum = 0
    inum = 0
    rnum = 0
    for i in range(dim):
        for j in range(dim):
            if a[i, j, 0] == 0:
                snum += 1
            if a[i, j, 0] == 2:
                inum += 1
            if a[i, j, 0] == 3:
                rnum += 1
    snod.append(snum)
    inod.append(inum)
    rnod.append(rnum)
    tdata.append(nd_p)
    nd_p += 1
print("\r", "computing successfully completed!   ", 50*"🟦")

plt.figure(figsize=(15, 7))
plt.rcParams.update({'font.size': 10})
plt.title('SIR Network pandemie simulation (local)')
plt.plot(tdata, inod, 'brown', label='Infectious network')
plt.plot(tdata, snod, 'darkblue', label='Susceptibles network')
plt.plot(tdata, rnod, 'darkgreen', label='Recovereds network')
plt.legend(loc=0)
plt.xlabel('Time(day)')
plt.ylabel('people number')
plt.grid(color='navy', linestyle='--', linewidth=0.5)
plt.savefig('SIR-Network.png')

