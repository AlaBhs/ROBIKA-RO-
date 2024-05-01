import gurobipy as gp
from gurobipy import GRB
import numpy as np

def optimize_bakery_location(I, J, Q, C, D, Dmax, DB, Dmin, time_limit):
    # Initialize the model
    model = gp.Model("Bakery_Location")

    # Decision variables
    x = {}
    for j in range(len(J)):
        x[j] = model.addVar(vtype=GRB.BINARY, name=f"x[{j}]")

    # Generate matrices A and B based on distances
    A = np.array([[1 if D[i, j] < Dmax else 0 for j in range(len(J))] for i in range(len(I))])
    B = np.array([[1 if DB[j, k] < Dmin else 0 for k in range(len(J))] for j in range(len(J))])

    # Objective function: minimize total installation costs
    model.setObjective(gp.quicksum(C[j] * x[j] for j in range(len(J))), GRB.MINIMIZE)

    # Constraints
    # Constraint 1: Maximum capacity per bakery
    for i in range(len(I)):
        model.addConstr(gp.quicksum(A[i, j] * x[j] for j in range(len(J))) <= Q[i], name=f"capacity_{I[i]}")

    # Constraint 2: Demand satisfaction for each neighborhood
    for j in range(len(J)):
        model.addConstr(gp.quicksum(A[i, j] * x[j] for i in range(len(I))) >= 1, name=f"demand_{J[j]}")

    # Constraint 3: Only one bakery per location
    for j in range(len(J)):
        model.addConstr(x[j] <= 1, name=f"location_{J[j]}")

    # Constraint 4: Minimum distance between two bakeries
    for j in range(len(J)):
        model.addConstr(gp.quicksum(B[j, k] * x[k] for k in range(len(J)) if k != j) <= (1 - x[j]), name=f"distance_{J[j]}")

    # Set time limit for optimization
    model.Params.TimeLimit = time_limit

    # Optimize the model
    model.optimize()

    # Get the solution
    solution = {}
    if model.status == GRB.OPTIMAL:
        print("Optimal solution found:")
        for j in range(len(J)):
            if x[j].x > 0.5:
                solution[J[j]] = True
                print(f"Bakery at location {J[j]}")
            else:
                solution[J[j]] = False
    else:
        print("No optimal solution found. Returning best feasible solution found so far:")
        for j in range(len(J)):
            if x[j].x > 0.5:
                solution[J[j]] = True
                print(f"Bakery at location {J[j]}")
            else:
                solution[J[j]] = False

    return solution

# Define the data
I = ['Neighborhood A', 'Neighborhood B', 'Neighborhood C']  # Set of neighborhoods
J = ['Location 1', 'Location 2', 'Location 3']  # Set of locations
Q = [100, 150, 200]  # Maximum capacity for each bakery
C = [50000, 60000, 70000]  # Cost of installing a bakery at each location
D_dict = {
    'Neighborhood A': {'Location 1': 5, 'Location 2': 8, 'Location 3': 10},
    'Neighborhood B': {'Location 1': 7, 'Location 2': 6, 'Location 3': 9},
    'Neighborhood C': {'Location 1': 9, 'Location 2': 7, 'Location 3': 5}
}  # Distance between neighborhood i and location j
Dmax = 8  # Maximum distance between a neighborhood and its nearest bakery

# Define the distance matrix
D = np.zeros((len(I), len(J)))

# Fill the matrix with values from the dictionary
for i, neighborhood in enumerate(I):
    for j, location in enumerate(J):
        D[i, j] = D_dict[neighborhood][location]

# Define the distances between locations
distance_data = {
    ('Location 1', 'Location 2'): 15,
    ('Location 1', 'Location 3'): 20,
    ('Location 2', 'Location 3'): 10,
    ('Location 2', 'Location 1'): 15,  # Add reverse distances if necessary
    ('Location 3', 'Location 1'): 20,
    ('Location 3', 'Location 2'): 10
}

# Define the distance matrix between locations
DB = np.zeros((len(J), len(J)))

# Update the distance matrix with actual distance values
for i, loc1 in enumerate(J):
    for j, loc2 in enumerate(J):
        if (loc1, loc2) in distance_data:
            DB[i, j] = distance_data[(loc1, loc2)]
            DB[j, i] = distance_data[(loc1, loc2)]  # If distances are symmetric

Dmin = 10  # Minimum distance between two bakeries
time_limit = 60  # Time limit for optimization (in seconds)

# Solve the problem
solution = optimize_bakery_location(I, J, Q, C, D, Dmax, DB, Dmin, time_limit)
print(solution)
