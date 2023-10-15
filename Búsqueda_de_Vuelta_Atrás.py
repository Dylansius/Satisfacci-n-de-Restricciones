def backtracking_search(csp):
    return recursive_backtracking({}, csp)

def recursive_backtracking(assignment, csp):
    if len(assignment) == len(csp.variables):
        return assignment
    
    var = select_unassigned_variable(assignment, csp)
    for value in order_domain_values(var, assignment, csp):
        if is_consistent(var, value, assignment, csp):
            assignment[var] = value
            result = recursive_backtracking(assignment, csp)
            if result is not None:
                return result
            del assignment[var]
    return None

# Implementa las funciones select_unassigned_variable, order_domain_values, is_consistent según tus necesidades.

# Ejemplo de uso:
problem = ...  # Define el CSP como en el ejemplo anterior
solution = backtracking_search(problem)
print("Solucion encontrada:", solution)

