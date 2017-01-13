#!/usr/bin/python
import numpy as np

class Facility:
    ''' Class of facilities'''
    facilityCount = 0
    def __init__(self, mean, std, inv_onhand, inv_pos, rp, oq, root):
	    ''' Customer demand parameter for facilities, mean and standard deviation '''
	    self.mean = mean
	    self.std = std
	    self.inv_onhand = inv_onhand
	    self.inv_pos = inv_pos
	    self.rp = rp     # reorder point
	    self.oq = oq     # order quantity
	    self.root = root # rootof this node
	    # (r,q) policy: when the inventory position is below the reorder point R, 
	    # a fixed order quantity q is placed immediately
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

    #def facilityOrder(self, daystoArrive)

    #def placeOrder(self, daystoArrive)
    ''' Place order to replenish inventory '''
        
class facilityOrder:
    ''' Order generated from each facility has various processing time.
    Hence we build a class to track this characteristic '''
    ''' Order processing time, uniform distribution '''
    def __init__(self, fac_from, fac_to, lowb, upb, daystoArrive=0):
        self.fac_from = fac_from
        self.fac_to = fac_to
        self.lowb = lowb
        self.upb = upb
        self.daystoArrive = daystoArrive
    
    def generateDays(lowb, upb):
    	self.daystoArrive = np.random.uniform(lowb, upb)

#class facilityOrder:
#    def __init__(self, amount, daystoArrive):
#        self.amount = amount
#        self.daystoArrive = daystoArrive
#function checkInv(facility, )

class customerOrder:
	def __init__(self, amount):
		self.amount = amount
''' Instances of class facilities, describing network structure
'''
fac0 = Facility(0, 0, 0, 0, 0, 0, None)
fac1 = Facility(1000, 500, 0, 0, 40000, 40000, fac0)
fac2 = Facility(600, 400, 0, 0, 6000, 8000, fac1)
fac3 = Facility(500, 300, 0, 0, 5000, 7000, fac1)
fac4 = Facility(400, 300, 0, 0, 8000, 6000, fac1)

# Instances of class facilityOrder
facorder1 = facilityOrder(0, 1, 10, 15,0) # facility 0 with infite inventory
#facorder2 = facilityOrder(1, 2, 4, 8)
#facorder3 = facilityOrder(1, 3, 5, 10)
#facorder4 = facilityOrder(1, 4, 4, 10) 

T = 365
t = 0
serviceLevel = 0.95
facilities = [fac1, fac2, fac3, fac4]
#timetoArrive = [0, 0, 0, 0]

# Instances of class customer Order, track amount of customer order
c_order1 = customerOrder(0) 
c_order2 = customerOrder(0) 
c_order3 = customerOrder(0) 
c_order4 = customerOrder(0) 

# Initilize facility orders, keep track of it
facility_orders = [facorder1]

# Simulation
while (t < 1):
	# Keep tracking of all facility orders 
    if facility_orders:                       # facility_orders list is not empty
        for i, facorder in enumerate(facility_orders):
            facorder.daystoArrive -= 1         # update days to arrive facilities
            
            if(facorder.daystoArrive == 0):
                target = facorder.fac_to - 1
                facilities[target].orderArrive() # update inventory of facility 
        
	# Generate daily customer demand for each facility 
    customer_orders = [c_order1, c_order2, c_order3, c_order4]
    
    # Deal with customer order
    for i, fac in enumerate(facilities):
        while (customer_orders[i].amount <= 0):       
            customer_orders[i].amount = np.random.normal(fac.mean, 
            	                                         fac.std)
        # Place order if there exist enough on-hand inventory
        if fac.inv_onhand > customer_orders[i].amount:
            fac.invSend(customer_orders[i].amount)
        else:
        	print('Unsasified order!')
        
        # If inventory position is less than reorder point, reorder immediately
        if fac.inv_pos < fac.rp:
            if fac.root == fac0:
            	fac.orderPlaced(fac.oq)
        # TO DO, generate new orders

            	neworder = facilityOrder(fac0, fac, 10, 15)
                facility_orders.append(neworder)
            elif fac.root.inv_onhand > fac.oq:
            	fac.orderPlaced(fac.oq)     
            	fac.root.invSend(fac.oq)
           
           

	
    if facorder.fac_from != 0:
            facilities[facorder.fac_from-1].invSend(facilities[target].oq)
	
	# Check inventory at the end of each day

	# Update time
    t += 1



