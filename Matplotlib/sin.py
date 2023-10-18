# pip install matplotlib
import numpy
import matplotlib.pyplot as plt

x = numpy.linspace(0, 10, 100)
y = 4 + 2 * numpy.sin(2 * x)

fig, ax = plt.subplots()
ax.plot(x, y, linewidth = 2.0)

ax.set(
    xlim = (0, 8), xticks = numpy.arange(1, 8),
    ylim = (0, 8), yticks = numpy.arange(1, 8)
)

plt.show()
