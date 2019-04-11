from __future__ import print_function
from ortools.linear_solver import pywraplp


def binPacking(weight, bincapicity, maxBins , debug = False):
  solver = pywraplp.Solver('SolveSimpleSystem',
                           pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)#BOP_INTEGER_PROGRAMMING)

  numVariables = []

  objective = solver.Objective()

  for binIdx in range(maxBins):
      binConstraint = solver.Constraint(0, bincapicity)
      items = []
      for i in range(len(weight)):
          var = solver.Var(0, 1, True, name='bin{}_item{}'.format(binIdx, i))
          binConstraint.SetCoefficient(var, weight[i])
          items.append(var)
          objective.SetCoefficient(var, weight[i] / bincapicity * (1 << binIdx))
      numVariables.append(items)

  for i in range(len(weight)):
      itemConstraint = solver.Constraint(1, 1)
      for binIdx in range(maxBins):
          itemConstraint.SetCoefficient(numVariables[binIdx][i], 1)


  objective.SetMinimization()

  solver.Solve()

  if debug:
    print('Weight:')
    for w in weight:
      print("{} ".format(w), end="")
    print()

    print('Solution:')
    for binIdx in range(maxBins):
      print("bin_{} ".format(binIdx), end="")
      for i in range(len(weight)):
          print("{} ".format(numVariables[binIdx][i].solution_value()), end="")
      print()

  usedBins = 0;
  for binIdx in range(maxBins):
      value = 0
      for i in range(len(weight)):
          value += numVariables[binIdx][i].solution_value()
      if value > 0:
        usedBins += 1

  return usedBins

if __name__ == '__main__':
    weight = [1, 2, 2]
    bincapicity = 2
    maxBins = 20
    binPacking(weight, bincapicity, maxBins)