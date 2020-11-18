#!/usr/bin/python

import os

import matplotlib.pyplot as plt
import numpy as np


def print_charge_curve():
    tau = 2
    u = 5

    x = np.linspace(0, 6.5 * tau)
    y = u * (1 - np.exp(-x / tau))
    t = u / tau * x

    plt.plot(x, y, 'g')

    plt.grid()
    plt.xlim((0, x[-1]))
    plt.ylim((0, u * 1.1))

    plt.xlabel(r'Zeit in s')
    plt.ylabel(r'Spannung in V')

    # U_0
    plt.axhline(u, color='b')
    plt.text(0.3, u + 0.1, '$U$', fontsize=12)

    plt.savefig('output/ladekurve.png')

    # Tangente
    plt.plot(x, t, 'm')
    plt.savefig('output/ladekurve_tangende.png')


def main():
    os.makedirs('output', exist_ok=True)

    print_charge_curve()


if __name__ == '__main__':
    main()
