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

    plt.plot(x, y)
    plt.plot(x, t)

    plt.grid()
    plt.xlim((0, x[-1]))
    plt.ylim((0, u * 1.1))

    plt.xlabel(r'Zeit in s')
    plt.ylabel(r'Zeit in V')

    plt.savefig('output/charge_curve.png')


def main():
    os.makedirs('output', exist_ok=True)

    print_charge_curve()


if __name__ == '__main__':
    main()
