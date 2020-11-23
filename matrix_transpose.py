import numpy as np
import random
import math

#First, You will be asked to enter the shape of rows, Followed by shape of columns. (X, Y)
#After that, Enter each element row wise when prompted, When first row is complete it prompts you to enter element from next row.

#Try entering this array as an example:- [[1 2 3]
#                                         [4 5 6]
#                                         [7 8 9]
#                                         [3 4 7]]

#You will get the answer as such: -   [[1 4 7 3]
#                                      [2 5 8 4]
#                                      [3 6 9 7]]




#Logic for storing your entered numbers in an array 
num_rows = int(input("enter the number of rows you want to add to your array:  "))

num_col = int(input("enter the number of columns you want to add to your array:  "))

final_arr = []


col = []

for i in range(0, num_rows):
    row = []
    for j in range(0, num_col):
        element = int(input("Enter the {} th element of the {} th row:  ".format(j+1,i+1)))
        row.append(element)
    
    final_arr.append(row)
    
    
final_arr = np.array(final_arr)

#Printing your entered array along with it's Shape.
print("your entered 2D array is:  ")
print(final_arr)
print(final_arr.shape)
print("\n")



#Logic for transpose of matrix you entered:---
trans_arr = []

counter = 0
over = False
new_trans = []
while(over!=True):
    if(counter==num_col):
        over = True
        break
    temp_arr = []
    
    for i in final_arr:
        temp_arr.append(i[counter])
    trans_arr.append(temp_arr)
    counter = counter + 1
    

 
 
    
#Printing the result: ----    
print("Your original 2D array is:   ")
print(final_arr) 
print("Original 2D array's shape is:   {}".format(final_arr.shape))

print("\n")   
    
trans_arr = np.array(trans_arr)
print("Transpose of your 2D array is:  ")
print(trans_arr)
print("Transposed 2D array's shape is:  {}".format(trans_arr.shape))

    
    

    
    
    
   
        
       
            
        
        
        