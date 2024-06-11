import math

loanamount = 100000
monthlyintrestrate = 0.01
numberofyears = 7
moonthly_payment1 = loanamount * monthlyintrestrate
monthly_payment2 = 1 - (1 / (math.pow( 1+monthlyintrestrate , numberofyears * 12)))
monthly_payment = moonthly_payment1 / monthly_payment2
print('monthle payment = ',round(monthly_payment,2))
total_payment = (monthly_payment*numberofyears*12)
print('total payment = ',round(total_payment,2))
