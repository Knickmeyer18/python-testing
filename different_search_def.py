import timeit
import random



README ="README: This is a python file where I am going to try and code different searches."

print("----------------------------------------------------------------------------------")
print(README)
print("----------------------------------------------------------------------------------")

#test list

num_list = [x for x in range(100)] 

num_to_find = randint(0, len(num_list))
#print(type(num_to_find))

def list_printer(list):
    
    print(list)    
    print()
    #printing the length of the list 
    print("-Length of the list: ",len(list))
    print()
    #printing out the type of list (it should always say list)
    print("-'type' of list: ", type(list), " ===> this should always say 'list' ")
    print()
    #printing the 'type' of the first two elements inside the list 
    print("-'type' of 1st element in list: ", type(list[0]))
    print()
    print("-'type' of the 2nd element in list: ", type(list[1]))

# ----------------------------------------------------------------------------------------

# Linear / Brute-force search

def brute_force_search(list, num_to_find):

    answer = 0
    for elements in list:
        
        if elements == num_to_find:
            answer = elements
            return answer
            break

# ----------------------------------------------------------------------------------------

# Binary search

'''
def binary_search(list, num_to_find):
    answer=0

    list_length = len(list)
    #return list_length
    first_half_list = list[:list_length//2]
    #return first_half_list
    second_half_list = list[list_length//2:]
    #return second_half_list

    for elements in 
'''

# ----------------------------------------------------------------------------------------
# FUNCTION CALLS / TIMING CALLS
# ----------------------------------------------------------------------------------------

#list_printer(num_list)      # this is calling the list_printer function



#print(binary_search(num_list, num_to_find))
