import timeit
import time
import random

'''
num_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
num_to_find = 15

# CODED RECURSIVELY

def binarySearch (arr, l, r, x): 
  
    # Check base case 
    if r >= l: 
  
        mid = l + (r - l)//2
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
          
        # If element is smaller than mid, then it  
        # can only be present in left subarray 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
  
        # Else the element can only be present  
        # in right subarray 
        else: 
            return binarySearch(arr, mid+1, r, x) 
  
    else: 
        # Element is not present in the array 
        return -1
'''  

  
# -----------------------------------------------------------------------

# CODED ITERATIVELY

def binary_search(mylist, find): 
    while len(mylist) > 0: 
        mid = (len(mylist))//2
        if mylist[mid] == find: 
            return True
        elif mylist[mid] < find: 
            mylist = mylist[:mid] 
        else: 
            mylist = mylist[mid + 1:] 
    return False



# -----------------------------------------------------------------------

#    https://www.geeksforgeeks.org/timeit-python-examples/

def binary_time(): 
    SETUP_CODE = ''' 
from __main__ import binary_search 
from random import randint'''
  
    TEST_CODE = ''' 
mylist = [x for x in range(10000)] 
find = randint(0, len(mylist)) 
binary_search(mylist, find)'''
      
    # timeit.repeat statement 
    times = timeit.repeat(setup = SETUP_CODE, 
                          stmt = TEST_CODE, 
                          repeat = 3, 
                          number = 10000) 
  
    # priniting minimum exec. time 
    print('Binary search time: {}'.format(min(times)))  




if __name__ == "__main__": 
#    linear_time() 
    binary_time() 




'''
# ------------------- Function call / Timing call -------------------------

#print("Recursive call")
t0=time.time()
print(binarySearch(num_list, 0, len(num_list)-1, num_to_find) )
t1=time.time()

tTotal=t1-t0

print(tTotal)
print()
# -------------------------------------------------------------------------

arr = [ 2, 3, 4, 10, 40 ] 
x = 10
#print("Iterative call")
stime=time.time()
print(binary_search(num_to_find, num_list) )
etime=time.time()

tTotal2 =etime-stime

print(tTotal2)

# ---------------------------------------------------------------------------
'''














