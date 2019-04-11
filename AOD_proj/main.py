from __future__ import print_function
from ortools.linear_solver import pywraplp

value = [2, 2, 3]
weight = [1, 2, 2]
size_constraint = 3


def main():
  solver = pywraplp.Solver('SolveSimpleSystem',
                           pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

  numVariables = []

  objective = solver.Objective()
  weight_constraint = solver.Constraint(0,size_constraint)

  for i in range(3):
      numVar = solver.NumVar(0, 1, 'x{}'.format(i))
      constraint = solver.Constraint(0, 1)
      constraint.SetCoefficient(numVar, 1)
      weight_constraint.SetCoefficient(numVar, weight[i])
      numVariables.append(numVar)
      objective.SetCoefficient(numVar,value[i])


  objective.SetMaximization()
  solver.Solve()
  print('Solution:')
  print('1 = ', numVariables[0].solution_value())
  print('2 = ', numVariables[1].solution_value())
  print('3 = ', numVariables[2].solution_value())

if __name__ == '__main__':
  main()