'''
Coding Ninja :> https://www.codingninjas.com/studio/problems/implement-upper-bound_8165383

Problem Statement: Given a sorted array of N integers and an integer x, write a program to find the upper bound of x.
Example :
Input Format: N = 4, arr[] = {1,2,2,3}, x = 2
Result: 3
Explanation: Index 3 is the smallest index such that arr[3] > x.
'''

# Brute Force 
def brute(arr,x):
    n = len(arr)
    for i in range (n):
        if arr[i] > x :
            return i 
    return n

# Test Run 
# print(brute([1,2,2,3],2))

# Optimal Approach 
def optimal (arr,x):
    n = len(arr)
    low = 0 
    high = n-1 
    ans = n 
    while (low <= high ):
        mid = (low + high) // 2 
        if arr[mid] > x :
            ans = mid 
            high = mid -  1 
        else : 
            low = mid +1 
    return ans

# Test Run 
print(optimal([1,2,2,3],2))

