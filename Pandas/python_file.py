# def print_diamond(n, i=0):
#     if n <= 0:
#         return
#     print(' ' * (n - 1) + '*' * (2 * i + 1))
#     print_diamond(n - 1, i + 1)
#     print(' ' * (n - 1) + '*' * (2 * i + 1))

# print_diamond(4)
import pandas as pd
import numpy as np
x= np.arange(16).reshape(4,4)*2
print(x)

data= pd.DataFrame(x,
index = ['Lahore', 'Karachi', 'Peshawar', 'Islamabad'],
columns = ['a', 'b',"c","d"])
# print(data[:])
# print(data.loc['Lahore':'Peshawar'][:-1])
# print(data)
# print(data.iloc[1])
print(data.iloc[1:2 , 1:3])


