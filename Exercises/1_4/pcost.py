# pcost.py
# read in data file and perform cost multiplication

import pprint

company_dict = {}
with open("../../Data/portfolio.dat", "r") as f:
    for company in f:
        # process company info by splitting on empty string
        values = company.strip("\n").split(" ")
        # constructs a dict obj of key values
        # ticker: {shares: int, price: float}
        ticker = values[0]
        shares = int(values[1])
        price = float(values[2])
        total_equity = round(shares * price, 2)
        company_dict[ticker] = {
            "shares": shares,
            "price": price,
            "total_equity": total_equity
        }

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(company_dict)

# Compute total portfolio equity and print
total_port_equity = 0
for company in company_dict.values():
    total_port_equity += company.get("total_equity")

pp.pprint(total_port_equity)

