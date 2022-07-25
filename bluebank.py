# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 21:30:07 2022

@author: sankalp
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Method 1 to read .json
json_file = open('loan_data_json.json')
data = json.load(json_file)

# Method 2 to read .json
with open('loan_data_json.json') as json_file:
    data = json.load(json_file)
    
# transform to dataframe
loandata = pd.DataFrame(data)

# finding unique values for purpose column
loandata['purpose'].unique()

# describe the loan data
loandata.describe()

# describe data for a specific column
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

# using exp() for getting annual income
income = np.exp(loandata['log.annual.inc'])
loandata['AnnualIncome'] = income

# FICO score

# fico >= 300 and < 400: 'Very Poor'
# fico >= 400 and ficoscore < 600: 'Poor'
# fico >= 601 and ficoscore < 660: 'Fair'
# fico >= 660 and ficoscore < 780: 'Good'
# fico >=780: 'Excellent'

category = []
length = len(loandata)

for x in range(length):
    fico = loandata['fico'][x]
    try:
        if fico >= 300 and fico < 400:
            ficocat = 'Very Poor'
        elif  fico >= 400 and fico < 600: 
            ficocat = 'Poor'
        elif  fico >= 601 and fico < 660: 
            ficocat = 'Fair'
        elif  fico >= 660 and fico < 700: 
            ficocat = 'Good'
        elif  fico >= 700: 
            ficocat = 'Excellent'    
        else:
            ficocat = 'Unknown'
    except:
        ficocat = 'Error - Unknown'  
    category.append(ficocat)

category = pd.Series(category)

loandata['fico.category'] = category 
 

# df.loc as conditional statement
# df.loc[df[columnname] condition, newcolumnname] = 'value is condition is met'

# for interest rates >0.12 then high else low, new column is wanted
loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'


# number of loans/rows by fico.category
catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color = 'green', width = 0.3)
plt.show()

purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.bar(color = 'blue', width = 0.3)
plt.show()

# scatter plots
ypoint = loandata['AnnualIncome']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint, color = '#4caf50')
plt.show()

# write back to csv
loandata.to_csv('loan_cleaned.csv', index=True)






























