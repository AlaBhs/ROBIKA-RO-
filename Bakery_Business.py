import gurobipy as gp
from gurobipy import GRB
import random

def solve_bakery_production(p, f, s, e, F, S, E, **kwargs):
    """Solves the bakery production optimization problem."""
    # Define default values for optional arguments
    default_values = {
        "w":[1,1,1,1],
        "o": None,
        "t": None,
        "M": None,
        "G": None,
        "O": None,
        "T":None,
        "time_limit":60
    }
    # Default constraints
    default_constraints = {
        "resource_limitations": False,
        "min_production_requirements": False,
        "oven_capacity": False,
        "dietary_restrictions": False,
        "production_time": True 
    }

    # If constraints are provided, update the default constraints
    if kwargs is not None:
        default_constraints.update(kwargs.get('constraints', {}))
        # Assign default values only if the corresponding keys are not present in kwargs
        w = kwargs.get('w', default_values['w'])
        o = kwargs.get('o', default_values['o'])
        t = kwargs.get('t', default_values['t'])
        M = kwargs.get('M', default_values['M'])
        G = kwargs.get('G', default_values['G'])
        O = kwargs.get('O', default_values['O'])
        T = kwargs.get('T', default_values['T'])
    # Extract constraint values
    oven_capacity = default_constraints["oven_capacity"]
    production_time = default_constraints["production_time"]
    min_production_requirements = default_constraints["min_production_requirements"]
    dietary_restrictions = default_constraints["dietary_restrictions"]
    resource_limitations = default_constraints["resource_limitations"]


    # Create a new model
    model = gp.Model("BakeryProduction")

    # Decision variables
    num_goods = len(p)
    x = model.addVars(num_goods, name="x")

    # Objective function
    model.setObjective(sum(p[i] * w[i] * x[i] for i in range(num_goods)), GRB.MAXIMIZE)

    # Resource Limitations
    if resource_limitations:
        model.addConstr(sum(f[i] * x[i] for i in range(num_goods)) <= F)
        model.addConstr(sum(s[i] * x[i] for i in range(num_goods)) <= S)
        model.addConstr(sum(e[i] * x[i] for i in range(num_goods)) <= E)

    # Minimum Production Requirements
    if min_production_requirements and M is not None:
        for i in range(num_goods):
            model.addConstr(x[i] >= M[i])

    # Oven Capacity
    if oven_capacity and o is not None:
        model.addConstr(sum(o[i] * x[i] for i in range(num_goods)) <= O)

    # Dietary Restrictions
    if dietary_restrictions and G is not None:
        model.addConstr(x[1] + x[3] >= G)

    # Production Time Constraint
    if production_time and t is not None and T is not None:
        t_total = sum(t[i] * x[i] for i in range(num_goods))
        model.addConstr(t_total <= T)


    # Set time limit for optimization
    model.Params.TimeLimit = default_values["time_limit"]

    # Solve the optimization problem
    model.optimize()

    # Check optimization status
    if model.status == GRB.OPTIMAL:
        print("Optimal solution found:")
        solution = [x[i].X for i in range(num_goods)]
        for i in range(num_goods):
            print(f"Quantity of Product {i+1}: {solution[i]}")
        return True, solution
    elif model.status == GRB.TIME_LIMIT:
        print("Time limit reached. Returning best feasible solution found so far:")
        solution = [x[i].X for i in range(num_goods)]
        for i in range(num_goods):
            print(f"Quantity of Product {i+1}: {solution[i]}")
        return True, solution
    else:
        print("No feasible solution found.")
        return False, []

def generate_random_params():
    """Generate random parameters for the bakery production problem."""
    # Define ranges for random parameters
    param_ranges = {
        "p": (5, 15),  # Profit per unit for each product
        "w": (0.5, 1.5),  # Weighting factors for each product
        "f": (0.5, 2),  # Flour required per unit for each product
        "s": (0.5, 1.5),  # Sugar required per unit for each product
        "e": (1, 3),  # Eggs required per unit for each product
        "F": (500, 1500),  # Available flour
        "S": (2500, 7500),  # Available sugar
        "E": (300, 900),  # Available eggs
        "M": (5, 25),  # Minimum production requirements
        "G": (5, 15),  # Gluten-free option requirement
        "O": (3, 7),  # Oven capacity
        "T": (4, 10)  # Available time
    }

    # Generate random parameters within defined ranges
    params = {}
    for param, (lower, upper) in param_ranges.items():
        if param in ["p", "w", "f", "s", "e"]:
            params[param] = [random.uniform(lower, upper) for _ in range(4)]
        else:
            params[param] = random.uniform(lower, upper)
    return params
def solve_bakery_production_randomly(max_attempts=10):
    """Solves the bakery production optimization problem with random parameters."""
    attempts = 0
    while attempts < max_attempts:
        params = generate_random_params()
        print("Generated random parameters:", params)
        # Try solving the problem with the generated parameters
        state, result = solve_bakery_production(**params)
        # If the solution is optimal, return
        if state:
            print (result)
            return
        print("No optimal solution found. Generating new parameters...")
        attempts += 1
    print(f"Maximum number of attempts ({max_attempts}) reached. No optimal solution found.")


solve_bakery_production_randomly()

'''
# Define problem data
p = [10, 12, 8, 9]  # Profit per unit for each product
w = [1, 1.2, 0.8, 1]  # Weighting factors for each product
f = [1, 1.5, 2, 1.75]  # Flour required per unit for each product
s = [0.5, 0.75, 1, 0.8]  # Sugar required per unit for each product
e = [2, 2, 3, 2.5]  # Eggs required per unit for each product
o = [1, 1, 2, 2]  # Oven slots required per unit for each product
t = [0.5, 0.6, 0.7, 0.8]  # Production time per unit for each product
F = 100  # Available flour
S = 50  # Available sugar
E = 60  # Available eggs
M = [20, 15, 0, 0]  # Minimum production requirements
G = 10  # Gluten-free option requirement
O = 5  # Oven capacity
T=8 #available time
activate_constraints = {
    "resource_limitations": False,
    "min_production_requirements": False,
    "oven_capacity": False,
    "dietary_restrictions": False,
    "production_time": True 

}

# Solve the problem
solve_bakery_production(p, f, s, e, F, S, E)
'''