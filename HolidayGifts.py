import time
import numpy as np
with open('gift_costs.txt') as f:
        gift_costs = f.read().split('\n')
gift_costs = np.array(gift_costs).astype(int)