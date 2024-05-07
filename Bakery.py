import gurobipy as gp
from gurobipy import GRB , GurobiError
from Gurobi import RunPLSolution

def optimize_production(profit_coefficients, resource_coefficients, resource_limits, **kwargs):
    default_params = {
        "minimum_production": None,  # Lowered minimum production requirements
        "oven_capacity": None,  # Oven slot usage per unit
        "dietary_restrictions" :None
    }
    # Update default parameter values with provided kwargs
    params = default_params.copy()

    if kwargs is not None:
        params.update(kwargs)

        # Extract parameters
        minimum_production = params["minimum_production"]
        oven_capacity = params["oven_capacity"]
        dietary_restrictions = params["dietary_restrictions"]


    # Create a new model
    model = gp.Model("Production Optimization")

    # Decision Variables
    num_goods = len(profit_coefficients)
    goods = range(num_goods)
    x = model.addVars(goods, vtype=GRB.CONTINUOUS, name="x")

    # Objective Function: Maximize Profit
    model.setObjective(sum(profit_coefficients[i] * x[i] for i in goods), GRB.MAXIMIZE)

    # Constraints: Resource Limitations
    '''for resource_type in range(len(resource_coefficients[0])):
        model.addConstr(sum(resource_coefficients[i][resource_type] * x[i] for i in goods) <= resource_limits[resource_type])'''
    for resource_type in range(len(resource_coefficients)):
        print("Resource type:", len(resource_coefficients))
        print("Length of resource_limits:", len(resource_limits))
        model.addConstr(sum(resource_coefficients[resource_type][i] * x[i] for i in goods) <= resource_limits[resource_type])


    # Constraints: Minimum Production Requirements
    if minimum_production is not None and minimum_production != []:
        for i, min_prod in enumerate(minimum_production):
            model.addConstr(x[i] >= min_prod)

    # Constraints: Oven Capacity
    if oven_capacity is not None and oven_capacity !=[]:
        model.addConstr(sum(oven_capacity[i] * x[i] for i in goods) <= oven_capacity[-1])

    # Constraints: Dietary Restrictions
    if dietary_restrictions is not None:
        model.addConstr(x[1] + x[3] >= dietary_restrictions)
    status,params, res=RunPLSolution(model,x,goods)
    return status,params, res



# Example Data
profit_coefficients = [0.5, 0.4, 0.6, 0.7]  # Profit per unit
resource_coefficients = [[0.1, 0.2, 0.15, 0.25],  # Flour coefficients for each good
                         [0.1, 0.2, 0.15, 0.25],  # Sugar coefficients for each good
                         [0.1, 0.2, 0.15, 0.25]]  # Eggs coefficients for each good
 # Resource usage per unit
resource_limits = [50, 40, 30]  # Flour, Sugar, Eggs
minimum_production = [10, 5, 0, 0]  # Minimum production requirements
oven_capacity = [1, 1, 2, 2, 6]  # Oven slot usage per unit
dietary_restrictions = 10  # Minimum number of gluten-free items
'''
# Adjusted Example Data
profit_coefficients = [0.5, 0.4, 0.6, 0.7]  # Profit per unit
resource_coefficients = [[0.1, 0.2, 0.15, 0.25],  # Flour coefficients for each good
                        [0.1, 0.2, 0.15, 0.25],  # Sugar coefficients for each good
                        [0.1, 0.2, 0.15, 0.25]]  # Eggs coefficients for each good
resource_limits = [100, 80, 60]  # Increased resource limits for Flour, Sugar, Eggs
#optinal
minimum_production = [5, 2, 0, 0]  # Lowered minimum production requirements
oven_capacity = [1, 1, 2, 2, 6000]  # Oven slot usage per unit
dietary_restrictions = 5  # Lowered dietary restrictions
'''
# Solve
status,params, res =optimize_production(profit_coefficients, resource_coefficients, resource_limits)
# with optimal
status,params, res =optimize_production(profit_coefficients, resource_coefficients, resource_limits, minimum_production=minimum_production, oven_capacity=oven_capacity, dietary_restrictions=dietary_restrictions)
