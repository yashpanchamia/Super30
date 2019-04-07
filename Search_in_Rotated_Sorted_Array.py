'''An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster than linear time. If the element doesn't exist in the array, return null.

For example, given the array [15, 19, 25, 2, 7, 10] and the element 7, return 4 (the index of 8 in the array).
'''

def binary_search_rotated(nums,target):
    left = 0
    n = len(nums)
    right = n-1

    while left<=right:
        # print(left,right)
        mid = (left+right)//2   #Integer division in python is done using operator '//'
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:         
            if nums[right]<=target and nums[mid]<nums[right]:       #right half is normally sorted     
                left = mid+1                                #target lies in the right half
            else:                                           
                right = mid-1                               #target lies in the left half
        
        elif nums[mid]>target:           
            if target>=nums[left] and nums[left]<nums[mid]:         #left half is normally sorted
                right = mid-1                               #target lies in the left half
            else:                                           
                left = mid+1                                #target lies in the right half
    
    return -1

numbers =  [15, 19, 25, 2, 7, 10]
target = 7
index = binary_search_rotated(numbers,target)
print("Index: ",index)

#Time Complexity: O(log(n))
#Space Complexity: O(1)

