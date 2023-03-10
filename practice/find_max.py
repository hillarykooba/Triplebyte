'''
As we iterate through nums, we want max_num to keep track of the largest number we've seen so far. Whenever we encounter a new largest number, we'll go ahead and update max_num to that value. Once we finish looping through nums, max_num will hold the largest value in the entire list!
'''

def find_max(nums):
    max_num = float("-inf") # smaller than all other numbers
    for num in nums:
        if num > max_num:
            # (Fill in the missing line here)
    return max_num

# Output: max_num = num
