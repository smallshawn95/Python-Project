import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]
z = [2, 2, 2, 2, 2]
fig1 = plt.figure(num = 1)
plt.subplot(2, 2, 1)
plt.plot(x)
fig2 = plt.figure(num = 1)
plt.subplot(2, 2, 1)
plt.plot(y)
fig3 = plt.figure(num = 1)
plt.subplot(2, 2, 1)
plt.plot(z)
plt.show()
