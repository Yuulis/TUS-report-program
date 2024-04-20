import problem_1 as p1


def f(x):
    return (1/4)*(x**4) + p1.A*(x**3) + p1.B*(x**2) + p1.C*x


def df(x):
    return x**3 + (3*p1.A)*(x**2) + (2*p1.B)*x + p1.C


def ddf(x):
    return 3*(x**2) + (6*p1.A)*x + 2*p1.B


def newton_method(default, precision=1e-8, max_step=3):
    x = default 
    step = 0

    while abs(f(x)) > precision and step <= max_step:
        print(f"Step {step}: x{step} = {x}, f(x) = {f(x)}, f'(x) = {df(x)}, f''(x) = {ddf(x)}")
        x = round(x - df(x) / ddf(x), 8)
        step += 1
            
    print(f"\n方程式の解: {x}")
    return x


# 初期値
# x0 = -p1.a - 2
# x0 = 0.5
x0 = p1.b + p1.c + 2


# ニュートン法を実行
result = newton_method(x0)