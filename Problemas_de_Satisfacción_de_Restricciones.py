from constraint import *

problem = Problem()

problem.addVariable('A', [1, 2, 3])
problem.addVariable('B', [2, 3, 4])
problem.addVariable('C', [3, 4, 5])

def constraint_function(a, b, c):
    return a + b == c

problem.addConstraint(constraint_function, ('A', 'B', 'C'))

solutions = problem.getSolutions()
print("Soluciones CSP:")
for solution in solutions:
    print(solution)

