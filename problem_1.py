import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

STUDENT_NUMBER = 0000000

a = int(str(STUDENT_NUMBER)[-1])%6+1
b = int(str(STUDENT_NUMBER)[-2])%5+1
c = int(str(STUDENT_NUMBER)[-3])+1

A = (a-b-c-1)/3
B = (-a+b+c-a*b-a*c)/2
C = a*b+a*c


# 関数
def f(x):
    return (1/4)*(x**4) + A*(x**3) + B*(x**2) + C*x


# 微分
def f_diff(f):
    return sym.diff(f)


# 極値を求める
def cal_extremum(f):
    return sym.solve(f)


# 関数とx軸の交点を見つける
def plot_roots(roots_list):
    roots = np.roots(roots_list)
    real_roots = roots[np.isreal(roots)].real
    colors = ['red', 'orange', 'lime', 'purple']
    for i, root in enumerate(real_roots):
        color = colors[i % len(colors)]
        plt.scatter(root, 0, color=color, label=f'Root {i+1}: ({root:.2f}, 0)')


def make_graph(f, extremum, label_text, roots_list, title):
    # グラフ表示領域
    x_min = -7
    x_max = 6
    x_interval = 0.1
    x_val = np.arange(x_min, x_max, x_interval)

    # 関数f(x)を格納する配列
    f_val = []

    # それぞれ配列に格納していく
    for i in range(len(x_val)):
        f_val.append(f.subs(x, x_val[i]))

    # 関数f(x)のグラフを作成
    plt.plot(x_val, f_val, color='blue', label=label_text)

    # グラフにx軸,y軸（0）を図示
    # 補助線（0）を作成 [axhline：水平 axvline:垂直]
    plt.axhline(y=0, color="gray")
    plt.axvline(x=0, color="gray")

    # x軸・y軸から極値までを点線で作成
    for j in range(len(extremum)):
        # 極値を一時変数に格納
        tmp_x = float(extremum[j])
        # y の値を一時変数に格納
        tmp_y = float(f.subs(x, tmp_x))

        # 補助線を点線で作成 [hlines：水平 vlines:垂直]
        plt.hlines([tmp_y], 0, tmp_x, "gray", linestyles='dashed')
        plt.vlines([tmp_x], 0, tmp_y, "gray", linestyles='dashed')

    plot_roots(roots_list)

    # グラフのタイトル
    plt.title(title, fontname='MS Gothic')

    # x軸のラベル
    plt.xlabel('x', fontname='MS Gothic')

    # y軸のラベル
    plt.ylabel('y', fontname='MS Gothic')

    # ラベルの表示
    plt.legend(bbox_to_anchor=(1, 1), loc='upper right', borderaxespad=1, fontsize=8)

    # グラフを表示
    plt.show()


if __name__ == '__main__':
    print(f'a = {a}, b = {b}, c = {c}')
    print(f'A = {A}, B = {B}, C = {C}')
    print(f'f(x) = (1/4)x^4 + {A}x^3 + {B}x^2 + {C}x')
    print(f'f\'(x) = x^3 + {3*A}x^2 + {2*B}x + {C}')

    # 文字列を設定
    x = sym.Symbol('x')

    # f を微分する
    df = f_diff(f(x))

    # f の極値をとる x の値を求める
    extremum_f = cal_extremum(df)

    # f の極値とそのときの x の値を出力
    print('====================')
    print('f(x) の極値')
    for i in range(len(extremum_f)):
        print('x = ', round(extremum_f[i], 2))
        print('f(x) = ', round(f(x).subs(x, extremum_f[i]), 2))

    # グラフ作成
    make_graph(f(x), extremum_f, label_text='f(x)', roots_list=[(1/4), A, B, C, 0], title='y = f(x) のグラフ')
    

    # df を微分する
    ddf = f_diff(df)

    # df の極値をとる x の値を求める
    extremum_df = cal_extremum(ddf)

    # df の極値とそのときの x の値を出力
    print('====================')
    print('f\'(x) の極値')
    for i in range(len(extremum_df)):
        print('x = ', round(extremum_df[i], 2))
        print('f\'(x) = ', round(df.subs(x, extremum_df[i]), 2))

    # グラフ作成
    make_graph(df, extremum_df, label_text='f\'(x)', roots_list=[1, 3*A, 2*B, C], title='y = f\'(x) のグラフ')
