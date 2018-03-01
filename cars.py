#!/bin/env python3

r"""Google Hash Code 2018 problem from 2018

Self-driving cars!

Example:

>>> a_example = open('a_example.in', 'r')
>>> solve(a_example)
1 0
2 2 1

>>> Ride((0, 0), (1, 3), 2, 9)
Ride((0, 0), (1, 3), 2, 9)

>>> read_problem_statement(a_example)
Problem(3, 4, 2, 3, 2, 10, [Ride((0, 0), (1, 3), 2, 9), Ride((1, 2), (1, 0), 0, 9), Ride((2, 0), (2, 2), 0, 9)])
"""

import numpy as np

class Problem:

    def __init__(self, rows, cols, vehicles, bonus, steps, rides):
        self.rows = rows
        self.cols = cols
        self.n_rides = len(rides)
        self.vehicles = vehicles
        self.bonus = bonus
        self.steps = steps
        self.rides = rides

    def __repr__(self):
        return f'Problem({self.rows}, {self.cols}, {self.vehicles}, {self.n_rides}, {self.bonus}, {self.steps}, {self.rides})'

class Ride:

    def __init__(self, start, end, t_start, t_finish):
        self.start = start
        self.end = end
        self.t_start = t_start
        self.t_finish = t_finish

    def __repr__(self):
        return f'Ride({self.start}, {self.end}, {self.t_start}, {self.t_finish})'

def read_problem_statement(problem):
    # first line includes
    # R number of rows in the grid (0 <= R <= 10000)
    # C number of columns of the grid (1 ≤ C ≤ 10000)
    # F number of vehicles in the fleet (1 ≤ F ≤ 1000)
    # N number of rides (1≤N ≤10000)
    # B per-ride bonus for starting the ride on time (1 ≤ B ≤ 10000)
    # T number of steps in the simulation (1 ≤ T ≤ 109)
    R, C, F, N, B, T = map(int, problem.readline().split())

    # N subsequent lines
    # a the row of the start intersection (0 ≤ a < R)
    # b the column of the start intersection (0 ≤ b < C )
    # x the row of the finish intersection (0 ≤ x < R)
    # y the column of the finish intersection (0 ≤ y < C )
    # s the earliest start (0≤s<T)
    # f the latest finish (0≤f ≤T), (f ≥s+|x−a|+|y−b|)
    # note that f can be equal to T – this makes the latest finish equal to the end of the simulation
    rides = []
    for n in range(N):
        a, b, x, y, s, f = map(int, problem.readline().split())
        rides.append(Ride((a, b), (x, y), s, f))

    return Problem(R, C, F, B, T, rides)

def solve(problem):
    pass
