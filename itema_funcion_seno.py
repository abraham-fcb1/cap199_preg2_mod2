
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x)

def df(x):
    return np.cos(x)

x = np.linspace(0, 2*np.pi, 400)
y = f(x)

puntos = [0, np.pi/4, np.pi/2, np.pi, 3*np.pi/2]
colores = ['red', 'green', 'blue', 'magenta', 'cyan']

plt.figure(figsize=(10,5))
plt.plot(x, y, color='black', linewidth=3, label='f(x) = sin(x)')

for x0, c in zip(puntos, colores):
    y0 = f(x0)
    m = df(x0)

    xt = np.linspace(x0 - 0.7, x0 + 0.7, 100)
    yt = m * (xt - x0) + y0

    plt.plot(xt, yt, color=c, linewidth=2, label=f'Tangente en x={x0:.2f}')
    plt.scatter(x0, y0, color=c, s=80)

plt.axhline(0, color='gray', linewidth=0.8)
plt.axvline(0, color='gray', linewidth=0.8)
plt.grid(alpha=0.3)
plt.title("Rectas tangentes a f(x) = sin(x)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()
