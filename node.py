# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 14:35:17 2019

@author: kilia
"""
import copy

class Node:

    def __init__(self, robots, father, movetuple):
        self.robots_ = robots
        self.father_ = father
        self.move_tuple_ = movetuple # what robot was moved to what direction

    def __init__(self, robots, father, movetuple, g, h):
        self.robots_ = robots
        self.father_ = father
        self.move_tuple_ = movetuple # what robot was moved to what direction
        self.g_ = g # g(n)
        self.h_ = h # heuristic

    def get_cost(self):
        return self.g_ + self.h_

    @staticmethod
    def get_solution(node):
        solution = []
        current = node
        while (current.father_ != 0):
            solution.insert(0, current.move_tuple_)
            current = current.father_
        return solution

    @staticmethod
    def compareState(state1, state2):
        t=True
        for i in range(len(state1.robots_)):
            if (state1.robots_[i].color_!=state2.robots_[i].color_) or (state1.robots_[i].x_!=state2.robots_[i].x_ ) or (state1.robots_[i].y_!=state2.robots_[i].y_):
                t=False
        return t

    def get_level(self):
        current = self
        output = 0
        while (current.father_ != 0):
            output += 1
            current = current.father_
        return output

    @staticmethod
    def copyNode(oldNode):
        return copy.deepcopy(oldNode)
