import pandas as pd
import numpy as np
import matplotlib.pyplot as pt


x=np.array([[5,2,6,1,10],[1.3,2.5,3.5,5.7,4.5],[1,0,0,1,1]])
y=np.array([1,0,0,1,1])

left_arr1=np.zeros((2,5))
right_arr1=np.zeros((2,5))
y_arr1=np.array([0])
y_arr2=np.array([0])
left_arr2=np.zeros((2,5))
right_arr2=np.zeros((2,5))
# creating a splits


def splits(left_array,right_array,index,y_arr):
    split=x[0,0] 
    a=0
    b=0
    for i in range(len(y)):
        if split>=x[index,i]:
            left_array[0,a]=(x[index,i]) 
            left_array[1,a]=(x[2,i]) 
              
            a+=1  
        else:
            right_array[0,b]=(x[index,i])
            right_array[1,b]=(x[2,i]) 
        
            
            b+=1
            
splits(left_arr1,right_arr1,0,y_arr1)      
splits(left_arr2,right_arr2,1,y_arr2)      
# print("left_arr1:",left_arr1,"\n" ,"right arr1:" ,right_arr1,"y_arr1: \n")
# print("left_arr2:",left_arr2,"\n","right arr2:" ,right_arr2,"y_arr2: \n")


# calculating Information Gain, That is using Gini
def _count_(arr):
    return np.count_nonzero(arr[1:])


def calculate_Gini(arr):
    total_items=len(arr[0])
    n_items= len(np.array([z for z in arr[0] if z!=0]))
    p=n_items/total_items
    ones=_count_(arr)
    zeros=n_items-ones
    p_arr=((1-((ones/n_items)**2+(zeros/n_items)**2))*p)
    print(f"total items of {arr}\n  \t {total_items}\n \t nitems= {n_items}\n \t ones:{ones} \t zeros:{zeros} \t p_arr:{p_arr}\n")
    
    return p_arr
    
    
gini1=calculate_Gini(left_arr1) +calculate_Gini(right_arr1)
print(gini1)