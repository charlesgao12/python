# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 20:47:16 2018

@author: chael
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

fig,ax=plt.subplots()

xx=[0.0]
yy=[-600.0]
vyy=10.0
ayy=-0.08

line0,=ax.plot(xx,yy,color='green')
big =plt.scatter(0,-600,c='black',s=80)


x=[0.0]
y=[0.0]
vx =0.5
vy=3.0
a=-0.003

line,=ax.plot(x,y)
blue = plt.scatter(0,0,c='blue',s=8)



turningindex = 0 #to store the explosion frame index




def init():
    global vyy
    global ayy    
    global xx
    global yy
    xx=[0.0]
    yy=[-600.0]
    vyy=5.0
    ayy=-0.04
    
    global vx, x, y
    global vy
    
    
    
    x=[0.0]
    y=[0.0]
    vx =0.5
    vy=3.0
  
    global vx2, x2, y2
    global vy2
    
    x2=[0.0]
    y2=[0.0]
    vx2 =-2
    vy2=1.0
    
    global turningindex
    
    turningindex = 0 #to store the explosion frame index
    line0.set_visible(False)
    line.set_visible(False)

    big.set_visible(False)
    blue.set_visible(False)

    
    
    
    
    return line0,
    
def bigmove(i):
    
    global xx
    
    global yy
    global vyy
    global turningindex
    if vyy>=0 and (vyy+ayy)<0:
        turningindex = i
        print('turning:',turningindex)
        line0.set_visible(False)
        line.set_visible(True)

        big.set_visible(False)
        blue.set_visible(True)

    #else:
    vyy=vyy+ayy
    
    
    yy = np.append(yy,[yy[-1]+vyy*(i+1)])    
    xx = np.append(xx,[0])
    big.set_offsets((0,yy[-1]))
    
    
    if i==0:
        xx =[0]
        yy=[-600.0]
        #vx =0.05
        vyy=2.0   
        line0.set_visible(True)
        big.set_visible(True)
    #print('big',i)
    #print(xx,yy)
    line0.set_xdata(xx)
    line0.set_ydata(yy)
    

def explosion(i):    
     #blue
    global x
    x = np.append(x,[vx* (i+1)])
    global vy
    
    vy = vy+a
    global y
    
    y= np.append(y,[y[-1]+vy*(i+1)]  )
    
    if i==0:
        x=[0]
        y=[yy[-1]]   
        #vx =0.05
        vy=0.2
        
    print(i,y)
    line.set_xdata(x)
    line.set_ydata(y)
    #global blue
    blue.set_offsets((vx* (i+1), y[-1]))
    

    

def update(i):
    if i == 0:
        init()
    
    if vyy>=0:# the big one explose, and then disapear
        bigmove(i)
        
    else:
        
        explosion(i-turningindex-1)   
   
    
    return line0,

      
plt.xlim((-600,600))
plt.ylim((-800,800))
#plt.plot(x,y)

ani = animation.FuncAnimation(fig=fig, init_func=init, repeat=True,func=update, interval=10, blit=False,frames=170)

plt.show()





