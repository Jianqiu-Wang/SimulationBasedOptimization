
#!/usr/bin/python
# encoding: utf-8
import numpy as np
import matplotlib.pyplot as plt
from queue import *
import pdb
 
class Facility:
    ''' Class of facilities'''
    facilityCount = 0
    def __init__(self, name, mean, std, lowb, upb, inv_onhand, inv_pos, rp, oq, root):
	    
        self.name = name
        self.mean = mean
        self.std = std
        self.lowb = lowb
        self.upb = upb
        self.inv_onhand = inv_onhand
        self.inv_pos = inv_pos
        self.rp = rp     # reorder point
        self.oq = oq     # order quantity
        self.root = root # rootof this node
        Facility.facilityCount += 1

    def invSend(self, amount):
        ''' Deliver to customer, substract corresponding inventory amount '''
        self.inv_onhand -= amount
        self.inv_pos -= amount

    def orderPlaced(self, amount):
    	self.inv_pos += self.oq

    def orderArrive(self):
    	self.inv_onhand += self.oq
    	#self.inv_pos += self.oq
    
class facilityOrder:
    ''' Order generated from each facility has various processing time.
    Hence we build a class to track this characteristic '''
    ''' Order processing time, uniform distribution '''
    def __init__(self, fac_from, fac_to, lowb, upb, daystoArrive):
        self.fac_from = fac_from
        self.fac_to = fac_to
        self.lowb = lowb
        self.upb = upb
        self.daystoArrive = daystoArrive
    
    def generateDays(self):
    	self.daystoArrive = np.random.randint(self.lowb, self.upb+1)

    def generateAmount(self, amount):
        self.amount = amount

class customerOrder:
	def __init__(self, amount):
		self.amount = amount

# Instances of class facilities, describing network structure
fac0 = Facility('fac0', 0, 0, 0, 0, 0, 0, 0, 0, None)
fac1 = Facility('fac1', 1000, 500, 10, 15, 0, 0, 40000, 40000, fac0)
#fac1.lowb = 10; fac1.upb = 15;
fac2 = Facility('fac2', 600, 400, 4, 8, 0, 0, 6000, 8000, fac1)
#fac2.lowb = 4; fac2.upb = 8;
fac3 = Facility('fac3', 500, 300, 5, 10, 0, 0, 5000, 7000, fac1)
#fac3.lowb = 5; fac3.upb = 10;
fac4 = Facility('fac4', 400, 300, 4, 10, 0, 0, 8000, 6000, fac1)
#fac4.lowb = 4; fac4.upb = 10;

# Instances of class customer Order, track amount of customer order
c_order1 = customerOrder(0) 
c_order2 = customerOrder(0) 
c_order3 = customerOrder(0) 
c_order4 = customerOrder(0) 

# Instances of class facilityOrder
facorder1 = facilityOrder(fac0, fac1, 10, 15,-100) # facility 0 with infite inventory
facorder2 = facilityOrder(fac1, fac2, 4, 8, -100)
facorder3 = facilityOrder(fac1, fac3, 5, 10, -100)
facorder4 = facilityOrder(fac1, fac4, 4, 10, -100) 

T = 365
t = 0
serviceLevel = 0.95
facilities = [fac1, fac2, fac3, fac4]

# Initilize facility orders, keep track of it
facility_orders = []
orderinQueue = [Queue(0), Queue(0), Queue(0), Queue(0)]
back_orders = []
num_backorder = [0, 0, 0, 0]
total_order = [0, 0, 0, 0]
inv_onhand = []
inv_pos = []
#debug
# Simulation

while (t < T) :
	# Keep tracking of all facility orders 
    #print(len(facility_orders))
    if facility_orders:                       # facility_orders list is not empty
        for i, facorder in enumerate(facility_orders):
            facorder.daystoArrive -= 1         # update days to arrive facilities
            if(facorder.daystoArrive == 0):
                facorder.fac_to.orderArrive()
                facility_orders.remove(facorder)  
	# Generate daily customer demand for each facility 
    customer_orders = [c_order1, c_order2, c_order3, c_order4]
    
    # Deal with customer order
    for i, fac in enumerate(facilities):
        # Generate customer order until it is valid( greater than 0)
        while (customer_orders[i].amount <= 0):       
            customer_orders[i].amount = np.random.normal(fac.mean, fac.std)
        
        # Deal with order in Queue
        while orderinQueue[i]:
            if fac.inv_onhand > orderinQueue.get().amount:
                


        # Place order if there exist enough on-hand inventory
        if fac.inv_onhand > customer_orders[i].amount:
            print('Customer order placed!')
            fac.invSend(customer_orders[i].amount)
        else:
            print('Customer')
            orderinQueue[i].put(customer_orders[i])

        # If inventory position is less than reorder point, reorder immediately
        if fac.inv_pos < fac.rp:
            target = fac.root  
            
            # Generate new order
            neworder = facilityOrder(target, fac, target.lowb, target.upb, 0)
            neworder.generateDays()
            neworder.generateAmount(fac.oq)

            if target == fac0:
                fac.orderPlaced(fac.oq)
                facility_orders.append(neworder)
            else: 
                if target.inv_onhand > fac.oq:
                    fac.orderPlaced(fac.oq)     
                    target.invSend(fac.oq)
                    facility_orders.append(neworder)
                else:
                    print('Unsasified order for facility! -- Back order')
                    orderinQueue[0].put(neworder)
                    #count 
	# Update time
    t += 1
    #inv_onhand.append([fac1.inv_onhand, fac2.inv_onhand,
     #                  fac3.inv_onhand, fac4.inv_onhand])
    inv_onhand.append([fac1.inv_onhand, fac2.inv_onhand,
                       fac3.inv_onhand, fac4.inv_onhand])
    inv_pos.append([fac1.inv_onhand, fac2.inv_pos, 
                    fac3.inv_pos, fac4.inv_pos])
    #print(inv_onhand)

#plt.plot(range(T), inv_onhand)
#plt.plot(range(T), inv_pos)
#plt.show()
