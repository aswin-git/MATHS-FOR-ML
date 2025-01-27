from scipy.stats import chi2
import numpy as np
import math

data = np.array([[20,30,40],
                 [25,25,20]])
alpha = 0.05

row_sum  = data.sum(axis=1)
col_sum = data.sum(axis=0)
total = data.sum()
print(f"row sum - {row_sum}\ncolumn sum - {col_sum}\ntotal sum - {total}")

expected_data = (np.outer(row_sum,col_sum))/total
print(f"Expected Data - {expected_data}")

chi_stat = ((data - expected_data)**2/expected_data).sum()
print(f"chi statistics - {chi_stat}")

df = (data.shape[0]-1)*(data.shape[1]-1)
print(f"df - {df}")

chi_cri = chi2.ppf(1-alpha,df)
print(f"Chi-Critical - {chi_cri}")

if abs(chi_stat)>chi_cri:
    print(f"Reject null hypothesis")
else:
    print(f"Failed to reject the null hypothesis")
