item_cost = 500
item_qty = 3
special_client = 1
total_order_cost = item_cost * item_qty
descount_pct = 0
if total_order_cost >= 1000:
    if special_client == 1:
        descount_pct = 20
    else:
        descount_pct = 10

descount_val = total_order_cost * descount_pct /100
print('total order cost before discount = ', total_order_cost)
total_order_cost = total_order_cost - descount_val
print('discount pct=',descount_pct)
print('descount val =', descount_val)
print('total order cost after discont =', total_order_cost)

