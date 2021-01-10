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
