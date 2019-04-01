import copy
from robot import Robot

# Node class
#
# Provides valuable methods for both BFS and A-Star needed to complete the
# algorithm efficiently

class Node:
    def __init__(self, robots, father, movetuple, g=0, h=0,level=0):
        self.robots_ = robots
        self.father_ = father
        self.move_tuple_ = movetuple # what robot was moved to what direction
        self.g_ = g # g(n)
        self.h_ = h # heuristic
        self.level_ = level

    def get_solution(self):
        solution = []
        while self.father_ != 0:
            solution.insert(0, self.move_tuple_)
            self = self.father_
        return solution

    def get_cost(self):
        return self.g_ + self.h_

    def get_level(self):
        current = self
        output = 0
        while (current.father_ != 0):
            output += 1
            current = current.father_
        return output

    def compareState(state1, state2):
        for r1,r2 in zip(state1.robots_,state2.robots_):
            if (r1.color_ == r2.color_ and r1.x_ == r2.x_  and r1.y_ == r2.y_):
                return False
        return True 

    def is_goal_state(self, r, target):
        return r.color_ == target.color_ and r.x_ == target.x_ and r.y_ == target.y_        

    def copyNode(self):
        mt = copy.deepcopy(self.move_tuple_)
        father = copy.deepcopy(self.father_)
        level = self.level_
        robots =[]
        for r in self.robots_:
            robots.append(Robot(r.color_,r.x_,r.y_))
        return Node(robots,father,mt,0,0,level)     
