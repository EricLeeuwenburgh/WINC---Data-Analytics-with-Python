import matplotlib.pyplot as plt
import numpy as np

"""Plots cant't be viewed in the terminal. Therefor copy the copy the code into Google Colab and run it there to visualize the plots. """

# 1 Creating a plot
fig, ax = plt.subplots() # Creates a figure containing a single axis.
ax.plot([1,2,3,4], [1,4,2,3]) # Plot some data on the axes.

# 2 Multiple plots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
x = np.arange(1, 10)
ax1.plot(x, x + x)
ax2.plot(x, np.sin(x))
ax3.plot(x, x * 1.5*x)
ax4.plot(x, np.cos(x))

# 3 Multiple lines
fig, ax = plt.subplots()
x = np.arange(1, 10)
ax.plot(x, x + 3)
ax.plot(x, np.sin(x))

# 4 Add labels + legend
fig, ax = plt.subplots()
x = np.arange(1, 10)
ax.plot(x, x + 3, label = "oil prices")
ax.plot(x, np.sin(x), label = "gas prices")
ax.legend()

# 5 Set y-axis limits
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
x = np.arange(1, 10)
ax1.plot(x, x + x)
ax2.plot(x, np.sin(x))
ax3.plot(x, x * 1.5*x)
ax4.plot(x, np.cos(x))

ax1.set_ylim(0, 30)
ax2.set_ylim(0, 30)
ax3.set_ylim(0, 30)
ax4.set_ylim(0, 30)

# 6 Label the y- and x-axis
fig, ax = plt.subplots()
x = np.arange(1, 13)
ax.plot(x, x + 3, label = "Doja cat")
ax.plot(x, np.sin(x) + x, label = "Justin Bieber")
ax.legend()

ax.set_xlim(1, 12)
ax.set_ylim(0, 20)

ax.set_xlabel("month")
ax.set_ylabel("appreciation")

# 7 Format markers and lines
fig, ax = plt.subplots()
x = np.arange(1, 13)
ax.plot(x, x + 3, label = "Doja cat", color="magenta", linestyle="--", marker=".")
ax.plot(x, np.sin(x) + x, label = "Justin Bieber"color="green", linestyle="", marker="8")
ax.legend()

ax.set_xlim(1, 12)
ax.set_ylim(0, 20)

ax.set_xlabel("month")
ax.set_ylabel("appreciation")

# 8 Shorter syntax
fig, ax = plt.subplots()
x = np.arange(1, 13)
ax.plot(x, x + 3, ".--m", label = "Doja cat")
ax.plot(x, np.sin(x) + x, "8g", label = "Justin Bieber")
ax.legend()

ax.set_xlim(1, 12)
ax.set_ylim(0, 20)

ax.set_xlabel("month")
ax.set_ylabel("appreciation")

# 9 Set plot title
fig, ax = plt.subplots()
x = np.arange(1, 13)
ax.plot(x, x + 3, ".--m", label = "Doja cat")
ax.plot(x, np.sin(x) + x, "8g", label = "Justin Bieber")
ax.legend()

ax.set_xlim(1, 12)
ax.set_ylim(0, 20)

ax.set_xlabel("month")
ax.set_ylabel("appreciation")

ax.set_title("Musician appreciation 2020")

# 10 Show grid
fig, ax = plt.subplots()
x = np.arange(1, 13)
ax.plot(x, x + 3, ".--m", label = "Doja cat")
ax.plot(x, np.sin(x) + x, "8g", label = "Justin Bieber")
ax.legend()

ax.set_xlim(1, 12)
ax.set_ylim(0, 20)

ax.set_xlabel("month")
ax.set_ylabel("appreciation")

ax.set_title("Musician appreciation 2020")
ax.grid(True)