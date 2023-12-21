import random
import time

def find_pairs_naive(lst, target):
    '''
    returns pairs of numbers that are in a list that sum up to a given target value
    '''
    pairs = set()                                                                                        # 2
    for i in lst:                                                                                        # n
        for j in lst:                                                                                    # n  
            if (i + j == target) and (i + i != target) and (j + j != target):                            # 6 (add then compare 3 times)
                if (i, j) and (j, i) not in pairs:                                                       # 1 (compares once)
                    pairs.add((i, j))                                                                    # 1
    return pairs                                                                                         # 1  
#                                                                                                        worst case = 3 + 6n^2 + 2n^2 = O(n^2)  (exponential) 
#                                                                                                        best case = 2 = O(2)                   (constant)

'''
Brief Explanation:
    This functions time complexity is O(n^2) because of the nested loop. 
    It needs to iterate over a list for each elements combination, twice, which 
    is why it takes much longer compared to the optimized function
'''

def find_pairs_optimized(lst, target):
    '''
    returns pairs of numbers that are in a list that sum up to a given target value (optimized for O(n))
    '''
    if lst == []:                                                                                        # 1
        return set()                                                                                     # 1
    else:
        pairs = set()                                                                                    # 2
        setList = set()                                                                                  # 2
        for i in lst:                                                                                    # n
            num = target - i                                                                             # 3n
            if num in setList:                                                                           # 1n
                if i > num:                                                                              # 1n
                    pairs.add((num, i))                                                                  # 1n
                else:
                    pairs.add((i, num))                                                                  # 1n
            setList.add(i)                                                                               # 1n
        return pairs                                                                                     # 1   
#                                                                                                        worst case = 6 + 9n = O(n)    (linear)
#                                                                                                        best case = 1 + 1 = O(2)      (constant)

'''
Brief Explanation:
    This functions time complexity is O(n) because it is iterating over a set instead of a list.
    This means that instead of checking every element and its combination, twice, it only needs
    one for loop effectively cutting down the time the function takes to run.  
'''

def measure_min_time(fn, args):
    '''
    measures minimum time taken for a function to run, out of 10 trials
    '''
    min_time = float('inf')
    for i in range(10):
        start = time.time()
        fn(*args)
        end = time.time()
        min_time = min(min_time, end-start)
        return min_time

test_lst = [10, 50, 100, 250, 500, 1000, 5000, 10000]
print('           n             find_pairs_optimized     find_pairs_naive')
print('__________________________________________________________________________________')

for i in test_lst:

    test_input = [*range(1,i)]      #creats list of length 1-n
    random.shuffle(test_input)      #stops a sorted list from giving best case scenario by shuffling
    target = test_input[5]          #list is random at this point, so this random target will test duplicates 

    #below creates tests for both functions above, returning their respective run times, rounded to 4 places
    test1 = measure_min_time(find_pairs_optimized, (test_input, target))
    test1 = round(test1, 4)
    
    test2 = measure_min_time(find_pairs_naive, (test_input, target))
    test2 = round(test2, 4)

    print(f'           {i}                   {test1}               {test2}             ')

print('____________________________________________________________________________________')