#Get the projected total sales.
#6/19/2020
#CTI-110 P2T1 - Sales Prediction
#Jonathan Dutton

#Get the projected total sales.
total_sales = float(input('Enter the projected sales:'))

# Calculate the profit as 23 percent of the total sales.
profit = total_sales * 0.23

# Display the profit.
print('The proit is $', format(profit, ',.2f'))
