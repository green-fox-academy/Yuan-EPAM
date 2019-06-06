### Target
To improve how airlines set prices (**Not Prediction**)

### Problem

```python
def pricing_function(days_left, tickets_left, demand_level):
	"""
	@ days_left : number of days until the flight
	@ tickets_left : number of seats they have left to sell
	@ demand_level : determines how many tickets you can sell at any given prices. (Ticket quantities are capped at the number of seats avaialable)
		quantity_sold = demand_level - price
		
	The output of this function will be drawn from the uniform distribution between 100 and 200.
	"""

```

