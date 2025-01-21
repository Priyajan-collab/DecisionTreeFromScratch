import pandas as pd
import numpy as np
import matplotlib.pyplot as pt


x = np.array([
    [3, 1, 4, 2, 5, 6, 7, 8, 9, 10],  # Feature 1
    [2.5, 1.0, 3.2, 2.8, 4.5, 5.6, 6.1, 7.3, 8.0, 9.1],  # Feature 2
    [1, 0, 1, 0, 1, 1, 0, 0, 1, 0]  # Class labels (y)
])
y = np.array([1, 0, 1, 0, 1, 1, 0, 0, 1, 0])  

# creating a splits



def grow_tree(index,threshold):
    right_indices= x[index]>threshold
    left_indices=x[index]<=threshold
    left=x[:,left_indices]
    right=x[:,right_indices]
    return left,right
            
    
# print("left_arr1:",left_arr1,"\n" ,"right arr1:" ,right_arr1,"y_arr1: \n")
# print("left_arr2:",left_arr2,"\n","right arr2:" ,right_arr2,"y_arr2: \n")


# calculating Information Gain, That is using Gini
def _count_(arr):
    return np.count_nonzero(arr[2])


def calculate_Gini(arr):
    total_items=x.shape[1]
    n_items= arr.shape[1]
    # print(n_items)
    if total_items!=0:
        p=n_items/total_items
    else:
       return 0
    ones=_count_(arr)
    zeros=n_items-ones
    try:
        if n_items!=0:
            p_arr=((1-((ones/n_items)**2+(zeros/n_items)**2))*p)
        else:
            p_arr=0
    except:
        print(f"n_items:{n_items} when arr:{arr} ")
        return 0
    print(f"total items of \t{arr} \n \t {total_items}\n \t nitems= {n_items}\n \t ones:{ones} \t zeros:{zeros} \t p_arr:{p_arr}\n")
    
    return p_arr


def best_split(index):
    x_unique=np.sort(np.unique(x[index])) 
    best_gini=float("inf") # got no clue and I will test this out
    best_threshold=None
    for threshold in x_unique:
        left_arr1,right_arr1= grow_tree(index,threshold) 
        
        gini1=calculate_Gini(left_arr1) +calculate_Gini(right_arr1)
        print(gini1,"\n")
        
        if gini1<best_gini:
            best_threshold=threshold
            best_gini=gini1
    return best_gini,float(best_threshold)
        


print(best_split(0))
