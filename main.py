import numpy as np
import matplotlib.pyplot as plt

print('Enter n')
n = int(input())
print('Enter 0 if Left Riemann Sum')
print('Enter 1 if Midpoint Riemann Sum')
print('Enter 2 if Right Riemann Sum')
i = int(input())
f = lambda x: x ** 2
a, b = 1, 2
dx = 1 / n
x_left = np.linspace(a, b - dx, n)
x_midpoint = np.linspace(dx / 2, b - dx / 2, n)
x_right = np.linspace(dx, b, n)
left_riemann_sum = np.sum(f(x_left) * dx)
midpoint_riemann_sum = np.sum(f(x_midpoint) * dx)
right_riemann_sum = np.sum(f(x_right) * dx)

if i == 0:
    print('Left Riemann Sum:', left_riemann_sum)
if i == 1:
    print('Midpoint Riemann Sum:', midpoint_riemann_sum)
if i == 2:
    print('Right Riemann Sum:', right_riemann_sum)
# Create matplotlib
x = np.arange(1, 2, 0.05)
y = x**2
fig, ax = plt.subplots()
ax.plot(x, y, 'r')
ax.set_ylim(bottom=0)
for j in range(n):
    x = np.linspace(a, b, n + 1)
    y = f(x)
    X = np.linspace(a, b, n**2 + 1)
    Y = f(X)
    if i == 0:
        plt.plot(X, Y, 'b')
        x_left = x[:-1]  # Left endpoints
        y_left = y[:-1]
        plt.plot(x_left, y_left, 'b.', markersize=10)
        plt.bar(x_left, y_left, width=(1 / n), alpha=0.2, align='edge', edgecolor='r')
        plt.title('Left Riemann Sum, n = {}'.format(n))
    if i == 1:
        plt.plot(X, Y, 'b')
        x_mid = (x[:-1] + x[1:]) / 2  # Midpoints
        y_mid = f(x_mid)
        plt.plot(x_mid, y_mid, 'b.', markersize=10)
        plt.bar(x_mid, y_mid, width=(1 / n), alpha=0.2, edgecolor='r')
        plt.title('Midpoint Riemann Sum, n = {}'.format(n))
    if i == 2:
        plt.plot(X, Y, 'b')
        x_right = x[1:]  # Left endpoints
        y_right = y[1:]
        plt.plot(x_right, y_right, 'b.', markersize=10)
        plt.bar(x_right, y_right, width=(-1 / n), alpha=0.2, align='edge', edgecolor='r')
        plt.title('Right Riemann Sum, n = {}'.format(n))

plt.show()
