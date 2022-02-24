from copy import deepcopy

from AbstractSolver import Solver


class NaiveSolver(Solver):
    def solve(self, contributors, projects):
        contributors, projects = map(deepcopy, [contributors, projects])

