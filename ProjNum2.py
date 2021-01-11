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

Réponse à la question 11
K est le facteur responsable de la vitesse de convergence de H vers H_{}. Plus k est grand et plus la solution converge rapidement.
Il ne peut cependant pas être choisi arbitrairement grand, car la correction pourrait alors être trop forte par rapport au pas de temps, ce qui rendrait la méthode d'Euler inefficace :
$\forall j, H(x_{j+1}) - H_{0} =  H(x_{j}) - H_{0} + dt(-k)(||\nabla H(x_{j})||)^2(H(x_{j+1}) - H_{0})
H(x_{j+1}) - H_{0} = (H(x_{j+1}) - H_{0})(1-kdt(||\nabla H(x_{j})||)^2)$
Oron sait que $(||\nabla H(x_{j})||)^2$ est borné d'après les questions précédentes. En considéran ses bornes, on retrouve une suite géométrique de raison $(1-kdt(||\nabla H(x_{j})||)^2)$.
Or pour que la solution converge bien, il faut $|(1-kdt(||\nabla H(x_{j})||)^2)|<1$. C'est-à-dire lorsque $0<k<\fract{2}{dt(||\nabla H(x_{j})||)^2$
          
