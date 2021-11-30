# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 17:05:09 2021

@author: sagar kumar
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 15:58:59 2021
@author: Admin
"""
#-------------------------Reading & Writing data in Files----------------------

import pandas

# Reading CSV Files with Pandas:
df = pandas.read_csv('C:/Users\sagar kumar\Desktop/User_Data.csv')
print(df)

# Writing CSV Files with Pandas:
df.to_csv('C:/Users\sagar kumar\Desktop/IIT-B.csv')

# Reading Excel Files with Pandas
df1 = pandas.read_excel('C:/Users\sagar kumar\Desktop/User_Data.xlsx')

df2 = pandas.read_excel('User_Data.xlsx')
print(df1)

# Writing Excel Files with Pandas 
df1.to_excel('C:/Users\sagar kumar\Desktop/IIT-B.xlsx')
df2 = pandas.DataFrame(df1)
print (df2)