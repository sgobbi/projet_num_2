def solve_euler_explicit(f, x0, dt, t0, tf):
    t = [t0]
    x = [x0]
    while t[-1] < tf:
        x.append(x[-1] + dt*f(t[-1], x[-1]))
        t.append(t[-1] + dt)
    return t, x

def solve_euler_implicit(f, x0, dt, t0, tf, itermax = 100):
    t = [t0]
    x = [x0]
    iter = 0
    while t[-1] < tf and i < itermax:
        x1 = x[-1] + dt*f(t[-1], x[-1])
        x.append(x[-1] + dt*f(t[-1], x1))
        t.append(t[-1] + dt)
    return t, x

#question 6, ordre de convergence
def exp(t, x):
    return x

for i in range(1, 6):
    dt = 2**(-i)
    plt.plot(solve_euler_explicit(exp, 1, dt, 0, 5), label = f'dt = 2^{-i}')
t = solve_euler_explicit(exp, 1, dt, 0, 5)[0]
plt.plot(t, np.exp(t), label='exp')
plt.legend()
plt.show()
