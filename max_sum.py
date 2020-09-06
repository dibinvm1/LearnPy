'''
Function that prints largest possible sum and indices in list of integers
'''
def find_max_sum(a,size): 
  
    max_sum = a[0]
    current_sum = a[0]
    start_index = 0
    end_index = 0
    temp = 0
  
    for i in range(1,size): 
        current_sum += a[i] 

        if max_sum < current_sum: 
            max_sum = current_sum 
            start_index = temp 
            end_index = i 

        if current_sum < 0: 
            current_sum = 0
            temp = i+1
  
    print (f"Max sum is : {max_sum}" )
    print (f"start Index : {start_index}") 
    print (f"end Index : {end_index} ") 
    
a = [-10,-20,-10,-10,-20,-10,-1] 
find_max_sum(a,len(a)) 