#!/usr/bin/python

import os

import matplotlib.pyplot as plt
import numpy as np


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


def main():
    print_charge_curve('ladekurve')
    print_charge_curve('versuch1/ladekurve', tau=1, u=4, e_tau='ms')


if __name__ == '__main__':
    main()
