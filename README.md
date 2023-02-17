# monte_carlo
An example of Monte-Carlo simulation in an inventory use-case

BathBunny Soap Case
Management of BathBunny* (BB), a leading bath soap manufacturer, is trying to control its inventory costs. The marketing department estimates that weekly demand is between 80k and 160k cases (all numbers are equally probable). If demand exceeds the amount of soap on hand, those sales are lost—that is, there is no backlogging of demand. The production department can produce at one of three levels: 110k, 120k, or 130k cases per week. Management would like to evaluate the following production policy: If the current inventory is less than L = 30k cases, produce 130k cases in the next week. If the current inventory exceeds U = 80k cases, produce 110k cases in the next week. Otherwise, BB will produce 120k cases in the next week.
The annual cost can be defined as the sum of the inventory cost, the opportunity cost, and the cost of production level change. The weekly cost of holding a case of soap in inventory is 3 cents. The approximate opportunity cost for every unit of lost demand is $1. Changing the production level from one week to the next costs $3000.
At the beginning of 2023, BB has 60k cases of inventory, and the production level for the first week is 120k.
Develop a simulation model for 52 weeks of operation at BB. Graph the soap inventory over time for one replication (realization) of the simulation model. Find the annual cost.
Run this model 500 times to estimate the average annual cost. Report the sample mean and standard deviation of the annual cost. Construct a 95% confidence interval for the annual cost. Plot the distribution of annual cost based on 500 iterations. 
