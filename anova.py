import numpy as np
from scipy.stats import f
import math

strat_1 = np.array([10,20,30,40,50,60,70])
strat_2 = np.array([20,10,40,55,65,75,85])
strat_3 = np.array([35,15,13,16,70,50,70])
alpha = 0.05
nos = 3
#length
n1 = len(strat_1)
n2 = len(strat_2)
n3 = len(strat_3)

#mean calculation
total_mean = np.mean(np.concatenate([strat_1,strat_2,strat_3]))
mean1 = strat_1.sum()/n1
mean3 = strat_3.sum()/n3
mean2 = strat_2.sum()/n2
print(f"mean 1 - {mean1}\nmean 2 - {mean2}\nmean3 - {mean3}")
#ssb and ssw calculation
ssb = n1*(mean1 - total_mean)**2 + n2*(mean2 - total_mean)**2 + n3*(mean3 - total_mean)**2 
ssw = np.sum(strat_1 - mean1)**2 + np.sum(strat_2 - mean2)**2 + np.sum(strat_3)**2
print(f"SSB - {ssb}\nSSW - {ssw}")

df_b = nos - 1
df_c = (n1+n2+n3) - nos
msb = ssb/df_b
msw = ssw/df_b
f_stat = msb/msw
critical = f.ppf(1-alpha,df_b,df_c)
print(f"MSB - {msb}\nMSW - {msw}\nCritical value - {critical}")

#decision rule 
if abs(f_stat)<critical:
    print("Reject Null Hypothesis")
else:
    print("unable to reject the Null Hypothesis")


