from scipy.stats import t
import numpy as np
import math

sample = np.array([10,20,30,40,50,60,70,80,90])
population_mean = 40
alpha = 0.05

n = len(sample)
df = n-1

#mean calculation
mean = sum(sample)/n
print(f"Mean - {mean}")

#standard deviation
sum_sq = sum([(x-mean)**2 for x in sample])
var = sum_sq/math.sqrt(n)
std = math.sqrt(var)
print(f"Standard deviation - {std}")

# T- calculation
t_stat = (mean - population_mean)/(std/math.sqrt(n))
t_critical = t.ppf(1-alpha/2,df)

if abs(t_stat)>t_critical:
    print("REJECT THE NULL HYPOTHESIS")
else:
    print("UNABLE TO REJECT NULL HYPOTHESIS")

