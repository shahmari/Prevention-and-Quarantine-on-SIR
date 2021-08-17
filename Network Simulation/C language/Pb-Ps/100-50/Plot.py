# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
import matplotlib.pyplot as plt


# %%
file_list=["Pb00.csv","Pb02.csv","Pb04.csv","Pb06.csv","Pb08.csv"]
rdata=np.ndarray((5,100,100))
rd_mean=np.ndarray((5,100))
for i in range(5):
    file=np.loadtxt(open(file_list[i],'r'), dtype='str', delimiter=",")
    for j in range(100):
        for k in range(100):
            rdata[i,j,k]=int(file[k,j])-(160000*i*0.2)
    for m in range(100):
        rd_mean[i,m]=np.average(rdata[i][:,m])    


# %%
Pb=np.linspace(0,1,num=100)
color=['steelblue','g','y','darkorange','r']
plt.figure(dpi=250,figsize=(12,10))
plt.grid()
for i in range(5):
    plt.plot(Pb,rd_mean[i],c=color[i])
plt.savefig('R-Ps(mean)')


# %%
plt.figure(dpi=250,figsize=(12,10))
plt.grid()
for i in range(5):
    for j in rdata[i]:
        plt.scatter(Pb,j,c=color[i],s=3,alpha=0.2)
plt.savefig('R-Ps(total)')


# %%
plt.figure(dpi=250,figsize=(12,10))
plt.grid()
for i in range(5):
    for j in rdata[i]:
        plt.scatter(Pb,j,c=color[i],s=3,alpha=0.2)
    plt.plot(Pb,rd_mean[i],c=color[i],lw=3)
plt.savefig('R-Ps')


