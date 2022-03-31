import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

y_vals = [0]
walk = [0]
count = 1

# spicy animation of 2D random walk

def animate(i):
    y_vals.append(y_vals[-1] + random.randint(-1,1))
    walk.append(0)

    plt.cla()
    plt.plot(walk)
    plt.plot(y_vals)



while True:
    ani = FuncAnimation(plt.gcf(), animate, interval = 1)
    plt.show()



'''

# Regular random walk



while count != 20:

    if y_vals[-1] == 0:
        count += 1

    y_vals.append(y_vals[-1] + random.randint(-1,1))



for i in y_vals:
    walk.append(0)

plt.plot(y_vals)
plt.plot(walk)

plt.show()












'''









