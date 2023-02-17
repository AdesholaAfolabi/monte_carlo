import numpy as np
import matplotlib.pyplot as plt

# Initialize variables
num_replications = 500
num_weeks = 52
init_inventory = 60000
init_production_level = 120000
L = 30000
U = 80000
holding_cost = 0.03
opportunity_cost = 1.0
change_cost = 3000.0

# Define functions to calculate inventory level and production level for each week
def calc_inventory_level(demand, inventory, production):
    actual_demand = min(demand, inventory)
    return max(0, inventory - actual_demand + production)

def calc_production_level(inventory):
    if inventory < L:
        return 130000
    elif inventory > U:
        return 110000
    else:
        return 120000

# Initialize arrays to store results
inventory_levels = np.zeros((num_replications, num_weeks))
annual_costs = np.zeros(num_replications)

# Run the simulation model
for i in range(num_replications):
    inventory = init_inventory
    production_level = init_production_level
    for j in range(num_weeks):
        demand = np.random.randint(80000, 160000)
        inventory = calc_inventory_level(demand, inventory, production_level)
        production_level = calc_production_level(inventory)
        inventory_levels[i][j] = inventory
        holding_cost_weekly = holding_cost * inventory
        opportunity_cost_weekly = opportunity_cost * max(0, demand - inventory)
        if j == 0:
            change_cost_weekly = 0
        else:
            change_cost_weekly = change_cost * (abs(production_level - prev_production_level) / 1000.0)
        prev_production_level = production_level
        weekly_cost = holding_cost_weekly + opportunity_cost_weekly + change_cost_weekly
        annual_costs[i] += weekly_cost
    annual_costs[i] *= 52

# Calculate sample mean and standard deviation of annual cost
sample_mean = np.mean(annual_costs)
sample_stddev = np.std(annual_costs, ddof=1)

# Calculate 95% confidence interval for annual cost
conf_interval = (sample_mean - 1.96 * (sample_stddev / np.sqrt(num_replications)),
                 sample_mean + 1.96 * (sample_stddev / np.sqrt(num_replications)))

# Plot inventory levels over time for one replication
plt.plot(inventory_levels[0])
plt.xlabel('Week')
plt.ylabel('Inventory (Cases)')
plt.title('Inventory Levels over Time for One Replication')
plt.show()

# Plot histogram of annual costs
plt.hist(annual_costs, bins=20)
plt.xlabel('Annual Cost ($)')
plt.ylabel('Frequency')
plt.title('Distribution of Annual Costs based on 500 Iterations')
plt.show()

# Print sample mean, sample standard deviation, and 95% confidence interval for annual cost
print('Sample mean of annual cost: ${:,.2f}'.format(sample_mean))
print('Sample standard deviation of annual cost: ${:,.2f}'.format(sample_stddev))
print('95% confidence interval for annual cost: (${:,.2f}, ${:,.2f})'.format(conf_interval[0], conf_interval[1]))
