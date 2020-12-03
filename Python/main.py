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


def print_charge_curve(name: str, u=5, tau=2, base_tau=2, e_tau='s'):
    x = np.linspace(0, 6.5 * base_tau)
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

    # Tau
    plt.axvline(tau, color='r')
    plt.text(tau + 0.1, +0.1, f'$𝜏 = {tau} s$', fontsize=12)

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
        i_c = (u - u_c) / r
        yield u_c, i_c
        i = (u - u_c) / r
        q += i * dt
        u_c = q / c


def print_square_function(name, u=5, f_f=1, tau=2, e_tau='s'):
    t = np.linspace(0, 2 * 6 * tau, 500, endpoint=False)
    dt = (np.max(t) - np.min(t)) / len(t)

    f = f_f / (2 * 5 * tau)

    u_t = u * (signal.square(2 * np.pi * f * t) / 2 + 0.5)

    plt.plot(t, u_t, color='b')
    plt.plot(t, [u_c for u_c, i_c in u_c_t(u_t, tau, dt)], color='g')

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
    plt.plot(t, [u_c for u_c, i_c in u_c_t(u_t, tau, dt)], color='g')

    plt.grid()
    plt.xlim((0, t[-1]))
    plt.ylim((0, u * 1.1))

    plt.xlabel(rf'Zeit in {e_tau}')
    plt.ylabel(r'Spannung in V')

    f_name = f'output/{name}.png'
    os.makedirs(os.path.dirname(f_name), exist_ok=True)
    plt.savefig(f_name)

    plt.clf()


def print_sin_u_i_function(name, phi=-45, e_t='s'):
    f = 0.5
    t = np.linspace(0, 2 / f, 500, endpoint=False)

    phi_rad = phi / 180 * np.pi

    u_max = 1
    i_max = 0.75

    u_t = u_max * np.sin(2 * np.pi * f * t)
    i_t = i_max * np.sin(2 * np.pi * f * t - phi_rad)

    plt.plot(t, u_t, color='b', label="Spannung")
    plt.plot(t, i_t, color='r', label="Strom")

    plt.grid()
    plt.xlim((0, t[-1]))

    # Markers
    if phi != 0:
        t_u_max = 1 / (4 * f)
        t_i_max = t_u_max + phi / 90 * 1 / (4 * f)

        plt.plot([t_u_max, t_u_max],
                 [u_max, u_max + 0.5], color='b')

        plt.plot([t_i_max, t_i_max],
                 [i_max, u_max + 0.5], color='r')

        plt.plot([t_u_max, t_i_max],
                 [u_max + 0.4, u_max + 0.4], color='black')

        plt.text((t_i_max+t_u_max)/2-0.05, u_max + 0.45, fr'$\varphi$', fontsize=12)

    plt.xlabel(rf'Zeit in {e_t}')
    plt.legend()

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

    print_square_function('versuch1/oszilloskop', tau=1, u=4, e_tau='ms')

    print_sin_function('sin_1')
    print_sin_function('sin_2', f_f=2)
    print_sin_function('sin_4', f_f=4)

    print_sin_u_i_function('sin_u_i_1')


if __name__ == '__main__':
    main()
