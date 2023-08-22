import pandas as pd 
import numpy as np
data={'days':[0,1,2,3,4,5,6,7,8,9],'steps':[4335,9552,7332,4504,5335,7552,8332,6504,8965,7689]}
p=pd.DataFrame(data)
print(p)
i=p['steps']=p['steps']+10000
print(i)
w=p['steps']>=7000
print(w)
print(p.loc[p['steps']>7000])
