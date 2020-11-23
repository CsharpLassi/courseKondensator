#!/usr/bin/python

import os

import matplotlib.pyplot as plt
import numpy as np
from scipy import signal


def print_discharge_curve(name: str, u=5, tau=2, e_tau='s'):
    x = np.linspace(0, 6.5 * tau)
    y = u * np.exp(-x / tau)
    t = - u / tau * x + u

    plt.plot(x, y, 'g')

    plt.grid()
    plt.xlim((0, x[-1]))
    plt.ylim((0, u * 1.1))

    plt.xlabel(rf'Zeit in {e_tau}')
    plt.ylabel(r'Spannung in V')

    # U_0
    f_name = f'output/{name}.png'
    os.makedirs(os.path.dirname(f_name), exist_ok=True)

    plt.savefig(f_name)

    # Tangente
    plt.plot(x, t, 'm')

    f_name = f'output/{name}_tangende.png'
    os.makedirs(os.path.dirname(f_name), exist_ok=True)
    plt.savefig(f_name)

    plt.clf()


def print_charge_curve(name: str, u=5, tau=2, e_tau='s'):
    x = np.linspace(0, 6.5 * tau)
    y = u * (1 - np.exp(-x / tau))
    t = u / tau * x

    plt.plot(x, y, 'g')

    plt.grid()
    plt.xlim((0, x[-1]))
    plt.ylim((0, u * 1.1))

    plt.xlabel(rf'Zeit in {e_tau}')
    plt.ylabel(r'Spannung in V')

    # U_0
    plt.axhline(u, color='b')
    plt.text(0.3, u + 0.1, '$U$', fontsize=12)

    f_name = f'output/{name}.png'
    os.makedirs(os.path.dirname(f_name), exist_ok=True)

    plt.savefig(f_name)

    # Tangente
    plt.plot(x, t, 'm')

    f_name = f'output/{name}_tangende.png'
    os.makedirs(os.path.dirname(f_name), exist_ok=True)
    plt.savefig(f_name)

    plt.clf()


def u_c_t(u_t, tau, dt):
    c = 1
    u_c = 0
    q = 0
    r = tau / c
    for u in u_t:
        yield u_c
        i = (u - u_c) / r
        q += i * dt
        u_c = q / c


def print_square_function(name, u=5, f_f=1, tau=2, e_tau='s'):
    t = np.linspace(0, 2 * 6 * tau, 500, endpoint=False)
    dt = (np.max(t) - np.min(t)) / len(t)

    f = f_f / (2 * 5 * tau)

    u_t = u * (signal.square(2 * np.pi * f * t) / 2 + 0.5)

    plt.plot(t, u_t, color='b')
    plt.plot(t, list(u_c_t(u_t, tau, dt)), color='g')

    plt.grid()
    plt.xlim((0, t[-1]))
    plt.ylim((0, u * 1.1))

    plt.xlabel(rf'Zeit in {e_tau}')
    plt.ylabel(r'Spannung in V')

    f_name = f'output/{name}.png'
    os.makedirs(os.path.dirname(f_name), exist_ok=True)
    plt.savefig(f_name)

    plt.clf()


def print_sin_function(name, u=5, f_f=1, tau=2, e_tau='s'):
    t = np.linspace(0, 2 * 6 * tau, 500, endpoint=False)
    dt = (np.max(t) - np.min(t)) / len(t)

    f = f_f / (2 * 5 * tau)

    u_t = u * (np.sin(2 * np.pi * f * t) / 2 + 0.5)

    plt.plot(t, u_t, color='b')
    plt.plot(t, list(u_c_t(u_t, tau, dt)), color='g')

    plt.grid()
    plt.xlim((0, t[-1]))
    plt.ylim((0, u * 1.1))

    plt.xlabel(rf'Zeit in {e_tau}')
    plt.ylabel(r'Spannung in V')

    f_name = f'output/{name}.png'
    os.makedirs(os.path.dirname(f_name), exist_ok=True)
    plt.savefig(f_name)

    plt.clf()


def main():
    print_charge_curve('ladekurve')
    print_discharge_curve('entladekurve')

    print_charge_curve('versuch1/ladekurve', tau=1, u=4, e_tau='ms')

    print_square_function('square_1')
    print_square_function('square_2', f_f=2)
    print_square_function('square_4', f_f=4)

    print_sin_function('sin_1')
    print_sin_function('sin_2', f_f=2)
    print_sin_function('sin_4', f_f=4)


if __name__ == '__main__':
    main()
