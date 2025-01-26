import numpy as np

X = np.array([
    [3, 1, 4, 2, 5, 6, 7, 8, 9, 10],  
    [2.5, 1.0, 3.2, 2.8, 4.5, 5.6, 6.1, 7.3, 8.0, 9.1],
    [2.5, 1.0, 3.2, 12.8, 4.9, 2.0006, 6.8, 7.3, 20.0, 9.1],  
      
])
Y = np.array([1, 0, 1, 0, 1, 1, 0, 0, 1, 0])  

class DecisionTree:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.original_X=self.x
        self.original_Y=self.y
    
        
        pass
    
    def split_tree(self,index,threshold):
        self.left_indices=self.x[index]<=threshold
        self.right_indices=self.x[index]>threshold
        left=self.x[index,self.left_indices]
        right=self.x[index,self.right_indices]
        
        return left,right
    
    def _calculate_gini(self,l_arr,R_arr):
        total_items=len(self.y)
        total_items_left=len(l_arr)
        total_items_right=len(R_arr)
        target_val_left= len([np.array(self.y[self.left_indices]) for x in (self.y[self.left_indices]) if x>0]) #basically flexing my numpy skills, first i am shrinking y such that it is equivalent to x and then i am checking for y >1 then i am counting it
        target_val_right=len([np.array(self.y[self.right_indices]) for x in (self.y[self.right_indices]) if x>0]) # I truly hope there's better way to do this
        
        #calculating the probability in each tree
        pt_l=total_items_left /total_items
        pt_R=total_items_right /total_items
        
        #calculating left and right gini
       
        left_gini=(1-(np.square(target_val_left/total_items_left)+np.square((target_val_left-total_items_left)/total_items_left))) *pt_l
        if total_items_right !=0:
            right_gini=(1-(np.square(target_val_right/total_items_right)+np.square((target_val_right-total_items_right)/total_items_right))) *pt_R
        else:
            right_gini=0
        gini= left_gini+right_gini
        return gini
        # print(f'total items in left and right :{total_items_left,total_items_right} \n target values in left and right :{target_val_left,target_val_right}')
    
    def calculate_best_gini(self,index):
        x_unique=np.unique(np.sort(self.x[index]))
        best_gini=float('inf')
        
        best_threshold=None
        for i,threshold in enumerate(x_unique):
            left,right=self.split_tree(index,threshold)
            # print(f'\n iteration:{i} \n left:{left} \n  right:{right}\n')
            gini=self._calculate_gini(left,right)
            if gini<best_gini:
                best_gini=gini
                best_threshold=threshold
               
        return best_threshold,best_gini ,index
                            
    def find_best_Gini_Threshold_all(self):
        self.best_gini_all=float("inf")
        self.best_threshold_all=None
        index=None
        self.feature=None
        
        for i in range(self.x.shape[0]):
            best_threshold_all_calc,best_gini_all_calc ,index=self.calculate_best_gini(i)
            if best_gini_all_calc<self.best_gini_all:
                self.best_gini_all=best_gini_all_calc
                self.best_threshold_all=best_threshold_all_calc
                self.feature=index
            
            
        print(f"best gini all : {self.best_gini_all} and best threshold all : {self.best_threshold_all} from feature :{self.feature}")
        return self.best_threshold_all,self.feature,self.best_gini_all
    
    # divide left or right branches into sub branches
    def _grow_branch(self,indices):
        self.x=self.original_X[:,indices]
        self.y=self.original_Y[indices]
        print(self.x, self.y)
        new_threshold,new_index,self.best_gini_all=self.find_best_Gini_Threshold_all()
        best_left,best_right=self.split_tree(new_index,new_threshold)
        print(self.y[self.right_indices],self.y[self.left_indices])
        if self.best_gini_all!=0:
            self.grow_tree()
        
        
        
    
    def grow_tree(self):
        self.find_best_Gini_Threshold_all()
        best_left,best_right=self.split_tree(self.feature,self.best_threshold_all)
        # print(self.right_indices,self.left_indices)
        self._grow_branch(self.left_indices)
        
    
        
        
        





#creating object
obj=DecisionTree(X,Y)
obj.grow_tree()
        