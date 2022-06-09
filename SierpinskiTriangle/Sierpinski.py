import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D


def generate_Sierpinski_triangle(start_vertex_pos, dot_num):
    Sierpinski_dots = np.zeros((2, dot_num))
    anchor_vertex = start_vertex_pos[np.random.randint(3)]
    anchor_dot = start_vertex_pos[np.random.randint(3)]
    for i in range(dot_num):
        Sierpinski_dot = ((anchor_vertex[0] + anchor_dot[0]) / 2, (anchor_vertex[1] + anchor_dot[1]) / 2)
        Sierpinski_dots[0][i] = Sierpinski_dot[0]
        Sierpinski_dots[1][i] = Sierpinski_dot[1]
        anchor_dot = Sierpinski_dot
        anchor_vertex = start_vertex_pos[np.random.randint(3)]
    return Sierpinski_dots


def update_dots(num):
    x.append(Sierpinski_dots[0][num])
    y.append(Sierpinski_dots[1][num])
    dots.set_offsets(np.c_[x, y])


if __name__ == '__main__':
    Sierpinski_dots = generate_Sierpinski_triangle([(0, 0), (6, 0), (3, 4)], 10000)
    fig, ax = plt.subplots()
    plt.grid(ls="--")
    x = [0, 6, 3]
    y = [0, 0, 4]
    dots = ax.scatter(x, y)

    ani = animation.FuncAnimation(fig, update_dots, 1000, interval=100, repeat=True)
    plt.show()
