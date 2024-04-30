import gurobipy as gp
from gurobipy import GRB

def optimize_bakery_location(I, J, Q, C, D, Dmax, DB, Dmin, time_limit):
    # Initialize the model
    model = gp.Model("Bakery_Location")

    # Decision variables
    x = {}
    for j in range(len(J)):
        x[j] = model.addVar(vtype=GRB.BINARY, name=f"x[{j}]")

    # Generate matrices A and B based on distances
    A = {(i, j): 1 if D[i][j] < Dmax else 0 for i in I for j in J}
    B = {(j, k): 1 if DB[j][k] < Dmin else 0 for j in range(len(J)) for k in range(len(J))}

    # Objective function: minimize total installation costs
    model.setObjective(gp.quicksum(C[j] * x[j] for j in J), GRB.MINIMIZE)

    # Constraints
    # Constraint 1: Maximum capacity per bakery
    for i in I:
        model.addConstr(gp.quicksum(A[i, j] * x[j] for j in J) <= Q[i], name=f"capacity_{i}")

    # Constraint 2: Demand satisfaction for each neighborhood
    for j in J:
        model.addConstr(gp.quicksum(A[i, j] * x[j] for i in I) >= 1, name=f"demand_{j}")

    # Constraint 3: Only one bakery per location
    for j in J:
        model.addConstr(x[j] <= 1, name=f"location_{j}")

    # Constraint 4: Minimum distance between two bakeries
    for j in range(len(J)):
        model.addConstr(gp.quicksum(B[j, k] * x[k] for k in range(len(J)) if k != j) <= (1 - x[j]), name=f"distance_{j}")

    # Set time limit for optimization
    model.Params.TimeLimit = time_limit

    # Optimize the model
    model.optimize()

    # Get the solution
    solution = {}
    if model.status == GRB.OPTIMAL:
        print("Optimal solution found:")
        for j in J:
            if x[j].x > 0.5:
                solution[j] = True
                print(f"Bakery at location {j}")
            else:
                solution[j] = False
    else:
        print("No optimal solution found. Returning best feasible solution found so far:")
        for j in J:
            if x[j].x > 0.5:
                solution[j] = True
                print(f"Bakery at location {j}")
            else:
                solution[j] = False

    return solution

# Define the data
I = ['Neighborhood A', 'Neighborhood B', 'Neighborhood C']  # Set of neighborhoods
J = ['Location 1', 'Location 2', 'Location 3']  # Set of locations
Q = {'Neighborhood A': 100, 'Neighborhood B': 150, 'Neighborhood C': 200}  # Maximum capacity for each bakery
C = {'Location 1': 50000, 'Location 2': 60000, 'Location 3': 70000}  # Cost of installing a bakery at each location
D = {
    'Neighborhood A': {'Location 1': 5, 'Location 2': 8, 'Location 3': 10},
    'Neighborhood B': {'Location 1': 7, 'Location 2': 6, 'Location 3': 9},
    'Neighborhood C': {'Location 1': 9, 'Location 2': 7, 'Location 3': 5}
}  # Distance between neighborhood i and location j
Dmax = 8  # Maximum distance between a neighborhood and its nearest bakery
# Define the distance matrix
DB = [[0 for _ in range(len(I))] for _ in range(len(I))]

# Define the distances between locations
distance_data = {
    ('Location 1', 'Location 2'): 15,
    ('Location 1', 'Location 3'): 20,
    ('Location 2', 'Location 3'): 10,
    ('Location 2', 'Location 1'): 15,  # Add reverse distances if necessary
    ('Location 3', 'Location 1'): 20,
    ('Location 3', 'Location 2'): 10
}

# Update the distance matrix with actual distance values
for i, loc1 in enumerate(I):
    for j, loc2 in enumerate(I):
        if (loc1, loc2) in distance_data:
            DB[i][j] = distance_data[(loc1, loc2)]
            DB[j][i] = distance_data[(loc1, loc2)]  # If distances are symmetric

 # Distance between bakery j and bakery k
Dmin = 10  # Minimum distance between two bakeries
time_limit = 60  # Time limit for optimization (in seconds)


# Solve the problem
solution = optimize_bakery_location(I, J, Q, C, D, Dmax, DB, Dmin, time_limit)
