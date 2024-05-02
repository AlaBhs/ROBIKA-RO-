from gurobipy import GRB , GurobiError
def get_status_description(status_code):
    status_dict = {
        1: "Model is loaded, but no solution information is available.",
        2: "Model was solved to optimality (subject to tolerances), and an optimal solution is available.",
        3: "Model was proven to be infeasible.",
        4: "Model was proven to be either infeasible or unbounded. To obtain a more definitive conclusion, set the DualReductions parameter to 0 and reoptimize.",
        5: "Model was proven to be unbounded. Important note: an unbounded status indicates the presence of an unbounded ray that allows the objective to improve without limit. It says nothing about whether the model has a feasible solution. If you require information on feasibility, you should set the objective to zero and reoptimize.",
        6: "Optimal objective for model was proven to be worse than the value specified in the Cutoff parameter. No solution information is available.",
        7: "Optimization terminated because the total number of simplex iterations performed exceeded the value specified in the IterationLimit parameter, or because the total number of barrier iterations exceeded the value specified in the BarIterLimit parameter.",
        8: "Optimization terminated because the total number of branch-and-cut nodes explored exceeded the value specified in the NodeLimit parameter.",
        9: "Optimization terminated because the time expended exceeded the value specified in the TimeLimit parameter.",
        10: "Optimization terminated because the number of solutions found reached the value specified in the SolutionLimit parameter.",
        11: "Optimization was terminated by the user.",
        12: "Optimization was terminated due to unrecoverable numerical difficulties.",
        13: "Unable to satisfy optimality tolerances; a sub-optimal solution is available.",
        14: "An asynchronous optimization call was made, but the associated optimization run is not yet complete.",
        15: "User specified an objective limit (a bound on either the best objective or the best bound), and that limit has been reached.",
        16: "Optimization terminated because the work expended exceeded the value specified in the WorkLimit parameter.",
        17: "Optimization terminated because the total amount of allocated memory exceeded the value specified in the SoftMemLimit parameter."
    }
    return status_dict.get(status_code, "Unknown status code")
def RunPLSolution (model,x,num,attempts=3):
    # Solve
    model.optimize()
    #check Status code
    status= get_status_description(model.Status) 
    Optimal_solution=[]
    ###########

    # Print solution
    if model.status == GRB.OPTIMAL:
        print("Optimal Solution:")
        for i in num:
            Optimal_solution.append(x[i].x)
            print(f"Number of goods produced for item {i+1}: {x[i].x}")
        print(f"Total Profit: {model.objVal}")
        return status, Optimal_solution, model.objVal
    elif model.status == GRB.INFEASIBLE:
        try:
                # Compute the Irreducible Inconsistent Subsystem (IIS)
                model.computeIIS()

                if model.IISMinimal:
                    print("IIS computed successfully. The following constraints are infeasible together:")
                    for constr in model.getConstrs():
                        if constr.IISConstr:
                            print(f"- {constr.ConstrName}:{model.getRow(constr)}")
                else:
                    print("No IIS found. The model may be feasible after all.")
        except GurobiError as e:
                print("Error computing IIS:", e)
        return status,Optimal_solution, None
    elif model.status == GRB.INF_OR_UNBD:
        if attempts > 0:
            model.setParam('DualReductions', 0)
            return RunPLSolution(model, x, num, attempts - 1)
        else:
            print("Maximum attempts reached. Exiting.")
            return status, Optimal_solution, None
    elif model.status == GRB.UNBOUNDED:
        print("Model is unbounded.")
        return status,Optimal_solution, None
    else:   
        # Check if solution is feasible
        print("No feasible solution found.")
        # Print violated constraints
        for constr in model.getConstrs():
            try:
                if constr.Slack < 0:
                    print(f"Constraint '{constr.ConstrName}' is violated by {-constr.Slack}.")
            except AttributeError:
                continue
            
            try:
                constr_expr = model.getRow(constr)
                lhs = sum(constr_expr.getCoeff(j) * x[j].X for j in num)
                if lhs > constr.RHS:
                    print(f"Constraint '{constr.ConstrName}' is violated by {lhs - constr.RHS}.")
            except AttributeError:
                continue

        return status,Optimal_solution, None
def RunBinaryPLSolution (model,J,x,num,attempts=3):
    # Solve
    model.optimize()
    #check Status code
    status= get_status_description(model.Status) 
    ###########

    # Print solution
    solution = {}
    if model.status == GRB.OPTIMAL:
        print("Optimal solution found:")
        for j in range(num):
            if x[j].x > 0.5:
                solution[J[j]] = True
                print(f"Bakery at location {J[j]}")
            else:
                solution[J[j]] = False
        return status, solution, None
        
    elif model.status == GRB.INFEASIBLE:
        try:
                # Compute the Irreducible Inconsistent Subsystem (IIS)
                model.computeIIS()

                if model.IISMinimal:
                    print("IIS computed successfully. The following constraints are infeasible together:")
                    for constr in model.getConstrs():
                        if constr.IISConstr:
                            print(f"- {constr.ConstrName}:{model.getRow(constr)}")
                else:
                    print("No IIS found. The model may be feasible after all.")
        except GurobiError as e:
                print("Error computing IIS:", e)
        return status,solution, None
    elif model.status == GRB.INF_OR_UNBD:
        if attempts > 0:
            model.setParam('DualReductions', 0)
            return RunBinaryPLSolution(model,J, x, num, attempts - 1)
        else:
            print("Maximum attempts reached. Exiting.")
            return status, solution, None
    elif model.status == GRB.UNBOUNDED:
        print("Model is unbounded.")
        return status,solution, None
    else:   
        # Check if solution is feasible
        print("No feasible solution found.")
        # Print violated constraints
        for constr in model.getConstrs():

            try:
                if constr.Slack < 0:
                    print(f"Constraint '{constr.ConstrName}' is violated by {-constr.Slack}.")
            except AttributeError:
                continue
            
            try:
                constr_expr = model.getRow(constr)
                lhs = sum(constr_expr.getCoeff(j) * x[j].X for j in num)
                if lhs > constr.RHS:
                    print(f"Constraint '{constr.ConstrName}' is violated by {lhs - constr.RHS}.")
            except AttributeError:
                continue

        return status,solution, None
