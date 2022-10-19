import matplotlib.pyplot as plt
import numpy as np
def signalx(t):
    if t>=-2 and t<-1:
        return -2-t
    elif t>=-1 and t<0:
        return 1
    elif t>=0 and t<2:
        return 1-t
    elif t>=2 and t<3:
        return -1
    else:
        return 0


def test():
    print("Yo")


def stepu(t):
    if t>=0:
        return 1
    else:
        return 0


def rampr(t):
    return t*stepu(t)



def xt(t):
    return stepu(t+1)-stepu(t)-rampr(t-1)+(2*rampr(t-2))


data=[]

print(signalx(-2))
print(signalx(-1))
print(signalx(0))
print(signalx(1))
print(signalx(2))
print(signalx(3))

print("==========")

data.append(signalx(-2))
data.append(signalx(-1.5))
data.append(signalx(-1))
data.append(signalx(-0.5))
data.append(signalx(0))
data.append(signalx(0.5))
data.append(signalx(1))
data.append(signalx(1.5))
data.append(signalx(2))
data.append(signalx(2.5))
data.append(signalx(3))
data.append(signalx(3.5))

time=np.arange(-3,3,0.5)

fig,ax=plt.subplots()

ax.plot(time,data)

ax.set(xlabel='time (s)',ylabel='voltage (mv)',title='Signal(x) expressed via u(t) and r(t)')
ax.grid()

fig.savefig("test.png")

plt.show()


                                           
                                           







