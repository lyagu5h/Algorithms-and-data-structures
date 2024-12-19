def runge_kutta_4(f, x0, y0, h, x_end):
    x = x0
    y = y0
    n_steps = int((x_end - x0) / h)  # Количество шагов
    for _ in range(n_steps):
        k1 = f(x, y)
        k2 = f(x + h / 2, y + h * k1 / 2)
        k3 = f(x + h / 2, y + h * k2 / 2)
        k4 = f(x + h, y + h * k3)
        y += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x += h
    return y

def f(x, y):
    return 2 * x

x0 = 0
y0 = 1
x_end = 1
h = 0.1

y_rk4 = runge_kutta_4(f, x0, y0, h, x_end)

y_exact = x_end**2 + 1

print(f"Численное решение (Рунге-Кутта): y({x_end}) = {y_rk4:.6f}")
print(f"Аналитическое решение: y({x_end}) = {y_exact:.6f}")
print(f"Погрешность: {abs(y_rk4 - y_exact):.6f}")