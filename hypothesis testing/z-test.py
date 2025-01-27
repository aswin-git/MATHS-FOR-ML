from scipy.stats import norm
import numpy as np
import math

sample = [10,20,30,40,50,60,70,80]
alpha = 0.05
population_mean = 60
population_std = 25
size = len(sample)

#mean calculation
sample_mean = sum(sample)/size
print(f"Sample Mean - {sample_mean}")

#standard deviation calculation
sq_var = sum([(x - sample_mean)**2 for x in sample])
var  = sq_var/(size-1)
std = math.sqrt(var)
print(f"Stadard Deviation - {std}")

z_stat = (sample_mean - population_mean)/(population_std/(math.sqrt(size)))
z_criticat = norm.ppf(1-alpha/2)

print(f"Z-Value - +or-{z_stat}\nCRUITAL VALUE - {z_criticat}")

if abs(z_stat)>z_criticat:
    print("Reject null hypothesis")
else:
    print("Failed to reject the null hypothesis")

