import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from bubble_sort import bubble_sort
all_data=[3,4,1,7,10,14,16,15,89,23,57,21,50,56,1]


def data_gen(t=0):
	return  bubble_sort(all_data)


fig, ax = plt.subplots()
x=[i for i in range(1,len(all_data)+1)]
y=all_data
#data1=[[i,j] for i,j in zip(x,y)]
sca1 = ax.scatter(x,y)
#ax.grid()
	
def init():
	data1=[[i,j] for i,j in zip(x,y)]
	sca1.set_offsets(data1)
	return sca1



def run(data):
    # update the data
	y=data
	print(y)
	sca1.set_offsets([[i,j] for i,j in zip(x,y)])
	return sca1

ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=1000,
                              repeat=False, init_func=init)
plt.show()




