### Combined effects of prevention and quarantine on a breakout in the SIR model

Here, I have reproduced an article with the same title from the [Nature website](https://www.nature.com/articles/srep00010).

This article simulated the epidemic using two methods: mean-field and network-based simulations.
In the first attempt, I performed network simulations using Python.
Although the initial attempt was successful, the code I wrote was very inefficient, disorganized, and unoptimized.
The main issue I encountered initially was the runtime problem. One of the goals was running the dynamic on a network with millions of nodes. I tried to solve this problem within the Python environment, but subsequent attempts to simulate the network still faced runtime issues.
All network simulation codes are available in the 'Network Simulation' directory. My initial attempt is located in the `Network Simulation\Python\Initial effort` folder. My final attempt at network simulation in the Python environment can be found in the `Network Simulation\Python\Final effort` folder.
In my final attempt, I simulated only one of the networks, and I did not simulate the second network in this environment. This is because, in the article, the simulation of the second network is implemented on the global average field.
Runtime issues persisted in this simulation; therefore, I decided to switch to the programming language $C$ and performed the simulation there, successfully resolving the runtime problem. The $C$ language codes are located in the `Network Simulation\C language` directory. Alongside the codes and compiled versions, you can observe some results. For plotting graphs, I used the $Matplotlib$ library, and the code for plotting the graphs is also available in the same directory.
To parallelize the computations for increased speed, I have used a non-standard method, and the implementation codes for it can be found in the 'runfile' folder.
