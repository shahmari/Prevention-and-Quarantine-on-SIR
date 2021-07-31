import numpy as np
import random as rm
import matplotlib.pyplot as plt

betta = 1
gamma = 1/5
I0 = 0.01
dim = 50
L = dim


snod = []
inod = []
rnod = []
tdata = []

adj = {1: 3, 3: 1, 2: 4, 4: 2}
adjx = {1: 0, 3: 0, 2: 1, 4: -1}
adjy = {1: -1, 3: 1, 2: 0, 4: 0}

def intial_state(P_s):
    a=np.zeros((dim,dim),dtype=int)

    n_s=0
    while n_s < P_s*(dim**2):
        rmsx=rm.randint(0,dim-1)
        rmsy=rm.randint(0,dim-1)
        if a[rmsx,rmsy]==0 :
            a[rmsx,rmsy]=1
            n_s+=1

    n_i=0
    while n_i < I0*(dim**2):
        rmix=rm.randint(0,dim-1)
        rmiy=rm.randint(0,dim-1)
        if a[rmix,rmiy]==0 :
            a[rmix,rmiy]=2
            n_i+=1
    return a


def simulation(P_b, P_s):
    a = intial_state(P_s)
    betta_p = (1-P_b)*betta
    #snod=[]
    #inod=[]
    rnod = []
    #tdata=[]
    nd_p = 0
    while nd_p < 200:

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
        #snum=0
        #inum=0
        rnum = 0
        for i in range(dim):
            for j in range(dim):
                #if a[i,j,0]==0:
                #snum+=1
                #if a[i,j,0]==2:
                #inum+=1
                if a[i, j] == 3:
                    rnum += 1
        #snod.append(snum/(dim**2))
        #inod.append(inum/(dim**2))
        rnod.append(rnum/(dim**2))
        #tdata.append(nd_p)
        nd_p += 1
    return rnod[-1]

def pps(n,ND) :
    P=n*100/ND
    PP= "{:.2f}".format(P)
    print("\r",end="")
    print("processes",PP,"% completed:   ",end="")
    i=50*n/ND
    a=50-int(i)
    b=(int(i)+1)*"🟩"
    c=(a-1)*"⬜️"
    print(b+c,end="")


psdata = [0, 0.2, 0.4, 0.6, 0.8]
pbdata = [[], [], [], [], []]
rdata = [[], [], [], [], []]
step = ["First", "Second", "Third", "Fourth", "Fifth"]
for i in range(5):
    n_pb = 0
    while n_pb < 0.99:
        pps(n_pb, 0.99)
        rdata[i].append(simulation(n_pb, psdata[i]))
        pbdata[i].append(n_pb)
        n_pb += 0.01
    print("\r", step[i], "step successfully completed!   ", 50*"🟦")
print("Processition Done!")

plt.figure(figsize=(15, 7))
plt.rcParams.update({'font.size': 10})
plt.title('Global interaction against the density of quarantine Pb')
plt.plot(pbdata[0], rdata[0], label='Ps=0')
plt.plot(pbdata[1], rdata[1], label='Ps=0.2')
plt.plot(pbdata[2], rdata[2], label='Ps=0.4')
plt.plot(pbdata[3], rdata[3], label='Ps=0.6')
plt.plot(pbdata[4], rdata[4], label='Ps=0.8')
plt.legend(loc=0)
plt.xlabel('density of quarantine')
plt.ylabel('density of Recovereds')
plt.grid(color='navy', linestyle='--', linewidth=0.5)
plt.savefig('R(inf)-Pb global')
