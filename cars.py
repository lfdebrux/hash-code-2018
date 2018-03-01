#!/bin/env python3

r"""Google Hash Code 2018 problem from 2018

Self-driving cars!

Example:

>>> a_example = open('a_example.in', 'r')
>>> print(solve(a_example))
1 0
2 2 1

>>> Ride((0, 0), (1, 3), 2, 9)
Ride((0, 0), (1, 3), 2, 9)

>>> a_example = open('a_example.in', 'r')
>>> read_problem_statement(a_example)
Problem(3, 4, 2, 3, 2, 10, [Ride((0, 0), (1, 3), 2, 9), Ride((1, 2), (1, 0), 0, 9), Ride((2, 0), (2, 2), 0, 9)])

This problem uses the Manhattan distance metric a lot

>>> manhattan_distance((0, 0), (2, 0))
2
>>> manhattan_distance((0, 0), (2, 2))
4

>>> Vehicle([2, 1]).print_rides()
'2 2 1'
"""

import numpy as np
import operator

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

    def __init__(self, index, start, end, t_start, t_finish):
        self.index = index
        self.start = start
        self.end = end
        self.t_start = t_start
        self.t_finish = t_finish

    def __repr__(self):
        return f'Ride({self.start}, {self.end}, {self.t_start}, {self.t_finish})'

class Vehicle:

    def __init__(self, rides=None, *, time=0, location=(0,0)):
        self.time = time
        self.location = location
        if rides:
            self.rides = rides
        else:
            self.rides = []

    def print_rides(self):
        s = f'{len(self.rides)}'
        for r in self.rides:
            s += f' {r.index}'
        return s

    def sort_nearest(self, rides):
        '''sort rides by the closest in space-time.'''
        return sorted(rides, key=self.distance_to_ride)

    def distance_to_ride(self, ride):
        return space_time_distance(self.location, self.time, ride.start, ride.t_start)

    def add_ride(self, ride):
        self.rides.append(ride)
        t_to_start = manhattan_distance(self.location, ride.start)
        self.time += t_to_start
        self.location = ride.end
        if self.time < ride.t_start:
            self.time = ride.t_start
        self.time += manhattan_distance(ride.start, ride.end)

def manhattan_distance(a, b):
    return abs(b[0]-a[0]) + abs(b[1]-a[1])

def space_time_distance(a, t_a, b, t_b):
    return manhattan_distance(a, b) + abs(t_a - t_b)

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
    for index in range(N):
        a, b, x, y, s, f = map(int, problem.readline().split())
        rides.append(Ride(index, (a, b), (x, y), s, f))

    return Problem(R, C, F, B, T, rides)

def earliest_start_solve(problem):
    '''a really unoptimised strategy for solving the problem'''
    sorted_rides = sorted(problem.rides, key=operator.attrgetter('t_start'))
    vehicles = []
    n_vehicles = problem.vehicles
    for i, r in enumerate(sorted_rides):
        v = Vehicle()
        v.add_ride(i, r)
        vehicles.append(v)
        n_vehicles -= 1
        if n_vehicles == 0:
            break
    return vehicles

def aron_solve(problem):
    '''extension of earliest start solve'''
    sorted_rides = sorted(problem.rides, key=operator.attrgetter('t_start'))
    vehicles = []
    assigned_rides = []
    n_vehicles = problem.vehicles
    #assign first ride to each vehicle
    for i, n in enumerate(sorted_rides):
        vehicles.append(Vehicle([i]))
        #ride id, [startx, starty, endx, endy, earlistart, latefinish], journey-length, actual finish
        ride = problem.rides[i]
        journey_length = abs(ride[0]-ride[2])+abs(ride[1]-ride[3])
        actual_start = 
        assigned_rides.append(i,ride,journey_length,)
        n_vehicles -= 1
        if n == 0:
            break
    #in the order that the vehicles finish with their current ride re-assign them
    while True:
        #find next vehicle to finish
        next_available = vehicles
        #assign closest achievable (vehicle can complete ride before latest finish of that ride) ride to vehicle

    return vehicles

def solve(problem, strategy=earliest_start_solve):
    problem = read_problem_statement(problem)
    vehicles = strategy(problem)
    return write_solution(vehicles)

def write_solution(vehicles):
    s = ''
    for v in vehicles:
        s += v.print_rides() + '\n'
    return s

def customer_value(rides):
    'lengt of the ride i.e. score, not using bonus as that is equal for all customers'
    rides_value = []
    for ride in rides:
        rides_value.append(abs(ride[0]-ride[2])+abs(ride[1]-ride[3]))
    return rides_value

def ride_possible(rides):
    'this founction tests if the ride is possible at all, i.e. lenght of the ride is less than assigned time slot'
    rides_possible = []
    for ride in rides:
        if abs(ride[0]-ride[2])+abs(ride[1]-ride[3]) < ride[5]-ride[4]:
            rides_possible.append[1]
        else:
            rides_possible.append[0]
    return rides_possible

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="Solve the Google Hash Code 2018 problem")
    parser.add_argument('problem', type=argparse.FileType('r'))
    parser.add_argument('--strategy', default="earliest_start_solve",
                        help="the strategy function to use")
    args = parser.parse_args()

    strategy = globals()[args.strategy]

    print(solve(args.problem, strategy=strategy))
