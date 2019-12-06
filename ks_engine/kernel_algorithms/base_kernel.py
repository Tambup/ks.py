#! /usr/bin/python

# Copyright (c) 2019 Filippo Ranza <filipporanza@gmail.com>


import math


def base_kernel_builder(base, values, sorter):
    return base


def percentage_better_kernel_builder(base, value, sorter, percentage):
    kernel_vars = sorter(base, value)
    last_taken = math.floor(len(kernel_vars) * percentage)
    for name in kernel_vars[last_taken:]:
        base[name] = False
    return base


KERNEL_BUILDERS = {
    "base": base_kernel_builder,
    "percentage": percentage_better_kernel_builder,
}
