''' Optimize the easiest model: 2 nodes network through pySOT 
'''
__version__ = '0.1'
__author__ = 'Jianqiu Wang'

import numpy as np


class TwoNodes:
    def __init__(self):
        self.xlow = np.zeros(5)
        self.xup = np.array([10, 10, 10, 1, 1])
        self.dim = 5
        self.min = -1
        self.integer = np.arange(0, 3)
        self.continuous = np.arange(3, 5)

    def eval_ineq_constraints(self, x):
        vec = np.zeros((x.shape[0], 3))
        vec[:, 0] = x[:, 0] + x[:, 2] - 1.6
        vec[:, 1] = 1.333 * x[:, 1] + x[:, 3] - 3
        vec[:, 2] = - x[:, 2] - x[:, 3] + x[:, 4]
        return vec

    def objfunction(self, x):
        if len(x) != self.dim:
            raise ValueError('Dimension mismatch')
        return - x[0] + 3 * x[1] + 1.5 * x[2] + 2 * x[3] - 0.5 * x[4]
        

''' Two-nodes network simulation
    Goal: Determine the optimal base-stock levels setting for the entire system
''' 
''' Pass parameters to simulator '''
''' Inventory parameters'''
BS = [3000, 800]  # Base stock levels （Initial value）
cb = 1            # Unit backorder cost
ch = 1            # Unit inventory holding cost
                  # Reorder period lengths ?? default: 1
Nd = 200          # Simulation horizon
Nw = 100          # Warm-up horizon      ?? Necessary?
''' Probability parameters'''
mean_node2 = 150
std_node2 = 30    # Normal dist of demands for node 2
low_node1 = 2 
high_node1 = 4    # Unif dist of delievry preparation time for node 1
''' Inventory system simulation'''
''' Initialization'''
t = 0
INVP = [0]        # Inventory position at beginning of day 0
INVO = 0        # On-order inventory of node 1 at the beginning of day
# No incoming flow, INVO is always 0
INVB = [0]        # Backorder amount of node 1 at the beginning of day t
INVH = [0]        # on-hand inventory of node 1 at the beginning of day t
OD = [0]          # order amount of node 1 at the beginning of day t
CO = [0]          # customer node order
ROD_21 = [0]      # order received by node 2 from node 1 on day t
state = np.array([0])       # number of days left before order is delivered on day t
''' Simulation starts'''
#while ( t < Nd + Nw ):
while t < 1:
    ''' Inventory operations'''
    ''' 1. Place orders'''
    ''' 1.1 Check inventory position INVP
        if the current period is the starting period of a reviewing cycle:
            generate order OD to desired value
        Since the reorder period is 1, need to check daily
    '''
    INVP.append(INVH[t] + INVO - INVB[t])
    OD.append(BS[0] - INVP[t])
    ''' 1.2 Generate customer node order'''
    CO.append(np.random.normal(mean_node2, std_node2)) # random number of order of node 2
    for idx,item in enumerate(state):
        if item == 1:
            INVH[t] = INVH[t] - OD[idx] # order on day idx will be delievered to node 2
        
    state = np.append(state, np.random.randint(low_node1, high=high_node1))
    print(state)
    ''' 2. Clear shipement task'''
    ''' 2.1 Check if all prepared orders are delivered'''
   
            
    ''' 3. Clear backorders'''
    
    ''' 4. Process orders in queues'''
    
    ''' 5. Schedule shipments'''
    
    ''' 6. Update inventory records'''
    state = state - 1
    ''' 7. Update t'''
    t = t + 1








































