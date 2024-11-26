# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
import matplotlib.pyplot as plt


# %%
file_list=[]
for i in range(50):
    file_list.append('Ps-Pb{}.csv'.format(i))
rdata=np.ndarray((50,50,50))
rd_mean=np.ndarray((50,50))
for i in range(50):
    file=np.loadtxt(open(file_list[i],'r'), dtype='str', delimiter=",")
    for j in range(50):
        for k in range(50):
            rdata[j,k,i]=int(file[k,j])
for i in range(50):
    for j in range(50):
        rd_mean[j,i]=np.mean(rdata[i,j])    


# %%
for i in range(50):
    for j in range(50):
        rd_mean[i,j]-=(j)*0.02*10000


# %%
plt.figure(dpi=150,figsize=(12,10))
Pslist=np.linspace(0,0.99,50)
Pblist=np.linspace(0,1,50)
c=plt.pcolormesh(Pslist,Pblist,rd_mean, cmap="plasma")
plt.title('density of Quarantine - density of Prevention (Local)')
plt.colorbar(c)
plt.xlabel('density of Prevention (Ps)')
plt.ylabel('density of Quarantine (Pb)')
plt.savefig('Ps-Pb')


# %%
plt.figure(dpi=150,figsize=(12,10))
plt.xlim((0,0.5))
plt.ylim((0,0.5))
Pslist=np.linspace(0,0.99,50)
Pblist=np.linspace(0,1,50)
c=plt.pcolormesh(Pslist,Pblist,rd_mean, cmap="plasma")
plt.title('density of Quarantine - density of Prevention (Local)')
plt.colorbar(c)
plt.xlabel('density of Prevention (Ps)')
plt.ylabel('density of Quarantine (Pb)')
plt.savefig('Ps-Pb(limited)')


# %%



