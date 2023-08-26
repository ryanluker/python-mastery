# pcost.py
# read in data file and perform cost multiplication.
# contains a single helper function for achieving the above.

def portfolio_cost(filename):
    total_equity = 0
    relative_path = "../../"
    with open(relative_path + filename, "r") as f:
        for company in f:
            # process company info by splitting on empty string
            values = company.split()
            shares = int(values[1])
            price = float(values[2])
            total_equity += (shares * price)

    return total_equity

