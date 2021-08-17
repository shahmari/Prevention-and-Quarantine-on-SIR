# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
import matplotlib.pyplot as plt


# %%
file_list=["Pb00.csv","Pb02.csv","Pb04.csv","Pb06.csv","Pb08.csv"]
Pblist=np.arange(0,1,0.2)
rdata=np.ndarray((5,50,99))
rd_mean=np.ndarray((5,99))
for i in range(5):
    file=np.loadtxt(open(file_list[i],'r'), dtype='str', delimiter=",")
    for j in range(50):
        for k in range(99):
            rdata[i,j,k]=int(file[k,j])
    for m in range(99):
        rd_mean[i,m]=np.average(rdata[i][:,m])


# %%
Ps=np.linspace(0,0.99,num=99)
for n in range(5):
    for i in range(99):
        for j in range(50):
            rdata[n,j,i]-=(Ps[i]*(333**2))
        rd_mean[n,i]-=(Ps[i]*(333**2))


# %%
color=['steelblue','g','y','darkorange','r']
plt.figure(dpi=250,figsize=(12,10))
plt.grid(color = 'navy', linestyle = '--', linewidth = 0.5)
plt.title('Local interaction against the density of Prevention')
for i in range(5):
    plt.plot(Ps,rd_mean[i],c=color[i],lw=3,label='Pb={:.1f}'.format(Pblist[i]))
plt.xlabel('density of Prevention (Ps)')
plt.ylabel('density of Recovereds (R∞)')
plt.legend(loc=0)
plt.savefig('R-Ps(mean)')


# %%
plt.figure(dpi=250,figsize=(12,10))
plt.grid(color = 'navy', linestyle = '--', linewidth = 0.5)
for i in range(5):
    for j in rdata[i]:
        plt.scatter(Ps,j,c=color[i],s=3,alpha=0.2)
plt.savefig('R-Ps(total)')


# %%
plt.figure(dpi=250,figsize=(12,10))
plt.grid(color = 'navy', linestyle = '--', linewidth = 0.5)
plt.title('Local interaction against the density of Prevention')
for i in range(5):
    for j in rdata[i]:
        plt.scatter(Ps,j,c=color[i],s=3,alpha=0.2)
    plt.plot(Ps,rd_mean[i],c=color[i],lw=3,label='Pb={:.1f}'.format(Pblist[i]))
plt.xlabel('density of Prevention (Ps)')
plt.ylabel('density of Recovereds (R∞)')
plt.legend(loc=0)
plt.savefig('R-Ps')


# %%



