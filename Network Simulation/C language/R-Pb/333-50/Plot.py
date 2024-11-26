# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
import matplotlib.pyplot as plt


# %%
file_list=["Ps00.csv","Ps02.csv","Ps04.csv","Ps06.csv","Ps08.csv"]
Pslist=np.arange(0,1,0.2)
rdata=np.ndarray((5,50,100))
rd_mean=np.ndarray((5,100))
for i in range(5):
    file=np.loadtxt(open(file_list[i],'r'), dtype='str', delimiter=",")
    for j in range(50):
        for k in range(100):
            rdata[i,j,k]=int(file[k,j])-((333**2)*i*0.2)
    for m in range(100):
        rd_mean[i,m]=np.average(rdata[i][:,m])    


# %%
Pb=np.linspace(0,1,num=100)
color=['steelblue','g','y','darkorange','r']
plt.figure(dpi=250,figsize=(12,10))
plt.title('Local interaction against the density of Quarantine')
plt.grid(color = 'navy', linestyle = '--', linewidth = 0.5)
for i in range(5):
    plt.plot(Pb,rd_mean[i],c=color[i],label='Ps={:.1f}'.format(Pslist[i]))
plt.xlabel('density of Quarantine (Pb)')
plt.ylabel('density of Recovereds (R∞)')
plt.legend(loc=0)
plt.savefig('R-Pb(mean)')


# %%
plt.figure(dpi=250,figsize=(12,10))
plt.title('Local interaction against the density of Quarantine')
plt.grid(color = 'navy', linestyle = '--', linewidth = 0.5)
for i in range(5):
    for j in rdata[i]:
        plt.scatter(Pb,j,c=color[i],s=3,alpha=0.2)
plt.xlabel('density of Quarantine (Pb)')
plt.ylabel('density of Recovereds (R∞)')
plt.legend(loc=0)
plt.savefig('R-Pb(total)')


# %%
plt.figure(dpi=250,figsize=(12,10))
plt.title('Local interaction against the density of Quarantine')
plt.grid(color = 'navy', linestyle = '--', linewidth = 0.5)
for i in range(5):
    for j in rdata[i]:
        plt.scatter(Pb,j,c=color[i],s=3,alpha=0.2)
    plt.plot(Pb,rd_mean[i],c=color[i],lw=3,label='Ps={:.1f}'.format(Pslist[i]))
plt.xlabel('density of Quarantine (Pb)')
plt.ylabel('density of Recovereds (R∞)')
plt.legend(loc=0)
plt.savefig('R-Pb')


