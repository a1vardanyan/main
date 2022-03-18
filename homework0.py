import pandas as pd
import numpy as np
import itertools
n = 5
min_v = 1
max_v = 100
box1 = np.zeros(n)
box2 = np.zeros(n)
stone = range(1, n+1)
value = np.random.randint(min_v,max_v,n)
df0 = {'num': stone, 'value': value, 'box1': box1, 'box2':  box2}
df1 = pd.DataFrame(df0)
list1 = pd.DataFrame(list(itertools.product([1, 0], repeat=n)))
list2 = pd.DataFrame(list(itertools.product([0, 1], repeat=n)))
box1_solution = list1*df1.value
box2_solution = list2*df1.value
box1 = list1*df1.value
box1['sum1'] = box1.sum(axis=1)
box1['sum2'] = value.sum()-box1.sum1
box1['net_squared'] = (box1.sum1-box1.sum2)**2
solution = np.array(box1.net_squared[box1.net_squared==box1.net_squared.min()].index)

#weights of stones
pd.DataFrame({'num': stone, 'value': value}).T
#solutions for 1st box
#number 1 means put these stones into the box №1, number 0 means put other stones into the box №2
solution_for_box_1 = list1.loc[solution]
pd.DataFrame(solution_for_box_1).columns = stone
print(solution_for_box_1)
#solutions for 2st box
#number 2 means put this stone into the box №2
solution_for_box_2 = list2.loc[solution]
pd.DataFrame(solution_for_box_2).columns = stone
print(solution_for_box_2)
#other view of correct stones in box_1
print(solution_for_box_1*stone)
#other view of correct stones in box_2
print(solution_for_box_2*stone)
#dataframe to check correctness of specific raw
box1.loc[[11]]